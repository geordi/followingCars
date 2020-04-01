
import pygame
import pygame.font
from pygame.time import Clock
from pygame.locals import *
import sys
from engine import Car, Engine
import numpy as np
from . import Sprite
from engine import LidarSensor

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
        self.metadata = []

 
    
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
        self.metadata = []

        # if there are no cars break
        if not self.engine.cars or len(self.engine.cars)==0:
            self.scene.append((self.center, 0, self.sprites[0]))
            return

        if self.focused_car>=len(self.engine.cars):
            self.focused_car = 0

        center = self.engine.cars[self.focused_car].position
        
        for idx, car in enumerate(self.engine.cars):
            car_pos = self.center - (center-car.position) * meter2pixel
            
            self.scene.append((car_pos, car._angle, self.sprites[idx % len(self.sprites)]))
            self.metadata.append(((int(car_pos.x), int(car_pos.y)), 0))
            
            # for v in car.vertices():
            #     relpos = self.center - (center-v) * meter2pixel
            #     self.metadata.append((relpos.astype(np.int), 1))
            if car==self.engine.cars[self.focused_car]:
                for s in car._sensors:
                    if isinstance(s, LidarSensor):
                        for v in s._intersections:
                            if v is not None:
                                relpos = self.center - (center-v) * meter2pixel
                                self.metadata.append((relpos.astype(np.int), 1))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False   
        if event.type == pygame.KEYDOWN:  
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                self.running = False
            if pressed[pygame.K_SPACE]:
                if self.engine.is_running:
                    self.engine.interrupt()
                else:
                    self.engine.run()
            if pressed[pygame.K_x]:
                self.engine.restart()
            
            if pressed[pygame.K_TAB]:
                self.move_focus()
        
    def move_focus(self):
        self.focused_car  += 1
        self.build_scene(self.engine)

    def on_loop(self):
        pass


    def on_render(self):
        self.display_surf.fill(pygame.Color(0,0,0))
        for pos, angle, sprite in self.scene:
            rotated = pygame.transform.rotate(sprite.image, angle)
            rect = rotated.get_rect()
            relpos = pos - (rect.width / 2, rect.height / 2)
            self.display_surf.blit(rotated, relpos)
        
        for pos, typ in self.metadata:
            if typ==0:
                pygame.draw.circle(self.display_surf, (255,0,0), pos, 3)
            if typ==1:
                pygame.draw.circle(self.display_surf, (0,255,0), pos, 3)
        
        # FPS writing
        fps_surface = self.font.render("{:.0f} FPS".format(self.clock.get_fps()), True, (255,255,255))
        self.display_surf.blit(fps_surface, (self.display_surf.get_width()-fps_surface.get_width(),0))

        # Simulation steps writing
        step_surface = self.font.render("{} steps".format(self.engine.step_count), True, (255,255,255))
        self.display_surf.blit(step_surface, (self.display_surf.get_width()-step_surface.get_width(),fps_surface.get_height()+5))

        # Simulation control keys
        lines = '''SPACE - start/stop simulation
        X - restart simulation
        TAB - move focus
        ESC - quit'''

        y = 5
        for line in lines.split('\n'):
            text = self.font.render(line.strip(), True, (255,255,255))
            self.display_surf.blit(text, ( 5, y))
            y += 5 + text.get_height()
            
            

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
 