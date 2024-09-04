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

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nl5py",
    version="0.1.3",
    author="Donny Zimmanck",
    author_email="dzimmanck@enphaseenergy.com",
    description="Python library for interfacing to the NL5 DLL based circuit simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enphase/nl5py",
    packages=setuptools.find_packages(),
    package_data={
        # Make sure the NL5 DLL is included in the package
        "": ["*.dll", "*.h", "*.lib"],
    },
    install_requires=["numpy", "pandas", "importlib-resources"],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
    ],
)
