import pygame
from aliens import Aliens
import random
from screen_settings import Screen


class Upgrade:
    def __init__(self):
        pygame.init()
     
        self.image = pygame.image.load("alien/rapidfire.png")
        self.alien = Aliens()
        self.screen = Screen()
        self.alien.spawn_first_wave()
        self.width = 50
        self.height = 50
     
        self.upgrade_speed = 2
        self.scale_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.random_upg = random.choices(self.alien.alien_army, k = 2)

        self.move = {
            "left":True,
            "right":False
        }


    def show_upgrade(self, window):
        for upgrade in self.random_upg:
            window.blit(self.scale_image, (upgrade["x"], upgrade["y"]))

        # for upgrade in self.random_upg:
        #     if upgrade["y"] <= self.screen.height + self.height:
        #         upgrade["y"] += self.upgrade_speed
        #         upgrade["y"] = upgrade["y"]

        #     else:
        #         self.random_upg = random.choices(self.alien.alien_army, k = 2)
                
                

    

            
        

        