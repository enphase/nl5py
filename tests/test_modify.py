import pytest
from nl5py import Schematic

import pytest
import os

def test_modify():
    schematic_file = os.path.join(os.path.dirname(__file__), "rc.nl5")
    schematic = Schematic(schematic_file)