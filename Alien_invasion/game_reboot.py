import pygame
import random

class Alien_invasion:
    def __init__(self):
        pygame.init()
        try:
            pygame.mixer.init()
        except pygame.error:
            pass

        pygame.mixer.set_num_channels(4)
        self.one_channel = pygame.mixer.Channel(1)

        self.clock = pygame.time.Clock()
        
        # screen
        self.screen_width = 1920
        self.screen_height = 1680
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # ship
        self.ship = pygame.image.load("alien/statek.png")
        
        self.ship_x = 900
        self.ship_y = 1000
        self.ship_width = 80
        self.ship_height = 80
        self.ship_speed = 5
        self.scale_ship = pygame.transform.scale(self.ship, (self.ship_width, self.ship_height))

        self.ship_left = pygame.image.load("alien/left.png")
        self.ship_left_scale = pygame.transform.scale(self.ship_left, (self.ship_width, self.ship_height))

        self.ship_right = pygame.image.load("alien/right.png")
        self.ship_right_scale = pygame.transform.scale(self.ship_right, (self.ship_width, self.ship_height))

        self.left_active = False
        self.right_active = False
        self.ship_alive = True

        # colors
        self.red = pygame.Color("red")
        self.black = pygame.Color("black")
        self.white = pygame.Color("white")
        self.yellow = pygame.Color("yellow")
        self.green = pygame.Color("green")


        # bullet
        self.bullet = pygame.image.load("alien/test.png")
        self.bullet_width = 50
        self.bullet_height = 200
        self.bullet_speed = 7
        self.scale_bullet = pygame.transform.scale(self.bullet, (self.bullet_width, self.bullet_height))
        self.bullet_army = []

        self.normal_fire = False
        self.rapid_fire = False

        # alien
        self.alien = pygame.image.load("alien/better_ship.png")
        self.alien_width = 80
        self.alien_height = 80
        self.scale_alien = pygame.transform.scale(self.alien, (self.alien_width, self.alien_height))
        self.alien_y = 100
        self.alien_x = 350

        self.alien_orange = pygame.image.load("alien/orange_ship.png")
        self.alien_width_orange = 80
        self.alien_height_orange = 80
        self.scale_alien_orange = pygame.transform.scale(self.alien_orange, (self.alien_width, self.alien_height))
        self.alien_y_orange = 200
        self.alien_x_orange = 350

        self.alien_yellow = pygame.image.load("alien/yellow_ship.png")
        self.alien_width_yellow = 80
        self.alien_height_yellow = 80
        self.scale_alien_yellow = pygame.transform.scale(self.alien_yellow, (self.alien_width, self.alien_height))
        self.alien_y_yellow = 300
        self.alien_x_yellow = 350

        self.start_timer = pygame.time.get_ticks()
        self.alien_army = []

        self.speed = False

        self.normal_alien = 15
        self.orange_alien = 15
        self.yellow_alien = 15

        self.laser_x = 0
        self.laser_y = 0

        self.laser_speed = 3

        self.laser_list = []

        for _ in range(self.normal_alien):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien,
                    "x":self.alien_x,
                    "y":self.alien_y,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_x += 90


        self.orange_alien_army = []

        for _ in range(self.orange_alien):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien_orange,
                    "x":self.alien_x_orange,
                    "y":self.alien_y_orange,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_x_orange += 90

        self.yellow_alien_army = []

        for _ in range(self.yellow_alien):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien_yellow,
                    "x":self.alien_x_yellow,
                    "y":self.alien_y_yellow,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_x_yellow += 90

        
        self.alien_directions = {
            "left":True,
            "right":False
        }



        # laser

        self.laser_image = pygame.image.load("alien/lahser.png")

        self.laser_width = 5
        self.laser_height = 150

        self.lahser = pygame.transform.scale(self.laser_image, (self.laser_width, self.laser_height))

        self.game_over = False  

        # explotion-image
        self.explode = pygame.image.load("alien/wybuch_2.png")
        self.explode_width = 100
        self.explode_height = 100
        self.scale_explode = pygame.transform.scale(self.explode, (self.explode_width, self.explode_height))

        self.explotion = False
        self.expotion_time = 0

        self.laser_timer = 0
        self.laser_time = False

        self.laser_ship_expoltion_start_timer = 0
        self.laser_ship_explotion = False

        self.ship_alien_exlpotion = 0


        self.alien_counter = 0

        self.random_choice = 0

        self.available_shoots = [index for index, _ in enumerate(self.alien_army)]
        self.random_shoot = random.choice(self.available_shoots)

        self.shoot_active = False
        self.shoot_timer = 0
        self.shoot_time = False


        self.repeat_shoot_timer = pygame.time.get_ticks()
        self.repeat = False

        self.spawn_alien_timer = pygame.time.get_ticks()


        self.available_aliens = [index for index, _ in enumerate(self.alien_army)]
        self.random_digit = random.choice(self.available_aliens)

        self.spawn_alien = True

        self.waves_counter = 1

        self.wave = pygame.font.SysFont("Arial", 40)
        self.text_wave = self.wave.render(f"Wave: {self.waves_counter}", True, self.white)

        self.wave_1 = True
        self.wave_2 = False
        self.wave_3 = False
        self.wave_4 = False
    
        self.final = False

        self.next_timer = 0
        self.next_exlode = False

        self.laser_upg = False

        self.two = True
        self.three = False
        self.four = False
        self.five = False

    
        self.flage = True
        self.t = pygame.time.get_ticks()


        self.timing = 0
        self.final_text = False


        self.roar = pygame.mixer.Sound("sound/rour_of_boss.wav")
        self.boss_fight = pygame.mixer.music.load("sound/boss_sound_fight.wav")

        self.final_boss = pygame.image.load("alien/final_boss.png")
        self.final_boss_red = pygame.image.load("alien/red.png")
        self.final_boss_width = 500
        self.final_boss_height = 500
        self.final_boss_x = 700
        self.final_boss_y = -500
        self.scale_final_boss = pygame.transform.scale(self.final_boss, (self.final_boss_width, self.final_boss_height))
        self.final_boss_speed = 2
        self.final_boss_alive = False

        self.scale_red = pygame.transform.scale(self.final_boss_red, (self.final_boss_width, self.final_boss_height))

        self.boss_spawning_timing = 0

        self.music_start_timer = pygame.time.get_ticks()

        self.music_active = False


        self.boss_move = {
            "left": True,
            "right": False
        }

