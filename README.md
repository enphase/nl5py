# `nl5py`

Python library for interfacing to the [NL5](https://sidelinesoft.com/nl5/) DLL based circuit simulator

`nl5py` is a Python interface for modifying, simulating, and extracting data from NL5 schematics using the [NL5](https://sidelinesoft.com/nl5/) DLL circuit simulator.  There are plans in the future to also support the HTTP API for interfacing to open schmatics in the regular [NL5](https://sidelinesoft.com/nl5/) program.

## Loading NL5 License
NL5 DLL can be used without a license, but will be limited to 20 components for tansient simulations.  If your schematic has more than 20 components and no license is detected, the following exception will be raised when you attempt to run a transient simulation.

```
Exception: NL5_Simulate: Too many components for Demo version
```

There are two ways to include a license file.  Either simple place an nl5.nll file in the same directory as the schematic file you are loading/simulating, or use the `load_license()` function.

```python
from nl5py import load_license
license_info = load_license("nl5.nll")
```

## Loading a Schematic
The `Schematic` class is the primary interface class.  You initialize the class with a path to an existing NL5 schematic file, which will load this into the NL5 DLL.

```python
from nl5py import Schematic
schematic = Schematic("analog.nl5")
```

## Modifying Circuit Parameters
You can modify the properties of circuit elements using the `set_value` method.

```python
schematic.set_value("C1", 2.1)  # change C1 to 2.1 Farads
schematic.set_value("C1.IC", 5.2) # Set the initial voltage of C1 to 5.2V
```

The library will verify that commands are recieved by the NL5 DLL without errors.  If an error is detected, it gets converted into an `Exception` and raised.

```python
schematic.set_value("C100", 2.1)  # C100 does not exist
```

Since `C100` does not exist in the schematic, it will throw the following exception:

```
Exception: NL5_SetValue: parameter C100 not found
```
### Modifying Subcircuits

If you want to modify elements in a subcircuit, you must do so using the `set_text` method and send all of the value changes as a string of comma deliminted commands.

```python
# Change C1 and C2 in the subcircuit inside X1
commands = ["C1 = 1", "C2 = 2"]
schematic.set_text("X1.Cmd", ",".join(commands))
```

If you want to set a value that needs to be comma deliminited, such as a PWL value, the PWL section should be in quotes.

```python
# C1 is a PWL capacitor
commands = ['C1.PWL = "1, 1, 2"', "C2 = 2"]
schematic.set_text("X1.Cmd", ",".join(commands))
```

## Transient Simulations

Before a transient simulation is run, the user must ensure that the circuit includes all the traces (voltages, currents, powers, etc) that they want to observe.  Traces can be added programmatically using the `add_trace` method.

```python
schematic.add_trace(name="C1", trace_type="V")  # add the voltage on C1
schematic.add_trace(name="C1", trace_type="I")  # add the current on C1
```

All of the NL5 trace types are supported via the following "trace_type" strings:

| trace_type | Description |
| ---------- | ----------- |
| "V"        | Voltage     |
| "I"        | Current     |
| "P"        | Power       |
| "Var"      | Variable    |
| "Func"     | Function    |
| "Data"     | Data        |

If no trace type is specified, it defaults to "Function".

```python
schematic.add_trace(name="V(C2)")  		 # add the voltage on C1 via a function trace
schematic.add_trace(name="V(C1)+V(C2)")  # add the sum of voltages on C1 and C2 via a function trace
```

Running a transient simulation is done using the `simulate_transient` method.

```python
schematic.simulate_transient(screen=20, step=1e-3)
```

After a simulation has completed, data can be extracted using get_data.

```python
data = schematic.get_data(traces=["V(1)", "V(2)", "V(3)", "V(4)", "V(5)"])
```

The data is returned in the form of a [pandas](https://pandas.pydata.org/) [dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).

```python
print(data.head())
```
```
              V(1)      V(2)      V(3)      V(4)      V(5)
0.000000  0.000000  0.000000  0.000000  0.000000  0.000000
0.000250  0.015708  0.005236  0.005236  0.005236  0.005236
0.000500  0.031416  0.010472  0.010472  0.010472  0.010472
0.000667  0.041888  0.013963  0.013963  0.013963  0.013963
0.000833  0.052360  0.017453  0.017453  0.017453  0.017453
```

## AC Simulations

The `Schematic` class also supports AC simulations, which work in much the same way as the transient simulations.

```python
# set the AC source
schematic.set_ac_source("I1")

# add AC traces
# TODO: Does not yet appear to be supported by DLL API

# run simulation
schematic.simulate_ac(start_frequency=1e3, stop_frequency=1e6, num_points=5000)

# extract data
data = schematic.get_ac_data(traces=["V(1)", "V(2)"])
```

The data returned from `get_ac_data` is a hierarchical index'd data frame with magnitude and phase info for each signal.

```python
print(data.head())
```

```
            V(1)                       V(2)                               
            magnitude       phase      magnitude       phase
1000.000000  0.009758  179.121846       0.009758  179.121846
1199.839968  0.014131  178.946299       0.014131  178.946299
1399.679936  0.019365  178.770721       0.019365  178.770721
1599.519904  0.025496  178.595105       0.025496  178.595105
1799.359872  0.032566  178.419447       0.032566  178.419447
```