from psychopy.localization import _translate
from psychopy.experiment import Param
from psychopy.experiment.components.settings.eyetracking import EyetrackerBackend


class GazePointEyetrackerBackend(EyetrackerBackend):
    """Experiment settings for the GazePoint GP3 eyetracker.
    """
    label = 'GazePoint GP3 (iohub)'
    key = 'eyetracker.hw.gazepoint.gp3.EyeTracker'

    needsFullscreen = False
    needsCalibration = False

    @classmethod
    def getParams(cls):
        # define order
        order = [
            # network settings
            "gpNetIP4Address",
            "gpNetPort",
            # runtime settings
            "gpSamplingRate",
            "gpTrackEyes"
        ]

        # network settings
        params = {}
        params['gpNetIP4Address'] = Param(
            "127.0.0.1",   # default value
            valType='str', 
            inputType="single",
            hint=_translate("IP Address to connect to."),
            label=_translate("IP4 Address"), 
            categ="Eyetracking"
        )
        params['gpNetPort'] = Param(
            "4242",  # default value
            valType='str', 
            inputType="single",
            hint=_translate("Port number to connect to."),
            label=_translate("Port"), 
            categ="Eyetracking"
        )

        # runtime settings
        params['gpSamplingRate'] = Param(
            "60", 
            valType='str', 
            inputType="single",
            hint=_translate("Sampling rate in Hz."),
            label=_translate("Sampling rate"), 
            categ="Eyetracking"
        )
        params['gpTrackEyes'] = Param(
            'BINOCULAR', 
            valType='str', 
            inputType="choice",
            allowedVals=['BINOCULAR'],
            hint=_translate("Which eye(s) to track."),
            label=_translate("Track eyes"), 
            categ="Eyetracking"
        )

        return params, order

    @classmethod
    def writeDeviceCode(cls, inits, buff):
        code = (
            "ioConfig[%(eyetracker)s] = {\n"
            "    'name': 'tracker',\n"
            "    'network_settings': {\n"
            "        'ip_address': %(gpNetIP4Address)s,\n"
            "        'port': %(gpNetPort)s,\n"
            "    },\n"
            "    'runtime_settings': {\n"
            "        'sampling_rate': %(gpSamplingRate)s,\n"
            "        'track_eyes': %(gpTrackEyes)s,\n"
            "    },\n"
            "}\n"
        )
        buff.writeIndentedLines(code % inits)
