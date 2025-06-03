import random
import pygame
from aliens import Aliens
from screen_settings import Screen

class Laser:
    def __init__(self):
        pygame.init()
        self.alien = Aliens()

        self.alien.spawn_first_wave()
     
        self.laser = pygame.image.load("alien/lahser.png")
        self.width = 5
        self.height = 150
        self.x = random.randint(1000, 1800)
        self.y = random.randint(0, 100)
        self.scale_laser = pygame.transform.scale(self.laser, (self.width, self.height))
        self.window = Screen()
        
        self.lahsers = []

        self.las1 = {
            "image":self.scale_laser,
            "x":self.x,
            "y":self.y,
            "in_game":True,
            "speed":6
        }

        for _ in self.alien.alien_army:
            self.lahsers.append(self.las1)

    
    def laser_move(self):
        if self.las1["y"] <= self.window.height + self.height:
            self.las1["y"] +=  self.las1["speed"]
            self.las1["y"] = self.las1["y"]
        else:
            self.las1["x"] = random.randint(1000, 1800)
            self.las1["y"] = random.randint(0, 100)

    




        
