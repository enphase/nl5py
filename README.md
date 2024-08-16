# `nl5py`

Python library for interfacing to the NL5 DLL based circuit simulator

`nl5py` is a Python interface for modifying, simulating, and extracting data from NL5 schematics using the NL5 DLL circuit simulator.  There are plans in the future to also support the HTTP API for interfacing to open schmatics in the regular NL5 program.

# Use

The `Schematic` class is the primary interface class.  You initialize the class with a path to an existing NL5 schematic file, which will load this into the NL5 DLL.

```python
from nl5py import Schematic
schematic = Schematic(f"{nl5_dir}/Examples/Transient/analog.nl5")
```

## Basic modifications 
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
## Modifying subcircuits

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