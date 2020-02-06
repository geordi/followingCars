import numpy as np


class Car:
    def __init__(self, position, size):
        """Init a abstract class for a Car in an simulation engine
        
        Arguments:
            position {2d array} -- 2D position in real world coordinates
            size {2D array} -- size in meters of a car
        """
        self._position = np.array(position)  
        self._size = np.array(size)
        self._sensors = []   

    @property
    def name(self):
        return 'Car'

    def __str__(self):
        return "Type: {}, Position: {}, Size: {}".format(self.name, self.position, self.size)
        
    def move(self, step_time, cars):
        """Move a car based on the time passed from last move
        
        Arguments:
            step_time {double} -- time passed from last movement in seconds
            cars {array[Car]} -- list of other cars in a scene to be able to get info about the scene using sensors
        """
        for idx, sensor in enumerate(self._sensors):
            sensor.sense(step_time, cars)
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

    def vertices(self):
        left_top = self.position-self.size/2
        right_top = left_top + [self.size[0], 0]
        right_bottom = self.position + self.size/2
        left_bottom = right_bottom - [self.size[0], 0]
        
        return [left_top, right_top, right_bottom, left_bottom]


    def add_sensor(self, sensor):
        self._sensors.append(sensor)

    
