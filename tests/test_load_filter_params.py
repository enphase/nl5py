import pytest
from nl5py import Schematic
import os
import numpy as np

schematic_file = os.path.join(os.path.dirname(__file__), "filter_tests.nl5")
schematic = Schematic(schematic_file)

def test_load_filter_params_analog():
    # Example: 2nd order analog filter
    b = [1.0, 0.0, 0.0]
    a = [1.0, 1.0e3, 1.0e6]
    schematic.load_filter_params("F1", b, a, analog=True)
    # Check that values are set (reverse order for analog)
    assert schematic.get_value("F1.b0") == pytest.approx(0.0)
    assert schematic.get_value("F1.b1") == pytest.approx(0.0)
    assert schematic.get_value("F1.b2") == pytest.approx(1.0)
    assert schematic.get_value("F1.a0") == pytest.approx(1.0e6)
    assert schematic.get_value("F1.a1") == pytest.approx(1.0e3)
    assert schematic.get_value("F1.a2") == pytest.approx(1.0)

def test_load_filter_params_digital():
    # Example: 3rd order digital filter
    b = [0.1, 0.2, 0.3, 0.4]
    a = [1.0, -0.5, 0.25, -0.125]
    schematic.load_filter_params("F2", b, a, analog=False)
    # Check that values are set (normal order for digital)
    assert schematic.get_value("F2.b0") == pytest.approx(0.1)
    assert schematic.get_value("F2.b1") == pytest.approx(0.2)
    assert schematic.get_value("F2.b2") == pytest.approx(0.3)
    assert schematic.get_value("F2.b3") == pytest.approx(0.4)
    assert schematic.get_value("F2.a0") == pytest.approx(1.0)
    assert schematic.get_value("F2.a1") == pytest.approx(-0.5)
    assert schematic.get_value("F2.a2") == pytest.approx(0.25)
    assert schematic.get_value("F2.a3") == pytest.approx(-0.125)

def test_load_filter_params_zero_pad():
    # b shorter than a, should be zero-padded
    b = [1.0, 0.0]
    a = [1.0, 2.0, 3.0]
    schematic.load_filter_params("F3", b, a, analog=False)
    assert schematic.get_value("F3.b0") == pytest.approx(1.0)
    assert schematic.get_value("F3.b1") == pytest.approx(0.0)
    assert schematic.get_value("F3.b2") == pytest.approx(0.0)
    assert schematic.get_value("F3.a0") == pytest.approx(1.0)
    assert schematic.get_value("F3.a1") == pytest.approx(2.0)
    assert schematic.get_value("F3.a2") == pytest.approx(3.0)

def test_load_filter_params_invalid_length():
    # a and b must have length between 1 and 6
    b = []
    a = []
    with pytest.raises(ValueError):
        schematic.load_filter_params("F4", b, a, analog=True)