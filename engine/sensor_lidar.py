import numpy as np
from . import Sensor
from .helper import intersect_line_car
import math

class LidarSensor(Sensor):
    """Ideal Lidar sensor in each sense call whole scene is checked, no delays"""

    def __init__(self, owner, offset, max_range, steps):
        """Initialization of the lidar
        
        Arguments:
            owner {object} -- Owner of the sensor that should not be affected by the sense method
            offset {point2D} -- Position relative to the car is hold it
            max_range {float} -- Maximum range in meters from the lidar
            steps {int} -- Steps for 360 degree lidar field of view
        """
        super().__init__(owner, offset)
        self._max_range = max_range
        self._steps = steps
        self._data = np.zeros([steps])

    @property
    def name(self):
        return 'Lidar, range={}, step={}'.format(self._max_range, self._step)

    def sense(self, step_time, cars):
        start = self.position
        angle_step = 360/self._steps
        angle = 0
        ray_idx = 0
        while angle<=360:
            rangle = angle * math.pi / 180
            end = start + self._max_range * np.array([math.cos(rangle), math.sin(rangle)])
            for idx, car in enumerate(cars):
                if car==self._owner:
                    continue
                distance = intersect_line_car(start, end, car) 
                if not distance:
                    self._data[ray_idx] = self._max_range
                else:
                    self._data[ray_idx] = distance
            angle += angle_step
            ray_idx += 1