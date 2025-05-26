import pygame
from screen_settings import Screen
from board import GameBoard
from rectangle import Rectangle
from colours import Colours

class Main:
    def __init__(self):
        # screen
        pygame.init()

        self.screen = Screen()
        self.window = pygame.display.set_mode((self.screen.width, self.screen.height))
        pygame.display.set_caption("Maze")


        # Game board
        self.board = GameBoard()

        # Rctangle
        self.r = Rectangle()

        # Colours
        self.colour = Colours()

        # FPS per secont
        self.clock = pygame.time.Clock()



    def start_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                

            self.window.blit(self.board.board, (self.board.board_x, self.board.board_y))
        

            pygame.draw.rect(self.window, self.colour.red, self.r.rect)
          

            
            key = pygame.key.get_pressed()

            if key[pygame.K_LEFT]:
                self.r.move_left()

            if key[pygame.K_RIGHT]:
                self.r.move_right()

            if key[pygame.K_UP]:
                self.r.move_up()

            if key[pygame.K_DOWN]:
                self.r.move_down()


            for i in self.board.a:
                if self.r.rect.colliderect(i):
                    self.r.collision()

            pygame.display.update()
            self.clock.tick(60)
            

start = Main()
start.start_game()



            