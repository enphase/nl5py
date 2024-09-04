import pytest
from nl5py import Schematic

import pytest
import os

schematic_file = os.path.join(os.path.dirname(__file__), "rc.nl5")
schematic = Schematic(schematic_file)


def test_set_get_value():
    schematic.set_value("C1", 1e-9)
    schematic.set_value("R1", 1e-3)

    assert schematic.get_value("C1") == 1e-9
    assert schematic.get_value("R1") == 1e-3

    with pytest.raises(Exception):
        schematic.set_value("C2", 1e-9)

    with pytest.raises(Exception):
        schematic.get_value("C2")
