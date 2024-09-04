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

from pathlib import Path
import os
import ctypes as ct
from . import nl5_lib


def load_license(filepath):
    return_code = NL5_GetLicense(filepath.encode())

    # if return_code!=0, there was an issue with the license, so read
    # the error register and raise exception
    if return_code != 0:
        error = NL5_GetError().decode("utf-8")
        raise Exception(error)

    # otherwise, the error register contains license info, which we return
    license_info = NL5_GetError().decode("utf-8")
    return license_info


def NL5_GetError():
    nl5_lib.NL5_GetError.argtypes = []
    nl5_lib.NL5_GetError.restype = ct.c_char_p
    return nl5_lib.NL5_GetError()


def NL5_GetInfo():
    nl5_lib.NL5_GetInfo.argtypes = []
    nl5_lib.NL5_GetInfo.restype = ct.c_char_p
    return nl5_lib.NL5_GetInfo()


def NL5_GetLicense(name):
    nl5_lib.NL5_GetLicense.argtypes = [ct.c_char_p]
    nl5_lib.NL5_GetLicense.restype = ct.c_int
    return nl5_lib.NL5_GetLicense(name)


def NL5_Open(name):
    nl5_lib.NL5_Open.argtypes = [ct.c_char_p]
    nl5_lib.NL5_Open.restype = ct.c_int
    return nl5_lib.NL5_Open(name)


def NL5_Close(ncir):
    nl5_lib.NL5_Close.argtypes = [ct.c_int]
    nl5_lib.NL5_Close.restype = ct.c_int
    return nl5_lib.NL5_Close(ncir)


def NL5_Save(ncir):
    nl5_lib.NL5_Save.argtypes = [ct.c_int]
    nl5_lib.NL5_Save.restype = ct.c_int
    return nl5_lib.NL5_Save(ncir)


def NL5_SaveAs(ncir, name):
    nl5_lib.NL5_SaveAs.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_SaveAs.restype = ct.c_int
    return nl5_lib.NL5_SaveAs(ncir, name)


def NL5_GetValue(ncir, name, v):
    nl5_lib.NL5_GetValue.argtypes = [ct.c_int, ct.c_char_p, ct.POINTER(ct.c_double)]
    nl5_lib.NL5_GetValue.restype = ct.c_int
    return nl5_lib.NL5_GetValue(ncir, name, v)


def NL5_SetValue(ncir, name, v):
    nl5_lib.NL5_SetValue.argtypes = [ct.c_int, ct.c_char_p, ct.c_double]
    nl5_lib.NL5_SetValue.restype = ct.c_int
    return nl5_lib.NL5_SetValue(ncir, name, v)


def NL5_GetText(ncir, name, text, length):
    nl5_lib.NL5_GetText.argtypes = [ct.c_int, ct.c_char_p, ct.c_char_p, ct.c_int]
    nl5_lib.NL5_GetText.restype = ct.c_int
    return nl5_lib.NL5_GetText(ncir, name, text, length)


def NL5_SetText(ncir, name, text):
    nl5_lib.NL5_SetText.argtypes = [ct.c_int, ct.c_char_p, ct.c_char_p]
    nl5_lib.NL5_SetText.restype = ct.c_int
    return nl5_lib.NL5_SetText(ncir, name, text)


def NL5_GetParam(ncir, name):
    nl5_lib.NL5_GetParam.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_GetParam.restype = ct.c_int
    return nl5_lib.NL5_GetParam(ncir, name)


def NL5_GetParamValue(ncir, npar, v):
    nl5_lib.NL5_GetParamValue.argtypes = [ct.c_int, ct.c_int, ct.POINTER(ct.c_double)]
    nl5_lib.NL5_GetParamValue.restype = ct.c_int
    return nl5_lib.NL5_GetParamValue(ncir, npar, v)


def NL5_SetParamValue(ncir, npar, v):
    nl5_lib.NL5_SetParamValue.argtypes = [ct.c_int, ct.c_int, ct.c_double]
    nl5_lib.NL5_SetParamValue.restype = ct.c_int
    return nl5_lib.NL5_SetParamValue(ncir, npar, v)


def NL5_GetParamText(ncir, npar, text, length):
    nl5_lib.NL5_GetParamText.argtypes = [ct.c_int, ct.c_int, ct.c_char_p, ct.c_int]
    nl5_lib.NL5_GetParamText.restype = ct.c_int
    return nl5_lib.NL5_GetParamText(ncir, npar, text, length)


