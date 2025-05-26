import pygame

from board import GameBoard

class Rectangle:
    def __init__(self):
        self.rect_x = 50
        self.rect_y = 500
        self.rect_width = 20
        self.rect_height = 20
        self.rect_speed = 1
        self.rect = pygame.Rect(self.rect_x, self.rect_y, self.rect_width, self.rect_height)

        self.board = GameBoard()

    def move_left(self):
        self.rect_x -= self.rect_speed
        self.rect.x = self.rect_x

    def move_right(self):
        self.rect_x += self.rect_speed
        self.rect.x = self.rect_x

    def move_up(self):
        self.rect_y -= self.rect_speed
        self.rect.y = self.rect_y

    def move_down(self):
        self.rect_y += self.rect_speed
        self.rect.y = self.rect_y
        

    def collision(self):
        self.__init__()
            

       

