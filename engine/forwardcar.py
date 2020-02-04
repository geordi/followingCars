import numpy as np
from . import Car

class ForwardCar(Car):
    
    def __init__(self, position, size, speed):
        """[summary]
        
        Arguments:
            Car {[type]} -- [description]
            position {[type]} -- [description]
            size {[type]} -- [description]
            speed {float} -- Speed in meters per second
        """
        super().__init__(position, size)
        self._speed = speed

    @property
    def name(self):
        return 'Forward'

    def speed(self):
        return self._speed

    def __str__(self):
        return "Type: {}, Position: {}, Direction: {}".format(self.name, self.position, self.direction)
    
    def move(self, time_passed):
        self.position = self.position + np.array([time_passed * self.speed, 0])