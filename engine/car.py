import numpy as np
from  pygame.math import Vector2
import math 

# Inspiration here http://rmgi.blog/pygame-2d-car-tutorial.html

class Car:
    def __init__(self, position, size, velocity=(0.0,0.0), angle=0.0, max_steering = 30, max_acceleration = 5, steering=0.0):
        """Init a abstract class for a Car in an simulation engine
        
        Arguments:
            position {2d array} -- 2D position in real world coordinates
            size {2D array} -- size in meters of a car
            velocity {2d array} -- velocity of the car
            angle {float} -- angle of the car
            max_steering {float} -- maximum steering in degrees
            max_acceleration {float} -- maximum acceleration in meters per second squared 
        """
        self._position = Vector2(position)  
        self._size = Vector2(size)
        self._velocity = Vector2(velocity, 0)
        self._angle = angle
        self._max_steering = max_steering
        self._max_acceleration = max_acceleration
        self._acceleration = 0.0
        self._steering = steering
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
        self._velocity += (self._acceleration * step_time, 0)
        if self._steering:
            turning_radius = self._size.y / math.sin(math.radians(self._steering))
            angular_velocity = self._velocity.x / turning_radius
        else:
            angular_velocity = 0
        
        self._position += self._velocity.rotate(-self._angle) * step_time
        self._angle += math.degrees(angular_velocity) * step_time
        # for idx, sensor in enumerate(self._sensors):
        #     sensor.sense(step_time, cars)
        # pass

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

    
