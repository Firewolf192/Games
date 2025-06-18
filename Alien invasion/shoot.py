import pygame
from ship import Ship
from aliens import Aliens

class Bullet:
    def __init__(self):
        pygame.init()
        self.image = pygame.image.load("alien/test.png")
        self.width = 50
        self.height = 200
        self.scale_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = None
        self.y = None

        self.bullet_in_game = True
        
        self.speed = 7
        self.ship = Ship()
        self.alien = Aliens()

        self.normal_active = False

        self.normal_fire = False
        self.rapid_active = True

        self.bullets = []

    def reset_postions(self):
        self.x = None
        self.y = None


    def move(self):
        if self.y + self.height >= 0:
            self.normal_fire = False
            self.y -= self.speed
            self.y = self.y

        else:
            self.normal_fire = True
            self.reset_postions()

    def reset(self):
        self.x = None
        self.y = None
        self.normal_active = False
        self.normal_fire = True
        self.bullet_in_game = True




