import pygame
from screen_settings import Screen


class Ship:
    def __init__(self):
        pygame.init()
        self.image = pygame.image.load("alien/statek.png")
        self.image2 = pygame.image.load("alien/left.png")
        self.image3 = pygame.image.load("alien/right.png")

        self.width = 80
        self.height = 80

        self.screen = Screen()

        self.scale_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.scale_image2 = pygame.transform.scale(self.image2, (self.width, self.height))
        self.scale_image3 = pygame.transform.scale(self.image3, (self.width, self.height))

        self.x = 850
        self.y = 800
        self.speed = 4

        self.turn_left = False
        self.turn_right = False
        self.standart = True

        self.alive = True


    def move_left(self):
        if self.x >= 0:
            self.x -= self.speed
            self.x = self.x

    def move_right(self):
        if self.x <= self.screen.width - self.width:
            self.x += self.speed
            self.x = self.x

    def move_up(self):
        if self.y >= 0:
            self.y -= self.speed
            self.y = self.y

    def move_down(self):
        if self.y <= self.screen.height - self.height:
            self.y += self.speed
            self.y = self.y


    def normal(self, screen):
        screen.blit(self.scale_image, (self.x, self.y))

    def left(self, screen):
        screen.blit(self.scale_image2, (self.x, self.y))

    def right(self, screen):
        screen.blit(self.scale_image3, (self.x, self.y))

    



       
