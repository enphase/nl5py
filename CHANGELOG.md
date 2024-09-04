# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Fixed
### Changes
### Added

## v0.1.5

### Fixed
-Add .so files to package data to Linux/macOS DLL libraries are included in package data
### Changes
### Added


## v0.1.4

### Fixed
-Now supports older versions of Python tested down to 3.8 ([issue-2](https://github.com/enphase/nl5py/issues/2))
-Now supports Windows, Linux, and macOS
### Changes
### Added
-Add pytest tests
-Add tox tests
-Add new AC functions NL5_AddVACTrace, NL5_AddIACTrace, NL5_AddFuncACTrace, NL5_AddZACTrace, NL5_AddGammaACTrace, NL5_AddVSWRACTrace, and NL5_AddLoopACTrace
-Add new methods to Schematic() class to support the new AC trace add functions

## v0.1.3

### Fixed
-Added "sort=True" to data concatenations so we have sorted time series data.
### Changes
-Updated NL5 DLLs to 3.14.65.26 which have 14 new API functions
### Added
-Add the NL5_GetTracesSize, NL5_GetTraceAt, and NL5_GetTraceName API commands
-Add "get_trace_names" to get a list of existing trace names that have been added
-Add "clear_traces" for deleting all existing traces
-Add default traces for "get_data" which grabs data from all traces

## v0.1.2

### Fixed
-Updated min Python version to 3.12. There appears to be an issue the DLL import with previous versions.
### Changes
### Added
-Add a delete_trace() method.

## v0.1.1

### Fixed
### Changes
### Added
-Add a "continue_transient" feature, which allows user to continue a transient from where last one left off.
-Added a changelog
-Chage setup.py file so NL5 DLL is included in the package date

## v0.1.0

### Fixed
### Changes
### Added
- Initial release