def NL5_SetParamText(ncir, npar, text):
    nl5_lib.NL5_SetParamText.argtypes = [ct.c_int, ct.c_int, ct.c_char_p]
    nl5_lib.NL5_SetParamText.restype = ct.c_int
    return nl5_lib.NL5_SetParamText(ncir, npar, text)


def NL5_GetTracesSize(ncir):
    nl5_lib.NL5_GetTracesSize.argtypes = [ct.c_int]
    nl5_lib.NL5_GetTracesSize.restype = ct.c_int
    return nl5_lib.NL5_GetTracesSize(ncir)


def NL5_GetTraceAt(ncir, index):
    nl5_lib.NL5_GetTraceAt.argtypes = [ct.c_int, ct.c_int]
    nl5_lib.NL5_GetTraceAt.restype = ct.c_int
    return nl5_lib.NL5_GetTraceAt(ncir, index)


def NL5_GetTrace(ncir, name):
    nl5_lib.NL5_GetTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_GetTrace.restype = ct.c_int
    return nl5_lib.NL5_GetTrace(ncir, name)


def NL5_GetTraceName(ncir, ntrace, name, length):
    nl5_lib.NL5_GetTraceName.argtypes = [ct.c_int, ct.c_int, ct.c_char_p, ct.c_int]
    nl5_lib.NL5_GetTraceName.restype = ct.c_int
    return nl5_lib.NL5_GetTraceName(ncir, ntrace, name, length)


def NL5_AddVTrace(ncir, name):
    nl5_lib.NL5_AddVTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddVTrace.restype = ct.c_int
    return nl5_lib.NL5_AddVTrace(ncir, name)


def NL5_AddITrace(ncir, name):
    nl5_lib.NL5_AddITrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddITrace.restype = ct.c_int
    return nl5_lib.NL5_AddITrace(ncir, name)


def NL5_AddPTrace(ncir, name):
    nl5_lib.NL5_AddPTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddPTrace.restype = ct.c_int
    return nl5_lib.NL5_AddPTrace(ncir, name)


def NL5_AddVarTrace(ncir, name):
    nl5_lib.NL5_AddVarTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddVarTrace.restype = ct.c_int
    return nl5_lib.NL5_AddVarTrace(ncir, name)


def NL5_AddFuncTrace(ncir, text):
    nl5_lib.NL5_AddFuncTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddFuncTrace.restype = ct.c_int
    return nl5_lib.NL5_AddFuncTrace(ncir, text)


def NL5_AddDataTrace(ncir, text):
    nl5_lib.NL5_AddDataTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddDataTrace.restype = ct.c_int
    return nl5_lib.NL5_AddDataTrace(ncir, text)


def NL5_DeleteTrace(ncir, ntrace):
    nl5_lib.NL5_DeleteTrace.argtypes = [ct.c_int, ct.c_int]
    nl5_lib.NL5_DeleteTrace.restype = ct.c_int
    return nl5_lib.NL5_DeleteTrace(ncir, ntrace)


def NL5_SetStep(ncir, step):
    nl5_lib.NL5_SetStep.argtypes = [ct.c_int, ct.c_double]
    nl5_lib.NL5_SetStep.restype = ct.c_int
    return nl5_lib.NL5_SetStep(ncir, step)


def NL5_SetTimeout(ncir, t):
    nl5_lib.NL5_SetTimeout.argtypes = [ct.c_int, ct.c_int]
    nl5_lib.NL5_SetTimeout.restype = ct.c_int
    return nl5_lib.NL5_SetTimeout(ncir, t)


def NL5_GetSimulationTime(ncir, t):
    nl5_lib.NL5_GetSimulationTime.argtypes = [ct.c_int, ct.POINTER(ct.c_double)]
    nl5_lib.NL5_GetSimulationTime.restype = ct.c_int
    return nl5_lib.NL5_GetSimulationTime(ncir, t)


def NL5_Start(ncir):
    nl5_lib.NL5_Start.argtypes = [ct.c_int]
    nl5_lib.NL5_Start.restype = ct.c_int
    return nl5_lib.NL5_Start(ncir)


def NL5_Simulate(ncir, interval):
    nl5_lib.NL5_Simulate.argtypes = [ct.c_int, ct.c_double]
    nl5_lib.NL5_Simulate.restype = ct.c_int
    return nl5_lib.NL5_Simulate(ncir, interval)


