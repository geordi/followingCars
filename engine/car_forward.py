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
    @property
    def speed(self):
        return self._speed

    def __str__(self):
        return "Type: {}, Position: {}, Speed: {}".format(self.name, self.position, self.speed)
    
    def move(self, step_time, cars):
        self.position = self.position + np.array([step_time * self.speed, 0])
        super().move(step_time, cars)