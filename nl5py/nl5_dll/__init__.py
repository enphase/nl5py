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

import platform
from importlib_resources import files
import ctypes as ct

# load the library
def get_library(operating_system):
    if "Windows" in operating_system:
        return ct.cdll.LoadLibrary(
            str(files(f"nl5py.nl5_dll.Windows").joinpath("nl5_dll.dll"))
        )
    elif "Linux" in operating_system:
        if "WSL2" in operating_system:
            return ct.cdll.LoadLibrary(
                str(files(f"nl5py.nl5_dll.Linux.Ubuntu").joinpath("nl5_dll.dll"))
            )
        elif "Ubuntu" in operating_system:
            return ct.cdll.LoadLibrary(
                str(files(f"nl5py.nl5_dll.Linux.Ubuntu").joinpath("nl5_dll.dll"))
            )
        elif "Red Hat" in operating_system:
            return ct.cdll.LoadLibrary(
                str(files(f"nl5py.nl5_dll.Linux.RHEL").joinpath("nl5_dll.dll"))
            )
    elif "Darwin" in operating_system:
        if "arm" in operating_system:
            return ct.cdll.LoadLibrary(
                str(files(f"nl5py.nl5_dll.macOS.arm64").joinpath("nl5_dll.dll"))
            )
        else:
            return ct.cdll.LoadLibrary(
                str(files(f"nl5py.nl5_dll.macOS.x64").joinpath("nl5_dll.dll"))
            )

    raise Exception(f"{operating_system} not supported")


nl5_lib = get_library(platform.platform())
