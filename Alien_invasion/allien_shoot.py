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
        self.scale_laser = pygame.transform.scale(self.laser, (self.width, self.height))
        self.window = Screen()
        
        self.lahsers = []

        self.las = {
            "image":self.scale_laser,
            "x":random.randint(1000, 1800),
            "y":random.randint(0, 100),
            "in_game":True,
            "speed":6
        }

        for _ in self.alien.alien_army:
            self.lahsers.append(self.las)

    

    def laser_move(self):
        if self.las["y"] <= self.window.height + self.height:
            self.las["y"] +=  self.las["speed"]
            self.las["y"] = self.las["y"]
        else:
            self.__init__()

    




        
