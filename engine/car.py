import numpy as np


class Car:
    def __init__(self, position, size):
        """Init a abstract class for a Car in an simulation engine
        
        Arguments:
            position {2d array} -- 2D position in real world coordinates
            size {2D array} -- size in meters of a car
        """
        self._position = np.array(position)  
        self._create_model = None
        self._size = size     

    @property
    def name(self):
        return 'Car'

    def __str__(self):
        return "Type: {}, Position: {}, Size: {}".format(self.name, self.position, self.size)
        
    def move(self, time_passed):
        """Move a car based on the time passed from last move
        
        Arguments:
            time_passed {double} -- time passed from last movement in seconds
        """
        pass

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def size(self):
        return self._size