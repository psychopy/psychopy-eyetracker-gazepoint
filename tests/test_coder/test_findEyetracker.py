from psychopy import plugins
from psychopy.iohub.devices import import_device
from psychopy.iohub import util



class BaseTestFindEyetracker:
    """
    Base class with methods for finding eyetracker. These will use `self.modulePath` to get the 
    module path, meaning subclasses can use different module paths
    """
    

    def test_importDevice(self):
        """
        Check that the EyeTracker device can be found by ioHub's import function
        """
        # import device class via ioHub
        import_device(
            self.modulePath + ".eyetracker", 
            "EyeTracker"
        )


    def test_getDeviceConfig(self):
        # get device config
        util.getDeviceDefaultConfig(self.modulePath)



class TestFindEyetrackerAbs(BaseTestFindEyetracker):
    """
    Test finding eyetracker using the absolute module path
    """
    modulePath = "psychopy_eyetracker_gazepoint.gazepoint.gp3"


class TestFindEyetrackerEP(BaseTestFindEyetracker):
    """
    Test finding eyetracker using the plugin entry point target
    """
    modulePath = "psychopy.iohub.devices.eyetracker.gp3"

    def setup_method():
        # make sure plugins are activated
        plugins.activatePlugins()
