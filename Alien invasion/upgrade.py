import pygame
from aliens import Aliens
import random

class Upgrade:
    def __init__(self):
        pygame.init()
     
        self.image = pygame.image.load("assets/alien/rapidfire.png")
        self.alien = Aliens()
        self.alien.spawn_first_wave(self.alien.x1, self.alien.y1, self.alien.speed1, self.alien.scale_image1)
        
        self.width = 50
        self.height = 50

        self.upgrade_speed = 2
        self.scale_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.random_upg = random.sample(self.alien.alien_army, k = 2)
  

    def show_upgrade(self, window):
        for upgrade in self.random_upg:
            window.blit(self.scale_image, (upgrade["x"], upgrade["y"]))

    # def upgrade_move(self):
    #     for upgrade in self.random_upg:
    #         if self.alien.move["right"]:
    #             upgrade["x"] += self.upgrade_speed



    

            
        

        