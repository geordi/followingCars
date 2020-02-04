import numpy as np
from . import Sensor

class LidarSensor(Sensor):

    # position of the sensor relative to the center of the car, maximum range of the laser sensor, set of the laser in degrees
    def __init__(self, position, max_range, step):
        super().__init__(position)
        self.range = max_range
        self.step = step

    @property
    def name(self):
        return 'Lidar, range={}, step={}'.format(self.max_range, self.step)

    def sense(self, cars):
        
        pass