def NL5_SimulateInterval(ncir, interval):
    nl5_lib.NL5_SimulateInterval.argtypes = [ct.c_int, ct.c_double]
    nl5_lib.NL5_SimulateInterval.restype = ct.c_int
    return nl5_lib.NL5_SimulateInterval(ncir, interval)


def NL5_SimulateStep(ncir):
    nl5_lib.NL5_SimulateStep.argtypes = [ct.c_int]
    nl5_lib.NL5_SimulateStep.restype = ct.c_int
    return nl5_lib.NL5_SimulateStep(ncir)


def NL5_SaveIC(ncir):
    nl5_lib.NL5_SaveIC.argtypes = [ct.c_int]
    nl5_lib.NL5_SaveIC.restype = ct.c_int
    return nl5_lib.NL5_SaveIC(ncir)


def NL5_GetDataSize(ncir, ntrace):
    nl5_lib.NL5_GetDataSize.argtypes = [ct.c_int, ct.c_int]
    nl5_lib.NL5_GetDataSize.restype = ct.c_int
    return nl5_lib.NL5_GetDataSize(ncir, ntrace)


def NL5_GetDataAt(ncir, ntrace, n, t, data):
    nl5_lib.NL5_GetDataAt.argtypes = [
        ct.c_int,
        ct.c_int,
        ct.c_int,
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
    ]
    nl5_lib.NL5_GetDataAt.restype = ct.c_int
    return nl5_lib.NL5_GetDataAt(ncir, ntrace, n, t, data)


def NL5_GetLastData(ncir, ntrace, t, data):
    nl5_lib.NL5_GetLastData.argtypes = [
        ct.c_int,
        ct.c_int,
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
    ]
    nl5_lib.NL5_GetLastData.restype = ct.c_int
    return nl5_lib.NL5_GetLastData(ncir, ntrace, t, data)


def NL5_GetData(ncir, ntrace, t, data):
    nl5_lib.NL5_GetData.argtypes = [
        ct.c_int,
        ct.c_int,
        ct.c_double,
        ct.POINTER(ct.c_double),
    ]
    nl5_lib.NL5_GetData.restype = ct.c_int
    return nl5_lib.NL5_GetData(ncir, ntrace, t, data)


def NL5_DeleteOldData(ncir):
    nl5_lib.NL5_DeleteOldData.argtypes = [ct.c_int]
    nl5_lib.NL5_DeleteOldData.restype = ct.c_int
    return nl5_lib.NL5_DeleteOldData(ncir)


def NL5_SaveData(ncir, name):
    nl5_lib.NL5_SaveData.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_SaveData.restype = ct.c_int
    return nl5_lib.NL5_SaveData(ncir, name)


def NL5_AddData(ncir, ntrace, t, data):
    nl5_lib.NL5_AddData.argtypes = [ct.c_int, ct.c_int, ct.c_double, ct.c_double]
    nl5_lib.NL5_AddData.restype = ct.c_int
    return nl5_lib.NL5_AddData(ncir, ntrace, t, data)


def NL5_DeleteData(ncir, name):
    nl5_lib.NL5_DeleteData.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_DeleteData.restype = ct.c_int
    return nl5_lib.NL5_DeleteData(ncir, name)


def NL5_GetInput(ncir, name):
    nl5_lib.NL5_GetInput.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_GetInput.restype = ct.c_int
    return nl5_lib.NL5_GetInput(ncir, name)


def NL5_SetInputValue(ncir, nin, v):
    nl5_lib.NL5_SetInputValue.argtypes = [ct.c_int, ct.c_int, ct.c_double]
    nl5_lib.NL5_SetInputValue.restype = ct.c_int
    return nl5_lib.NL5_SetInputValue(ncir, nin, v)


def NL5_SetInputLogicalValue(ncir, nin, i):
    nl5_lib.NL5_SetInputLogicalValue.argtypes = [ct.c_int, ct.c_int, ct.c_int]
    nl5_lib.NL5_SetInputLogicalValue.restype = ct.c_int
    return nl5_lib.NL5_SetInputLogicalValue(ncir, nin, i)


def NL5_GetOutput(ncir, name):
    nl5_lib.NL5_GetOutput.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_GetOutput.restype = ct.c_int
    return nl5_lib.NL5_GetOutput(ncir, name)


def NL5_GetOutputValue(ncir, nout, v):
    nl5_lib.NL5_GetOutputValue.argtypes = [ct.c_int, ct.c_int, ct.POINTER(ct.c_double)]
    nl5_lib.NL5_GetOutputValue.restype = ct.c_int
    return nl5_lib.NL5_GetOutputValue(ncir, nout, v)


