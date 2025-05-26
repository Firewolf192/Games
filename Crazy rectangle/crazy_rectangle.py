import pygame
import random

# base_dir = os.path.dirname(os.path.abspath(__file__))
# audio_dir = os.path.join(base_dir, "Audio")


class Crazy_rectangle:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.1)

        self.screen_width = 1000
        self.screen_height = 900

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Crazy Rectangle")

        # main rectangle
        self.rect_x = 450
        self.rect_y = 600
        self.rect_width = 70
        self.rect_height = 70
        self.rect_speed = 0.5

        # colors
        self.red = pygame.Color("red")
        self.black = pygame.Color("black")
        self.orange = pygame.Color("orange")
        self.white = pygame.Color("white")
        self.yellow = pygame.Color("yellow")

        # catchable rectangle
        self.catch_x = random.randint(0, 800)
        self.catch_y = random.randint(0, 800)
        self.catch_width = 40
        self.catch_height = 40

        self.points = 0

        # font
        self.font = pygame.font.SysFont("Arial", 40)
        self.text_x = 10
        self.text_y = 10

        # timer
        self.start_ticks = pygame.time.get_ticks()
        self.time_font = pygame.font.SysFont("Arial", 40)
        self.time = True

        # end font

        self.end_font = pygame.font.SysFont("Arial", 60)

        pygame.mixer.music.load("Audio/music1.mp3")
        pygame.mixer.music.play(-1)

    def start_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill(self.black)
            rect_move = pygame.key.get_pressed()

            if rect_move[pygame.K_LEFT]:
                if self.rect_x > 0:
                    self.rect_x -= self.rect_speed

            if rect_move[pygame.K_RIGHT]:
                if self.rect_x < self.screen_width - self.rect_width:
                    self.rect_x += self.rect_speed
            
            if rect_move[pygame.K_UP]:
                if self.rect_y > 0:
                    self.rect_y -= self.rect_speed

            if rect_move[pygame.K_DOWN]:
                if self.rect_y < self.screen_height - self.rect_height:
                    self.rect_y += self.rect_speed
            

            rend = self.font.render(f"Punkty: {self.points}",True, self.white)
            self.screen.blit(rend, (self.text_x, self.text_y))

            self.rectangle = pygame.Rect(self.rect_x, self.rect_y, self.rect_width, self.rect_height)
            self.catch = pygame.Rect(self.catch_x, self.catch_y, self.catch_width, self.catch_height)

         

            if self.rectangle.colliderect(self.catch):
                self.catch_x = random.randint(0, 800)
                self.catch_y = random.randint(0, 800)
                self.points += 1
                rend = self.font.render(f"Punkty: {self.points}",True, self.white)
                self.rect_speed += 0.1
                sound_effect = pygame.mixer.Sound(f"Audio/music2.mp3")
                sound_effect.play(0)


            pygame.draw.rect(self.screen, self.red, self.rectangle)
            pygame.draw.rect(self.screen, self.orange, self.catch)

            if self.time:
                elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000

            if elapsed_time == 60:
                self.rect_speed = 0
                self.time = False

                self.reset = pygame.Rect(400, 400, 245, 50)
                pygame.draw.rect(self.screen, self.yellow, self.reset)

                end = self.end_font.render("Gra zakończona", True, self.white)
                self.screen.blit(end, (350, 300))

                mouse_pouse = pygame.mouse.get_pos()

                if self.reset.collidepoint(mouse_pouse):
                    pygame.draw.rect(self.screen, self.white, self.reset)

                    if pygame.mouse.get_pressed()[0]:
                        self.start_ticks = pygame.time.get_ticks()
                        self.points = 0
                        self.time = True
                        self.rect_speed = 0.5
                        self.rect_x = 450
                        self.rect_y = 600
                        self.catch_x = random.randint(0, 800)
                        self.catch_y = random.randint(0, 800)


                play_again = self.font.render("Zagraj ponownie", False, self.black)
                self.screen.blit(play_again, (403, 400))

            timer_text = self.time_font.render(f"Czas: {elapsed_time}s", True, self.white)
            self.screen.blit(timer_text, (10, 60))
            pygame.display.update()



rt = Crazy_rectangle()
rt.start_game()


