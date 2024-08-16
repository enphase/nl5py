# `nl5py`

Python library for interfacing to the NL5 DLL based circuit simulator

`nl5py` is a Python interface for modifying, simulating, and extracting data from NL5 schematics using the NL5 DLL circuit simulator.  There are plans in the future to also support the HTTP API for interfacing to open schmatics in the regular NL5 program.

# Use

The `Schematic` class is the primary interface class.  You initialize the class with a path to an existing NL5 schematic file, which will load this into the NL5 DLL.

```python
from nl5py import Schematic
schematic = Schematic(f"{nl5_dir}/Examples/Transient/analog.nl5")
```

You can modify the properties of circuit elements using the `set_value` method.

```python
schematic.set_value("C1", 2.1)  # change C1 to 2.1 Farads
schematic.set_value("C1.IC", 5.2) # Set the initial voltage of C1 to 5.2V
```

The library will verify that commands are recieved by the NL5 DLL without errors.  If an error is detected, it gets converted into an `Exception` and raised.

```python
schematic.set_value("C100", 2.1)  # C100 does not exist
```

```
Exception: NL5_SetValue: parameter C100 not found
```