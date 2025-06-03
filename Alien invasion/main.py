import pygame
from screen_settings import Screen
from ship import Ship
from colors import Color
from shoot import Bullet
from sounds import SoundEfect
from aliens import Aliens
from allien_shoot import Laser


class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = Screen()
        self.window = pygame.display.set_mode((self.screen.width, self.screen.height))

        self.ship = Ship()
        self.color = Color()
        self.bullet = Bullet()
        self.sound = SoundEfect()
        
        self.alien = Aliens()
        self.clock = pygame.time.Clock()
        self.weapon = Laser()

        self.alien.spawn_first_wave()

        self.game_over = False
        

    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.bullet.normal_fire and self.bullet.bullet_in_game and not self.game_over:
                        pygame.mixer.Sound.play(self.sound.shoot)
                        self.bullet.normal_active = True
          
                    elif event.key == pygame.K_SPACE and self.bullet.rapid_active and not self.game_over:
                        self.bullet.bullets.append({
                            "image": self.bullet.scale_image,
                            "x":self.ship.x,
                            "y":self.ship.y,
                            "speed": self.bullet.speed,
                            "ingame":True
                        })
                        pygame.mixer.Sound.play(self.sound.shoot)

          
            self.window.fill(self.color.black)

            if self.ship.standart and self.ship.alive and not self.game_over:
                self.ship.normal(self.window)

            if self.ship.turn_left and self.ship.alive and not self.game_over:
                self.ship.left(self.window)

            if self.ship.turn_right and self.ship.alive and not self.game_over:
                self.ship.right(self.window)

            move = pygame.key.get_pressed()

            if move[pygame.K_RIGHT]:
                self.ship.turn_right = True
                self.ship.standart = False
                self.ship.move_right()
            else:
                self.ship.standart = True
                self.ship.turn_right = False

            if move[pygame.K_LEFT]:
                self.ship.turn_left = True
                self.ship.standart = False
                self.ship.move_left()
            else:
                self.ship.turn_left = False

            if move[pygame.K_UP]:
                self.ship.move_up()

            if move[pygame.K_DOWN]:
                self.ship.move_down()

            if move[pygame.K_LEFT] and move[pygame.K_RIGHT]:
                self.ship.turn_left = False
                self.ship.turn_right = False
                self.ship.standart = True

            if self.bullet.normal_active: 
                if self.bullet.x is not None and self.bullet.y is not None:
                    if self.bullet.bullet_in_game:
                        self.window.blit(self.bullet.scale_image, (self.bullet.x, self.bullet.y))
                                
                else:
                    self.bullet.x = self.ship.x
                    self.bullet.y = self.ship.y
                self.bullet.move()

            if self.bullet.rapid_active:
                for bullet in self.bullet.bullets[:]:
                    self.window.blit(bullet["image"], (bullet["x"], bullet["y"]))

            if self.bullet.rapid_active:
                for bullet in self.bullet.bullets[:]:
                    bul_rect = pygame.Rect(bullet["x"], bullet["y"], self.bullet.width, self.bullet.height)

                    if bullet["y"] + self.bullet.height >= 0:
                        bullet["y"] -= bullet["speed"]
                    else:
                        self.bullet.bullets.remove(bullet)
                    
                    for alien in self.alien.alien_army[:]:
                        if alien["alive"]:
                            al_rect = pygame.Rect(alien["x"], alien["y"], self.alien.width, self.alien.height)

                        if bul_rect.colliderect(al_rect):
                            bullet["ingame"] = False
                            alien["alive"] = False
                            self.bullet.bullets.pop(0)
                            break
                        
            for alien in self.alien.alien_army[:]:
                if alien["alive"]:
                    self.window.blit(alien["alien"], (alien["x"], alien["y"]))
            
            self.alien.alien_move()
            if self.bullet.x is not None and self.bullet.y is not None:
                if self.bullet.bullet_in_game:
                    bullet_rect = pygame.Rect(self.bullet.x, self.bullet.y, self.bullet.width, self.bullet.height)
                   
                for alien in self.alien.alien_army[:]:
                    if alien["alive"]:
                        alien_rect = pygame.Rect(alien["x"], alien["y"], self.alien.width, self.alien.height)

                        if bullet_rect.colliderect(alien_rect):
                            alien["alive"] = False
                            self.bullet.reset()
                            break    
            
            for laser in self.weapon.lahsers:
                if laser["in_game"]:
                    rect = pygame.Rect(laser["x"], laser["y"], self.weapon.width, self.weapon.height)
                    self.window.blit(laser["image"], (laser["x"], laser["y"]))
                    ship_rect = pygame.Rect(self.ship.x, self.ship.y, self.ship.width, self.ship.height)

                    if rect.colliderect(ship_rect):
                        self.game_over = True

            if self.game_over:
                self.ship.speed = 0

                last_text = pygame.font.SysFont("Arial", 90)
                last = last_text.render("Game lost", True, self.color.white)
                self.window.blit(last, (750, 400))

                reset = pygame.Rect(765, 610, 330, 70)
                pygame.draw.rect(self.window, self.color.red, reset)

                mouse_pos = pygame.mouse.get_pos()

                if reset.collidepoint(mouse_pos):
                    pygame.draw.rect(self.window, self.color.yellow, reset)

                    if pygame.mouse.get_pressed()[0]:
                        self.__init__()

                play_again = pygame.font.SysFont("Arlai", 70)
                play_again_text = play_again.render("Play again", True, self.color.black)
                self.window.blit(play_again_text, (800, 620))

            self.weapon.laser_move()

        
            if all(not alien["alive"] for alien in self.alien.alien_army[:]):
                self.alien.spawn_second_wave()
                    
            pygame.display.update()
            self.clock.tick(60)

ai = Main()
ai.main_loop()