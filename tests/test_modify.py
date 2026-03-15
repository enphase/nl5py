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


def test_enable_disable_component():
    # disable R1
    schematic.disable_component("R1")

    # simulate and verify we no longer get voltage on C1
    schematic.add_trace("C1", "V")
    schematic.simulate_transient(screen=1, step=1e-3)
    data = schematic.get_data()
    assert data["V(C1)"].iloc[-1] == 0.0

    # enable R1
    schematic.enable_component("R1")

    # re-simule and verify we get voltage
    schematic.simulate_transient(screen=1, step=1e-3)
    data = schematic.get_data()
    assert data["V(C1)"].iloc[-1] > 0.0

    # try to enable a non-existance component and verify we throw an exception
    with pytest.raises(Exception):
        schematic.enable_component("C2")

    # try to disable a non-existance component and verify we throw an exception
    with pytest.raises(Exception):
        schematic.disable_component("C2")