def NL5_GetOutputLogicalValue(ncir, nout, i):
    nl5_lib.NL5_GetOutputLogicalValue.argtypes = [
        ct.c_int,
        ct.c_int,
        ct.POINTER(ct.c_int),
    ]
    nl5_lib.NL5_GetOutputLogicalValue.restype = ct.c_int
    return nl5_lib.NL5_GetOutputLogicalValue(ncir, nout, i)


def NL5_SetAC(ncir, ffrom, fto, points, scale):
    nl5_lib.NL5_SetAC.argtypes = [
        ct.c_int,
        ct.c_double,
        ct.c_double,
        ct.c_int,
        ct.c_int,
    ]
    nl5_lib.NL5_SetAC.restype = ct.c_int
    return nl5_lib.NL5_SetAC(ncir, ffrom, fto, points, scale)


def NL5_SetACSource(ncir, name):
    nl5_lib.NL5_SetACSource.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_SetACSource.restype = ct.c_int
    return nl5_lib.NL5_SetACSource(ncir, name)


def NL5_AddVACTrace(ncir, name):
    nl5_lib.NL5_AddVACTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddVACTrace.restype = ct.c_int
    return nl5_lib.NL5_AddVACTrace(ncir, name)


def NL5_AddIACTrace(ncir, name):
    nl5_lib.NL5_AddIACTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddIACTrace.restype = ct.c_int
    return nl5_lib.NL5_AddIACTrace(ncir, name)


def NL5_AddFuncACTrace(ncir, name):
    nl5_lib.NL5_AddFuncACTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_AddFuncACTrace.restype = ct.c_int
    return nl5_lib.NL5_AddFuncACTrace(ncir, name)


def NL5_AddZACTrace(ncir):
    nl5_lib.NL5_AddZACTrace.argtypes = [ct.c_int]
    nl5_lib.NL5_AddZACTrace.restype = ct.c_int
    return nl5_lib.NL5_AddZACTrace(ncir)


def NL5_AddGammaACTrace(ncir):
    nl5_lib.NL5_AddGammaACTrace.argtypes = [ct.c_int]
    nl5_lib.AddGammaACTrace.restype = ct.c_int
    return nl5_lib.NL5_AddGammaACTrace(ncir)


def NL5_AddVSWRACTrace(ncir):
    nl5_lib.NL5_AddVSWRACTrace.argtypes = [ct.c_int]
    nl5_lib.NL5_AddVSWRACTrace.restype = ct.c_int
    return nl5_lib.NL5_AddVSWRACTrace(ncir)


def NL5_AddLoopACTrace(ncir):
    nl5_lib.NL5_AddLoopACTrace.argtypes = [ct.c_int]
    nl5_lib.NL5_AddLoopACTrace.restype = ct.c_int
    return nl5_lib.NL5_AddLoopACTrace(ncir)


def NL5_CalcAC(ncir):
    nl5_lib.NL5_CalcAC.argtypes = [ct.c_int]
    nl5_lib.NL5_CalcAC.restype = ct.c_int
    return nl5_lib.NL5_CalcAC(ncir)


def NL5_GetACTrace(ncir, name):
    nl5_lib.NL5_GetACTrace.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_GetACTrace.restype = ct.c_int
    return nl5_lib.NL5_GetACTrace(ncir, name)


def NL5_GetACDataSize(ncir, ntrace):
    nl5_lib.NL5_GetACDataSize.argtypes = [ct.c_int, ct.c_int]
    nl5_lib.NL5_GetACDataSize.restype = ct.c_int
    return nl5_lib.NL5_GetACDataSize(ncir, ntrace)


def NL5_GetACDataAt(ncir, ntrace, n, f, mag, phase):
    nl5_lib.NL5_GetACDataAt.argtypes = [
        ct.c_int,
        ct.c_int,
        ct.c_int,
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
    ]
    nl5_lib.NL5_GetACDataAt.restype = ct.c_int
    return nl5_lib.NL5_GetACDataAt(ncir, ntrace, n, f, mag, phase)


def NL5_SaveACData(ncir, name):
    nl5_lib.NL5_SaveACData.argtypes = [ct.c_int, ct.c_char_p]
    nl5_lib.NL5_SaveACData.restype = ct.c_int
    return nl5_lib.NL5_SaveACData(ncir, name)
