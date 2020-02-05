
import pygame
import pygame.font
from pygame.time import Clock
from pygame.locals import *
import sys
from engine import Car, Engine
import numpy as np
from . import Sprite

meter2pixel = 20.0
pixel2meter = 1/meter2pixel

    

class Visualization:
    def __init__(self, engine):
        self.running = True
        self.display_surf = None
        self.size = self.width, self.height = 800, 600
        self.center = self.width/2, self.height/2
        self.clock = Clock()
        self.font = None
        self.engine = engine
        self.engine.on_simulation_step = self.build_scene
        self.scene = []
        self.target_fps = 60.0
        self.focused_car = 0
 
    
    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
        self.font = pygame.font.Font(pygame.font.get_default_font(), 12)

        self.sprites = [
           Sprite("images/blue-small.png"), 
           Sprite("images/orange-small.png"), 
        ] 
        self.engine.restart()
        

    def build_scene(self, engine):
        self.scene = []

        # if there are no cars break
        if not self.engine.cars or len(self.engine.cars)==0:
            self.scene.append((self.center, self.sprites[0]))
            return

        if self.focused_car>=len(self.engine.cars):
            self.focused_car = 0

        center = self.engine.cars[self.focused_car].position
        # self.scene.append((self.center, self.sprites[self.focused_car]))
        for idx, car in enumerate(self.engine.cars):
            car_pos = self.center - (center-car.position) * meter2pixel
            # car_pos *= meter2pixel
            self.scene.append((car_pos, self.sprites[idx % len(self.sprites)]))
        

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False   
        if event.type == pygame.KEYDOWN:  
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                self.running = False
            if pressed[pygame.K_r]:
                self.engine.run(delay=1/self.target_fps)
            if pressed[pygame.K_x]:
                self.engine.restart()
            if pressed[pygame.K_b]:
                self.engine.interrupt()
            if pressed[pygame.K_TAB]:
                self.move_focus()
        
    def move_focus(self):
        self.focused_car  += 1
        self.build_scene(self.engine)

    def on_loop(self):
        pass


    def on_render(self):
        self.display_surf.fill(pygame.Color(255,255,255))
        for pos, sprite in self.scene:
            relpos = pos + sprite.offset
            self.display_surf.blit(sprite.image, relpos)
        
        # FPS writing
        fps_surface = self.font.render("{:.0f} FPS".format(self.clock.get_fps()), True, (255,255,255))
        self.display_surf.blit(fps_surface, (self.display_surf.get_width()-fps_surface.get_width(),0))

        pygame.display.flip()
        self.clock.tick(self.target_fps)


    def on_cleanup(self):
        pygame.quit()
 

    def on_execute(self):
        if self.on_init() == False:
            self.running = False
 
        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 