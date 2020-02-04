import numpy as np

class Sensor:

    def __init__(self, position):
        self.position = position
        
    @property
    def name(self):
        return 'Sensor'

    def sense(self, cars):
        pass
