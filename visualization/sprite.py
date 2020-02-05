import pygame
import numpy as np

class Sprite:
    def __init__(self, src_image):
        self._image = pygame.image.load(src_image).convert_alpha()
        self._size = np.array(self.image.get_size())

    @property
    def image(self):
        return self._image

    @property
    def size(self):
        return self._size

    @property
    def offset(self):
        return -self.size/2
    