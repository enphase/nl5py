# Copyright 2024 Enphase Energy, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import pandas as pd
import numpy as np
from .nl5_dll.commands import *
import ctypes as ct

# decorator which will check for NL5 errors
def check(func):
    def checked(*args, **kwargs):
        returned = func(*args, **kwargs)

        # check for any NL5 errors and throw exception if there is an error
        error = NL5_GetError()
        if error != b"OK":
            raise Exception(error.decode("utf-8"))

        return returned

    return checked


class Schematic:
    @check
    def __init__(self, filename):
        self.circuit = NL5_Open(filename.encode())

    @check
    def set_value(self, name, value):
        NL5_SetValue(self.circuit, name.encode(), value)

    @check
    def set_text(self, name, text):
        NL5_SetText(self.circuit, f"{name}".encode(), text.encode())

    @check
    def get_value(self, name):
        value = ct.c_double()
        NL5_GetValue(self.circuit, name.encode(), value)
        return value.value

    @check
    def get_text(self, name, length=100):
        text = ct.create_string_buffer(length)
        NL5_GetText(self.circuit, name.encode(), text, length)
        return text.value.decode("utf-8")

    @check
    def simulate_transient(self, screen, step):
        NL5_SetStep(self.circuit, step)
        NL5_Start(self.circuit)
        NL5_Simulate(self.circuit, screen)

    @check
    def simulate_interval(self, screen, step):
        NL5_SetStep(self.circuit, step)
        NL5_Start(self.circuit)
        NL5_SimulateInterval(self.circuit, screen)

    @check
    def continue_transient(self, screen, step):
        NL5_SetStep(self.circuit, step)
        NL5_Simulate(self.circuit, screen)

    @check
    def continue_interval(self, screen, step):
        NL5_SetStep(self.circuit, step)
        NL5_SimulateInterval(self.circuit, screen)
    

    def get_trace_names(self, length=100):
        num_traces = NL5_GetTracesSize(self.circuit)
        trace_names = num_traces * [""]
        for i in range(num_traces):
            trace_number = NL5_GetTraceAt(self.circuit, i)

            trace_name = ct.create_string_buffer(length)
            NL5_GetTraceName(self.circuit, trace_number, trace_name, length)
            trace_names[i] = trace_name.value.decode("utf-8")
        return trace_names

    @check
    def add_trace(self, name, trace_type="Func"):
        # map the correct trace adding function
        func = {
            "V": NL5_AddVTrace,
            "I": NL5_AddITrace,
            "P": NL5_AddPTrace,
            "Var": NL5_AddVarTrace,
            "Func": NL5_AddFuncTrace,
            "Data": NL5_AddDataTrace,
        }[trace_type]

        func(self.circuit, f"{name}".encode())

    @check
    def delete_trace(self, name):
        trace_number = self.get_trace_number(name)
        NL5_DeleteTrace(self.circuit, trace_number)

    def clear_traces(self):
        trace_number = NL5_GetTraceAt(self.circuit, 0)
        while trace_number >= 0:
            NL5_DeleteTrace(self.circuit, trace_number)
            trace_number = NL5_GetTraceAt(self.circuit, 0)

    @check
    def get_trace_number(self, trace):
        return NL5_GetTrace(self.circuit, trace.encode())

    @check
    def get_data_at(self, trace, n):
        trace_number = self.get_trace_number(trace)

        t = ct.c_double()
        data = ct.c_double()
        NL5_GetDataAt(self.circuit, trace_number, n, t, data)

        return t.value, data.value
    
    @check
    def get_last_data(self, trace):
        trace_number = self.get_trace_number(trace)

        t = ct.c_double()
        data = ct.c_double()
        NL5_GetLastData(self.circuit, trace_number, t, data)

        return t.value, data.value

    @check
    def get_trace_data(self, trace):
        trace_number = self.get_trace_number(trace)

        # get the data length
        n = NL5_GetDataSize(self.circuit, trace_number)

        # extract the data
        data = np.empty((2, n))
        for i in range(n):
            data[:, i] = self.get_data_at(trace, i)

        # convert to a pandas series
        return pd.Series(index=data[0, :], data=data[1, :], name=trace)

    def get_data(self, traces=None, fill=True):
        # if no traces are specified, assume user wants all traces
        if traces is None:
            traces = self.get_trace_names()

        # concatenate the data into a single DataFrame
        data = pd.concat(
            [self.get_trace_data(trace) for trace in traces], axis=1, sort=True
        )

        if fill:
            data.ffill(inplace=True)

        return data

    @check
    def set_ac_source(self, name):
        NL5_SetACSource(self.circuit, name.encode())

    @check
    def add_ac_trace(self, name, trace_type="Func"):
        # map the correct trace adding function
        func = {
            "V": NL5_AddVACTrace,
            "I": NL5_AddIACTrace,
            "Func": NL5_AddFuncACTrace,
        }[trace_type]

        func(self.circuit, f"{name}".encode())

    @check
    def add_z_trace(self):
        NL5_AddZACTrace(self.circuit)

    @check
    def add_gamma_trace(self):
        NL5_AddGammaACTrace(self.circuit)

    @check
    def add_vswr_trace(self):
        NL5_AddVSWRACTrace(self.circuit)

    @check
    def add_loop_trace(self):
        NL5_AddLoopACTrace(self.circuit)

    @check
    def simulate_ac(self, start_frequency, stop_frequency, num_points, log_scale=True):
        NL5_SetAC(
            self.circuit, start_frequency, stop_frequency, num_points, int(log_scale)
        )
        NL5_CalcAC(self.circuit)

    @check
    def get_ac_trace_number(self, trace):
        return NL5_GetACTrace(self.circuit, trace.encode())

    @check
    def get_ac_data_at(self, trace, n):
        trace_number = self.get_ac_trace_number(trace)

        f = ct.c_double()
        mag = ct.c_double()
        phase = ct.c_double()
        NL5_GetACDataAt(self.circuit, trace_number, n, f, mag, phase)

        return f.value, mag.value, phase.value

    @check
    def get_ac_trace_data(self, trace):
        trace_number = self.get_ac_trace_number(trace)

        # get the data length
        n = NL5_GetACDataSize(self.circuit, trace_number)

        # extract the data
        data = np.empty((3, n))
        for i in range(n):
            data[:, i] = self.get_ac_data_at(trace, i)

        # convert to a dataframe with a hierarchical index
        df = pd.concat(
            {
                trace: pd.DataFrame(
                    index=data[0, :],
                    data={"magnitude": data[1, :], "phase": data[2, :]},
                )
            },
            axis=1,
        )

        return df

    @check
    def get_ac_data(self, traces):
        return pd.concat(
            [self.get_ac_trace_data(trace) for trace in traces], axis=1, sort=True
        ).ffill()

    @check
    def save(self):
        NL5_Save(self.circuit)

    @check
    def saveas(self, filename):
        NL5_SaveAs(self.circuit, filename.encode())
    
    def set_analog_filter_params(name: str, *, sos=None, a=None, b=None):
        """
        Configure an analog filter using a specified name and either second-order sections (sos) 
        or polynomial coefficients (a, b).

        Parameters:
        - name (str): A string representing the name of the filter (e.g., "lowpass").
        - sos (array-like, optional): Second-order sections array (e.g., output of scipy.signal functions).
        - a (array-like, optional): Denominator polynomial coefficients.
        - b (array-like, optional): Numerator polynomial coefficients.

        Raises:
        - ValueError: If both or neither of 'sos' and ('a', 'b') are provided.
        """
        # Validate name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Filter name must be a non-empty string.")

        # Ensure only one of `sos` or `a` and `b` is provided
        if sos is not None and (a is not None or b is not None):
            raise ValueError("Provide either 'sos' or both 'a' and 'b', not both.")
        if sos is None and (a is None or b is None):
            raise ValueError("Provide either 'sos' or both 'a' and 'b'.")

        # Determine filter type
        filter_type = "SOS-based" if sos is not None else "Polynomial-based"
        print(f"Configuring analog {filter_type} filter named '{name}'.")

        # Determine Filter order
        order = len(a) if a is not None else len(sos)
        print(f'order = {order}')

        # Example logic: Print parameters for debugging (replace with real configuration)
        if sos is not None:
            print(f"SOS: {sos}")
        else:
            print(f"Numerator coefficients (b): {b}")
            print(f"Denominator coefficients (a): {a}")
