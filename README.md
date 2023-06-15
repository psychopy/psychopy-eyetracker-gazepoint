# psychopy-eyetracker-gazepoint

Extension for PsychoPy which adds support for [Gazepoint](https://www.gazept.com/) 
eyetrackers (via ioHub)

## Supported Devices

Installing this package alongside PsychoPy will enable support for the following 
devices:

* Supported Gazepoint eye trackers
    
## Installing

Install this package with the following shell command:: 

    pip install psychopy-eyetracker-gazepoint

You may also use PsychoPy's builtin plugin/package manager to install this 
package.

## Usage

Once the package is installed, PsychoPy will automatically load it when started 
and the `psychopy.iohub.devices.eyetracker.hw.gazepoint` namespace will contain 
the loaded objects.