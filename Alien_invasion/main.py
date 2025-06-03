import pygame
from game_menager import GameManager



class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.status = GameManager()

        self.window = pygame.display.set_mode((self.status.screen.width, self.status.screen.height))
        self.clock = pygame.time.Clock()

        self.status.alien.spawn_first_wave()

        self.game_over = False
        
    def reset(self):
        self.game_over = False
        self.status.alien.alien_army.clear()
        self.status.alien.x1 = 150
        self.status.alien.y1 = 10
        self.status.alien.x2 = 150
        self.status.alien.y2 = 100
        self.status.alien.x3 = 150
        self.status.alien.y3 = 190
        self.status.ship.x = 850
        self.status.ship.y = 800
        self.status.alien.spawn_first_wave()
        self.status.ship.speed = 4
                                

    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.status.bullet.normal_fire and self.status.bullet.bullet_in_game and not self.game_over:
                        pygame.mixer.Sound.play(self.status.sound.shoot)
                        self.status.bullet.normal_active = True
          
                    elif event.key == pygame.K_SPACE and self.status.bullet.rapid_active and not self.game_over:
                        self.status.bullet.bullets.append({
                            "image": self.status.bullet.scale_image,
                            "x":self.status.ship.x,
                            "y":self.status.ship.y,
                            "speed": self.status.bullet.speed,
                            "ingame":True
                        })
                        pygame.mixer.Sound.play(self.status.sound.shoot)

          
            self.window.fill(self.status.color.black)

            if self.status.ship.standart and self.status.ship.alive and not self.game_over:
                self.status.ship.normal(self.window)

            if self.status.ship.turn_left and self.status.ship.alive and not self.game_over:
                self.status.ship.left(self.window)

            if self.status.ship.turn_right and self.status.ship.alive and not self.game_over:
                self.status.ship.right(self.window)

            move = pygame.key.get_pressed()

            if move[pygame.K_RIGHT]:
                self.status.ship.turn_right = True
                self.status.ship.standart = False
                self.status.ship.move_right()
            else:
                self.status.ship.standart = True
                self.status.ship.turn_right = False

            if move[pygame.K_LEFT]:
                self.status.ship.turn_left = True
                self.status.ship.standart = False
                self.status.ship.move_left()
            else:
                self.status.ship.turn_left = False

            if move[pygame.K_UP]:
                self.status.ship.move_up()

            if move[pygame.K_DOWN]:
                self.status.ship.move_down()

            if move[pygame.K_LEFT] and move[pygame.K_RIGHT]:
                self.status.ship.turn_left = False
                self.status.ship.turn_right = False
                self.status.ship.standart = True

            if self.status.bullet.normal_active: 
                if self.status.bullet.x is not None and self.status.bullet.y is not None:
                    if self.status.bullet.bullet_in_game:
                        self.window.blit(self.status.bullet.scale_image, (self.status.bullet.x, self.status.bullet.y))
                                
                else:
                    self.status.bullet.x = self.status.ship.x
                    self.status.bullet.y = self.status.ship.y
                self.status.bullet.move()

            if self.status.bullet.rapid_active:
                for bullet in self.status.bullet.bullets[:]:
                    self.window.blit(bullet["image"], (bullet["x"], bullet["y"]))

                if self.status.bullet.rapid_active:
                    for bullet in self.status.bullet.bullets[:]:
                        bul_rect = pygame.Rect(bullet["x"], bullet["y"], self.status.bullet.width, self.status.bullet.height)

                        if bullet["y"] + self.status.bullet.height >= 0:
                            bullet["y"] -= bullet["speed"]
                        else:
                            self.status.bullet.bullets.remove(bullet)
                        
                        for alien in self.status.alien.alien_army[:]:
                            if alien["alive"]:
                                al_rect = pygame.Rect(alien["x"], alien["y"], self.status.alien.width, self.status.alien.height)

                                if bul_rect.colliderect(al_rect):
                                    bullet["ingame"] = False
                                    alien["alive"] = False
                                    self.status.bullet.bullets.remove(bullet)
                                    break
                        
            for alien in self.status.alien.alien_army[:]:
                if alien["alive"]:
                    self.window.blit(alien["alien"], (alien["x"], alien["y"]))
            
            self.status.alien.alien_move()
            if self.status.bullet.x is not None and self.status.bullet.y is not None:
                if self.status.bullet.bullet_in_game:
                    bullet_rect = pygame.Rect(self.status.bullet.x, self.status.bullet.y, self.status.bullet.width, self.status.bullet.height)
                   
                for alien in self.status.alien.alien_army[:]:
                    if alien["alive"]:
                        alien_rect = pygame.Rect(alien["x"], alien["y"], self.status.alien.width, self.status.alien.height)

                        if bullet_rect.colliderect(alien_rect):
                            alien["alive"] = False
                            self.status.bullet.reset()
                            break    
            
            for laser in self.status.weapon.lahsers:
                if laser["in_game"]:
                    rect = pygame.Rect(laser["x"], laser["y"], self.status.weapon.width, self.status.weapon.height)
                    self.window.blit(laser["image"], (laser["x"], laser["y"]))
                    
                    ship_rect = pygame.Rect(self.status.ship.x, self.status.ship.y, self.status.ship.width, self.status.ship.height)

                    if rect.colliderect(ship_rect):
                        self.game_over = True

            if self.game_over:
                self.status.ship.speed = 0

                last_text = pygame.font.SysFont("Arial", 90)
                last = last_text.render("Game lost", True, self.status.color.white)
                self.window.blit(last, (750, 400))

                reset = pygame.Rect(765, 610, 330, 70)
                pygame.draw.rect(self.window, self.status.color.red, reset)

                mouse_pos = pygame.mouse.get_pos()

                if reset.collidepoint(mouse_pos):
                    pygame.draw.rect(self.window, self.status.color.yellow, reset)

                    if pygame.mouse.get_pressed()[0]:
                        self.reset()
                       
                    
                play_again = pygame.font.SysFont("Arlai", 70)
                play_again_text = play_again.render("Play again", True, self.status.color.black)
                self.window.blit(play_again_text, (800, 620))

            self.status.weapon.laser_move()

            if self.status.alien.wave1:
                if all(not alien["alive"] for alien in self.status.alien.alien_army[:]):
                    self.status.alien.alien_army.clear()

                    self.status.alien.spawn_second_wave()
                    self.status.alien.wave1 = False
                    self.status.alien.wave2 = True

            if self.status.alien.wave2:
                if all(not alien["alive"] for alien in self.status.alien.alien_army[:]):
                    self.status.alien.alien_army.clear()
                    self.status.alien.spawn_third_wave()
                    self.status.alien.wave2 = False
                    self.status.alien.wave3 = True

            if self.status.alien.wave3:
                if all(not alien["alive"] for alien in self.status.alien.alien_army[:]):
                    self.status.alien.alien_army.clear()
                    self.status.alien.spawn_fourth_wave()

            self.status.upgrade.show_upgrade(self.window)
            self.status.upgrade.upgrade_move()
            pygame.display.update()
            self.clock.tick(60)

ai = Main()
ai.main_loop()