#################################################################################################################################################
        
        self.green_width = 1300
        self.green_height = 50
        self.green_boss_life = pygame.Rect(300, 1320, self.green_width, self.green_height)

        self.red_width = 0
        self.red_height = 50
        self.red_boss_life = pygame.Rect(300, 1320, self.red_width, self.green_height)

        self.boss_dying = False

        self.flame = pygame.image.load("alien/flame.png")
        self.flame_x = None
        self.flame_y = None
        self.flame_width = 300
        self.flame_height = 300
        self.scale_flame = pygame.transform.scale(self.flame, (self.flame_width, self.flame_height))
        self.flame_speed = 10

        self.flame_active = False
        self.flame_timer = 0

        self.blaster = pygame.image.load("alien/blaster.png")
        self.blaster_x = None
        self.blaster_y = None
        self.blaster_width = 100
        self.blaster_height = 100
        self.scale_blaster = pygame.transform.scale(self.blaster, (self.blaster_width, self.blaster_height))
        self.blaster_speed = 10

        self.blaster_active = False
        self.blaster_timer = 0

        self.area = [50, 250, 500]
        self.random_area1 = random.choice(self.area)
        self.random_area2 = random.choice(self.area)

        self.roar_sound = False

        self.second_roar = pygame.mixer.Channel(2)
        self.second_timer = 0

        self.win = False

        self.upgrade = pygame.image.load("alien/rapidfire.png")
        self.upgrade_width = 50
        self.upgrade_height = 50
        self.upgrade_x = None
        self.upgrade_y = None
        self.scale_upgrade = pygame.transform.scale(self.upgrade, (self.upgrade_width, self.upgrade_height))
        self.upgrade_x2 = None
        self.upgrade_y2 = None
        self.upgrade_list = []

        self.choices = random.choices(self.alien_army, k = 1)
        self.choices2 = random.choices(self.alien_army, k = 1)
        

        self.upgrade_active = False
        self.upgrade_active2 = False

        self.upgrades = ["ship_speed", "bullet_speed", "rapid_fire"]
        self.upgrades2 = ["ship_speed", "bullet_speed", "rapid_fire"]

        self.choose = random.choice(self.upgrades)
        self.choose2 = random.choice(self.upgrades2)

        self.stop1 = False
        self.stop2 = False

        self.text = pygame.font.SysFont("Arial", 60)
    




    def create_alien_float(self):
        for _ in range(5):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien,
                    "x":self.alien_x,
                    "y":self.alien_y,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_y += 90


    def creat_orange_alien_float(self):
 

        for _ in range(5):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien_orange,
                    "x":self.alien_x_orange,
                    "y":self.alien_y_orange,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_y_orange += 90
            


    def creat_yellow_alien_float(self):
        for _ in range(14):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien_yellow,
                    "x":self.alien_x_yellow,
                    "y":self.alien_y_yellow,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_x_yellow += 90

    
    def create_alien_float2(self):
        for _ in range(8):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien,
                    "x":self.alien_x,
                    "y":self.alien_y,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_y += 90
            self.alien_x -= 90

    def creat_orange_alien_float2(self):
        for _ in range(14):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien_orange,
                    "x":self.alien_x_orange,
                    "y":self.alien_y_orange,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_x_orange += 90

    def creat_yellow_alien_float2(self):
        for _ in range(8):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien_yellow,
                    "x":self.alien_x_yellow,
                    "y":self.alien_y_yellow,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_x_yellow += 90
            self.alien_y_yellow += 90



    

    def show_ship(self):
        self.screen.blit(self.scale_ship, (self.ship_x, self.ship_y))

    def show_left_ship(self):
        self.screen.blit(self.ship_left_scale, (self.ship_x, self.ship_y))

    def show_right_ship(self):
        self.screen.blit(self.ship_right_scale, (self.ship_x, self.ship_y))

    def collision_allien_bullet(self, object):
        for alien in object:
            if alien["alive"]:
                alien_rect = pygame.Rect(alien["x"], alien["y"], self.alien_width_yellow, self.alien_height_yellow)
                 
            for bullet in self.bullet_army:
                bullet_rect = pygame.Rect(bullet["bullet_x"], bullet["bullet_y"], 40, self.bullet_height)
                
                try:
                    if bullet_rect.colliderect(alien_rect):
                        alien["alive"] = False
                        self.bullet_army.remove(bullet)
                        self.normal_fire = False
                        self.alien_counter += 1
                        
                        try:
                            for index in self.available_shoots:
                                self.available_shoots.pop(index)
                                break

                            for index in self.available_aliens:
                                self.available_aliens.pop(index)
                                break
                        except IndexError:
                            pass


                except UnboundLocalError:
                    pass

    def collision_alien_ship(self, object):
        if self.ship_alive and not self.game_over:
            ship_rect = pygame.Rect(self.ship_x, self.ship_y, self.ship_width, self.ship_height)
              
        
        for alien in object:
            if alien["alive"]:
                alien_rect = pygame.Rect(alien["x"], alien["y"], self.alien_width, self.alien_height)
           
                try:
                    if ship_rect.colliderect(alien_rect):
                        self.expotion_time = pygame.time.get_ticks()
                        self.explotion = True
                        self.game_over = True

                  
                except UnboundLocalError:
                    pass

    def create_alien_float_same(self):
        for _ in range(2):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien,
                    "x":self.alien_x,
                    "y":self.alien_y,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_x += 90
            self.alien_y -= 90

    def creat_orange_alien_float2_same(self):
        test = 10
        for _ in range(test):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien_orange,
                    "x":self.alien_x_orange,
                    "y":self.alien_y_orange,           
                    "alive":True,
                    "speed":2

                }

            )     
            self.alien_y_orange += 90

    def creat_yellow_alien_float2_same(self):
        for _ in range(2):
            self.alien_army.append(
                {
                    "alien_image":self.scale_alien_yellow,
                    "x":self.alien_x_yellow,
                    "y":self.alien_y_yellow,           
                    "alive":True,
                    "speed":2

                }

            )
            self.alien_x_yellow += 90
            self.alien_y_yellow += 90


    def show_alien(self, object):
        self.timer = pygame.time.get_ticks()

        for alien in object[:]:
            if alien["alive"]:    
                self.screen.blit(alien["alien_image"], (alien["x"], alien["y"]))


    def aliens_move(self, object):
        max_x = max([alien["x"] for alien in object if alien["alive"]], default = 0)
        min_x = min([alien["x"] for alien in object if alien["alive"]], default = 0)

        left_x = 1
        left = pygame.Rect(left_x, -10, 5, 2000)
        
        right = pygame.Rect(1915, -10, 5, 2000)
      
     
        if pygame.time.get_ticks() - self.t >= 2000:
            self.flage = False

  
        for alien in self.alien_army:
            if self.flage:
                alien["y"] += alien["speed"]

  
        for alien in object:
            if alien["x"] == max_x:
                max_rect = pygame.Rect(alien["x"], alien["y"], self.alien_width, self.alien_height)
            
             

            elif alien["x"] == min_x:
                min_rect = pygame.Rect(alien["x"], alien["y"], self.alien_width, self.alien_height)
            

        for alien in self.alien_army:
            try:
                if min_rect.colliderect(left):
                    self.alien_directions["left"] = False
                    self.alien_directions["right"] = True

                elif max_rect.colliderect(right):
                    self.alien_directions["right"] = False
                    self.alien_directions["left"] = True

            except UnboundLocalError:
                pass



        for alien in self.alien_army:
            if self.alien_directions["left"]:
                if alien["x"] > left_x:
                    alien["x"] -= alien["speed"]

            elif self.alien_directions["right"]:
                if alien["x"] < self.screen_width - self.alien_width:
                    alien["x"] += alien["speed"]




    def main_loop(self):
        running = True
        while running:
                 
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                
                if event.type == pygame.KEYDOWN and not self.normal_fire and not self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.bullet_army.append({
                            "bullet_image":self.scale_bullet,
                            "bullet_x":self.ship_x,
                            "bullet_y":self.ship_y,
                            "bullet_in_game":True
                        })


                if event.type == pygame.KEYDOWN and not self.rapid_fire and not self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.normal_fire = True

            try:      
                self.screen.fill(self.black)
            except AttributeError:
                pass

            # ship move
            ship_move = pygame.key.get_pressed()

            if ship_move[pygame.K_LEFT]:
                self.left_active = True
                self.right_active = False

                if self.ship_x > 0:
                    self.ship_x -= self.ship_speed
            else:
                self.left_active = False

            if ship_move[pygame.K_RIGHT]:
                self.right_active = True
                self.left_active = False

                if self.ship_x < self.screen_width - self.ship_width:
                    self.ship_x += self.ship_speed
            else:
                self.right_active = False
            
            if ship_move[pygame.K_UP]:
                if self.ship_y > 0:
                    self.ship_y -= self.ship_speed
            
            if ship_move[pygame.K_DOWN]:
                if self.ship_y < self.screen_height - self.ship_height:
                    self.ship_y += self.ship_speed


            # turn of ship
            if self.ship_alive and not self.left_active and not self.right_active:
                self.show_ship()

            if self.left_active and self.ship_alive:
                self.show_left_ship()

            if self.right_active and self.ship_alive:
                self.show_right_ship()

            # shoot
            if self.rapid_fire and not self.game_over:
                for bullet in self.bullet_army[:]:
                    self.screen.blit(bullet["bullet_image"], (bullet["bullet_x"], bullet["bullet_y"]))

                    if bullet["bullet_y"] > 0:
                        bullet["bullet_y"] -= self.bullet_speed
                    else:
                        bullet["x"] = self.ship_x
                        bullet["y"] = self.ship_y
                        self.bullet_army.remove(bullet)
                        self.rapid_fire_fire = False

            if self.normal_fire and not self.game_over:
                for bullet in self.bullet_army[:]:
                    self.screen.blit(bullet["bullet_image"], (bullet["bullet_x"], bullet["bullet_y"]))

                    if bullet["bullet_y"] > 0:
                        bullet["bullet_y"] -= self.bullet_speed

                    else:
                        bullet["x"] = self.ship_x
                        bullet["y"] = self.ship_y
                        self.bullet_army.remove(bullet)
                        self.normal_fire = False

            if not self.final and not self.win:
                self.collision_alien_ship(self.alien_army)
        
                
            if self.game_over:
                self.ship_alive = False
                self.ship_speed = 0
                self.random_digit = -1
                self.choice = -1

                game_over_font = pygame.font.SysFont("Arial", 100)
                game_over_text = game_over_font.render("Game over", True, self.white)
                self.screen.blit(game_over_text, (800, 700))

                reset = pygame.Rect(840, 900, 330, 70)
                pygame.draw.rect(self.screen, self.red, reset)

                mouse_pos = pygame.mouse.get_pos()

                if reset.collidepoint(mouse_pos):
                    pygame.draw.rect(self.screen, self.yellow, reset)

                    if pygame.mouse.get_pressed()[0]:
                        self.__init__()


                play_again = pygame.font.SysFont("Arlai", 70)
                play_again_text = play_again.render("Play again", True, self.black)
                self.screen.blit(play_again_text, (880, 910))

            if not self.final and not self.win:
                self.show_alien(self.alien_army)
                self.aliens_move(self.alien_army)
                self.collision_allien_bullet(self.alien_army)

         

            if self.explotion:
                if pygame.time.get_ticks() - self.expotion_time <= 1000:
                        self.screen.blit(self.scale_explode, (self.ship_x, self.ship_y))

            ship_rect = pygame.Rect(self.ship_x, self.ship_y, self.ship_width, self.ship_height)

            if pygame.time.get_ticks() - self.repeat_shoot_timer >= 2000:
                for index, alien in enumerate(self.alien_army):
                    if index == self.random_shoot:
                        self.laser_list.append({"image":self.lahser, "x":alien["x"], "y":alien["y"], "speed": 3, "in_game":True})

                        self.shoot_active = True  
                        self.repeat_shoot_timer = pygame.time.get_ticks()
                        try:  
                            self.available_shoots.pop(self.random_shoot)
                        except IndexError:
                            pass
                        break

            if not self.final and not self.win:
                for laser in self.laser_list[:]:
                    if self.shoot_active and not self.game_over:
                        self.shoot_timer = pygame.time.get_ticks()
                        self.next_timer = pygame.time.get_ticks()
                        self.screen.blit(laser["image"], (laser["x"], laser["y"]))

                        if laser["y"] < self.screen_height + self.laser_height:
                            laser["y"] += laser["speed"]

                        else:
                            self.laser_list.remove(laser)
                            try:
                                self.random_shoot = random.choice(self.available_shoots)
                            except IndexError:
                                pass


                    
                    if self.shoot_active and not self.game_over:
                        laser_rect = pygame.Rect(laser["x"], laser["y"], self.laser_width, self.laser_height)
                    
                        if ship_rect.colliderect(laser_rect):
                            self.next_exlode = True
                            self.game_over = True

            if self.next_exlode:
                if pygame.time.get_ticks() - self.next_timer <= 1000:
                    self.screen.blit(self.scale_explode, (self.ship_x, self.ship_y))


            if self.shoot_time:
                if pygame.time.get_ticks() - self.shoot_timer <= 1000:
                    self.screen.blit(self.scale_explode, (self.ship_x, self.ship_y))


            if self.two:
                if all(not alien["alive"] for alien in self.alien_army[:]):
                    self.alien_y = 335
                    self.alien_x = 350
                    self.alien_y_orange = 335
                    self.alien_x_orange = 1700
                    self.alien_y_yellow = 330
                    self.alien_x_yellow = 435

                    self.laser_upg = True

                    self.alien_army.clear()
                    self.create_alien_float()
                    self.creat_orange_alien_float()
                    self.creat_yellow_alien_float()
                    self.wave_1 = False
                    self.wave_2 = True

                    self.two = False
                    self.three = True

                    self.stop1 = False
                    self.stop2 = False

                    self.upgrade_x = None
                    self.upgrade_y = None

                    self.upgrade_x2 = None
                    self.upgrade_y2 = None




                    self.choices = random.choices(self.alien_army, k = 1)
                    self.choices2 = random.choices(self.alien_army, k = 1)
                    

                
                    for index, alien in enumerate(self.alien_army):
                        self.available_shoots.append(index)

                    self.random_shoot = random.choice(self.available_shoots)

                    
            if self.three:
                if all(not alien["alive"] for alien in self.alien_army[:]):
                    self.alien_y = 350
                    self.alien_x = 1630

                    self.alien_y_orange = 350
                    self.alien_x_orange = 350

                    self.alien_y_yellow = 350
                    self.alien_x_yellow = 260

                    self.laser_upg = True

                    self.alien_army.clear()
                    self.create_alien_float2()
                    self.creat_orange_alien_float2()
                    self.creat_yellow_alien_float2()
                    self.wave_2 = False
                    self.wave_3 = True

                    self.three = False
                    self.four = True

                    for index, alien in enumerate(self.alien_army):
                        self.available_shoots.append(index)

                    self.random_shoot = random.choice(self.available_shoots)

                    self.stop1 = False
                    self.stop2 = False

                    self.upgrade_x = None
                    self.upgrade_y = None

                    self.upgrade_x2 = None
                    self.upgrade_y2 = None



                    self.choices = random.choices(self.alien_army, k = 1)
                    self.choices2 = random.choices(self.alien_army, k = 1)
                    


            if self.four:
                if all(not alien["alive"] for alien in self.alien_army[:]):
                    self.alien_y = 10
                    self.alien_x = 1854
                    self.alien_y_orange = 10
                    self.alien_x_orange = 1000
                    self.alien_y_yellow = 10
                    self.alien_x_yellow = 140
                    self.wave_3 = False
                    self.wave_4 = True

                    self.four = False
                    self.five = True

               
                    self.alien_army.clear()
                    self.create_alien_float2()
            
                    self.creat_yellow_alien_float2()
              
                    for index, alien in enumerate(self.alien_army):
                        self.available_shoots.append(index)

                    self.random_shoot = random.choice(self.available_shoots)
                    self.speed = True

                    if self.five:
                        self.timing = pygame.time.get_ticks()
                        self.boss_spawning_timing = pygame.time.get_ticks()
                        self.flame_timer = pygame.time.get_ticks()
                        self.final = True

                    self.stop1 = False
                    self.stop2 = False


                    self.choices = random.choices(self.alien_army, k = 1)
                    self.choices2 = random.choices(self.alien_army, k = 1)
                    


            if self.stop1 == False:
                for alien in self.choices:
                    if not alien["alive"]:
                        if self.upgrade_x is not None and self.upgrade_y is not None:
                            upgrade_rect = pygame.Rect(self.upgrade_x, self.upgrade_y, self.upgrade_width, self.upgrade_height)
                            ship_rect = pygame.Rect(self.ship_x, self.ship_y, self.ship_width, self.ship_height)
                          
                            
                            self.upgrade_active = True
                            
                            if ship_rect.colliderect(upgrade_rect):
                                self.stop1 = True
                                self.upgrade_active = False

                                if self.choose == "ship_speed":
                                    self.ship_speed += 0.5

                                elif self.choose == "bullet_speed":
                                    self.bullet_speed += 5

                                if self.choose == "rapid_fire" and self.rapid_fire == False:
                                    self.rapid_fire = True
                                else:
                                    self.ship_speed += 2

                                

                                self.choose = random.choice(self.upgrades)

                        else:
                            self.upgrade_x = alien["x"]
                            self.upgrade_y = alien["y"]
                

            if self.stop2 == False:
                for alien in self.choices2:
                    if not alien["alive"]:
                        if self.upgrade_x2 is not None and self.upgrade_y2 is not None:
                            upgrade_rect2 = pygame.Rect(self.upgrade_x2, self.upgrade_y2, self.upgrade_width, self.upgrade_height)
                            ship_rect2 = pygame.Rect(self.ship_x, self.ship_y, self.ship_width, self.ship_height)
                            self.upgrade_active2 = True

                            if ship_rect2.colliderect(upgrade_rect2):

                                if self.choose == "ship_speed":
                                    self.ship_speed += 0.5

                                elif self.choose == "bullet_speed":
                                    self.bullet_speed += 5

                                elif self.choose == "rapid_fire" and self.rapid_fire == False:
                                    self.rapid_fire = True

                                self.stop2 = True
                                self.upgrade_active2 = False

                                self.choose2 = random.choice(self.upgrades)

                        else:
                            self.upgrade_x2 = alien["x"]
                            self.upgrade_y2 = alien["y"]

            try:
                if self.upgrade_active:
                    self.screen.blit(self.scale_upgrade, (self.upgrade_x, self.upgrade_y))
                    self.upgrade_y += 5

                if self.upgrade_active2:
                    self.screen.blit(self.scale_upgrade, (self.upgrade_x2, self.upgrade_y2))   
                    self.upgrade_y2 += 5
            except TypeError:
                pass

            
            if self.laser_upg:
                for laser in self.laser_list[:]:
                    laser["speed"] = 6

            if self.speed:
                for alien in self.alien_army[:]:
                    alien["speed"] = 7

                for laser in self.laser_list[:]:
                    laser["speed"] = 10


            if self.wave_1 and not self.final and not self.win:
                wave_1 = self.wave.render(f"Wave 1", True, self.white)
                self.screen.blit(wave_1, (12, 1300))

            if self.wave_2 and not self.final and not self.win:
                wave_2 = self.wave.render(f"Wave 2", True, self.white)
                self.screen.blit(wave_2, (12, 1300))

            if self.wave_3 and not self.final and not self.win:
                wave_3 = self.wave.render(f"Wave 3", True, self.white)
                self.screen.blit(wave_3, (12, 1300))

            if self.wave_4 and not self.final and not self.win:
                wave_4 = self.wave.render(f"Wave 4", True, self.white)
                self.screen.blit(wave_4, (12, 1300))

            if self.final:
                boss_rect = pygame.Rect(self.final_boss_x, self.final_boss_y, self.final_boss_width, self.final_boss_height)
                ship_rect = pygame.Rect(self.ship_x, self.ship_y, self.ship_width, self.ship_height)

          
                if boss_rect.colliderect(ship_rect):
                    self.game_over = True
               
           
                final_text = pygame.font.SysFont("Arial", 60)
                final = final_text.render("You woke up something terrifyring", True, self.white)

                if pygame.time.get_ticks() - self.timing <= 2000:
                    self.screen.blit(final, (600, 400))
                    self.one_channel.play(self.roar)
                    

                if pygame.time.get_ticks() - self.boss_spawning_timing >= 4000:
                    self.final_boss_alive = True

                if self.final_boss_alive:
                    self.screen.blit(self.scale_final_boss, (self.final_boss_x, self.final_boss_y))
                    if self.final_boss_y < 300:
                        self.final_boss_y += self.final_boss_speed

                 
                        if not self.music_active:
                            pygame.mixer.music.play(-1)
                            self.music_active = True

                    else:
                        if self.boss_move["left"]:
                            if self.final_boss_x > 0:
                                self.final_boss_x -= self.final_boss_speed
                            else:
                                self.boss_move["left"] = False
                                self.boss_move["right"] = True

                        
                        if self.boss_move["right"]:
                            if self.final_boss_x < self.screen_width - self.final_boss_width:
                                self.final_boss_x += self.final_boss_speed
                            else:
                                self.boss_move["right"] = False
                                self.boss_move["left"] = True

                    pygame.draw.rect(self.screen, self.green, self.green_boss_life)
                    for bullet in self.bullet_army[:]:
                        bullet_rect = pygame.Rect(bullet["bullet_x"], bullet["bullet_y"], self.bullet_width, self.bullet_height)
                        
                        if bullet_rect.colliderect(boss_rect):
                            self.bullet_army.remove(bullet)
                            if self.red_width < 1300:
                                self.red_width += 10
                                self.red_boss_life = pygame.Rect(300, 1320, self.red_width, self.green_height)
                                self.boss_dying = True
                            else:
                                self.final = False
                                self.final_boss_alive = False
                                self.win = True
                                
                            if self.normal_fire:
                                self.normal_fire = False

                            
                    if self.boss_dying:
                        pygame.draw.rect(self.screen, self.red, self.red_boss_life)
                    
                    self.second_timer = pygame.time.get_ticks()
                    

                    if pygame.time.get_ticks() - self.flame_timer > 10000:
                        self.flame_active = True

                    if self.flame_active and self.flame_x is not None and self.flame_x is not None:
                        if self.flame_active:
                            flame_rect = pygame.Rect(self.flame_x, self.flame_y, self.flame_width, self.flame_height)
                            self.screen.blit(self.scale_flame, (self.flame_x, self.flame_y))
                          

                            if self.flame_y < self.screen_height + self.flame_height:
                                self.flame_y += self.flame_speed

                                if flame_rect.colliderect(ship_rect):
                                    self.game_over = True

                            else:
                                self.flame_active = False
                                self.flame_timer = pygame.time.get_ticks()
                                self.random_area1 = random.choice(self.area)
                          
                                
                    else:
                        self.flame_x = self.final_boss_x + self.random_area1
                        self.flame_y = self.final_boss_y

                    if pygame.time.get_ticks() - self.blaster_timer > 1000:
                        self.blaster_active = True

                    if self.blaster_active and self.blaster_x is not None and self.blaster_y is not None:

                        if self.blaster_active:
                            blaster_rect = pygame.Rect(self.blaster_x, self.blaster_y, self.blaster_width, self.blaster_height)
                            self.screen.blit(self.scale_blaster, (self.blaster_x, self.blaster_y))

                            if self.blaster_y < self.screen_height + self.blaster_height:
                                self.blaster_y += self.blaster_speed

                                if blaster_rect.colliderect(ship_rect):
                                    self.game_over = True

                            else:
                                self.blaster_active = False
                                self.blaster_timer = pygame.time.get_ticks()
                                self.random_area2 = random.choice(self.area)
                         
                    else:
                        self.blaster_x = self.final_boss_x + self.random_area2
                        self.blaster_y = self.final_boss_y

                    
                    if self.red_width >= 650:
                        self.flame_speed = 20
                        self.blaster_speed = 20
                        self.final_boss_speed = 10
                        self.screen.blit(self.scale_red, (self.final_boss_x, self.final_boss_y))

                        if not self.roar_sound:
                            self.second_roar.play(self.roar)
                            self.roar_sound = True

            if self.win:
                last_text = pygame.font.SysFont("Arial", 90)
                last = last_text.render("Game won!", True, self.white)
                self.screen.blit(last, (750, 400))

                reset = pygame.Rect(765, 610, 330, 70)
                pygame.draw.rect(self.screen, self.red, reset)

                mouse_pos = pygame.mouse.get_pos()

                if reset.collidepoint(mouse_pos):
                    pygame.draw.rect(self.screen, self.yellow, reset)

                    if pygame.mouse.get_pressed()[0]:
                        self.__init__()


                play_again = pygame.font.SysFont("Arlai", 70)
                play_again_text = play_again.render("Play again", True, self.black)
                self.screen.blit(play_again_text, (800, 620))


            pygame.display.update()
            self.clock.tick(60)

ai = Alien_invasion()
ai.main_loop()
