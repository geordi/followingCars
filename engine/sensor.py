import numpy as np

class Sensor:

    def __init__(self, owner, offset = np.array([0,0])):
        """Initialization of the common property of each sensor
        
        Arguments:
            owner {object} -- Owner of the sensor that should not be affected by the sense method
            offset {point2D} -- Offset of the sensor relative to the owner
        """
        self._owner = owner
        self._offset = offset
        
    @property
    def name(self):
        return 'Sensor'

    def sense(self, step_time, cars):
        """Sense the neighborhood and get the data from the scene around the sensor
        
        Arguments:
            step_time {float} -- time elapsed from previous call or simulation step
            cars {array[Car]} -- list of cars from the scene
        """
        pass

    @property
    def position(self):
        return self._owner.center + self._offset
