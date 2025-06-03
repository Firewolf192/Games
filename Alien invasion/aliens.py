import pygame
from screen_settings import Screen

class Aliens:
    def __init__(self):
        self.image1 = pygame.image.load("alien/better_ship.png")
        self.width = 80
        self.height = 80
        self.speed1 = 2
        self.x1 = 150
        self.y1 = 10
        self.scale_image1 = pygame.transform.scale(self.image1, (self.width, self.height))

        self.screen = Screen()

        self.image2 = pygame.image.load("alien/orange_ship.png")
        self.width = 80
        self.height = 80
        self.speed2 = 2
        self.x2 = 150
        self.y2 = 100
        self.scale_image2 = pygame.transform.scale(self.image2, (self.width, self.height))

        self.image3 = pygame.image.load("alien/yellow_ship.png")
        self.width = 80
        self.height = 80
        self.speed3 = 2
        self.x3 = 150
        self.y3 = 190
        self.scale_image3 = pygame.transform.scale(self.image3, (self.width, self.height))

        self.alien_army = []



        self.move = {
            "left":True,
            "right":False
        }

    def spawn_first_wave(self):
        for _ in range(15):
            self.x1 += 90
            self.x1 = self.x1
            self.alien_army.append({
                "alien":self.scale_image1,
                "x":self.x1,
                "y":self.y1,
                "speed":self.speed1,
                "alive":True
            })

        for _ in range(15):
            self.x2 += 90
            self.x2 = self.x2
            self.alien_army.append({
                "alien":self.scale_image2,
                "x":self.x2,
                "y":self.y2,
                "speed":self.speed2,
                "alive":True
            })

        for _ in range(15):
            self.x3 += 90
            self.x3 = self.x3
            self.alien_army.append({
                "alien":self.scale_image3,
                "x":self.x3,
                "y":self.y3,
                "speed":self.speed3,
                "alive":True
            })

    def spawn_second_wave(self):
        for _ in range(15):
            self.x1 += 90
            self.x1 = self.x1
            self.alien_army.append({
                "alien":self.scale_image1,
                "x":self.x1,
                "y":self.y1,
                "speed":self.speed1,
                "alive":True
            })

        for _ in range(15):
            self.x2 += 90
            self.x2 = self.x2
            self.alien_army.append({
                "alien":self.scale_image2,
                "x":self.x2,
                "y":self.y2,
                "speed":self.speed2,
                "alive":True
            })

        for _ in range(15):
            self.x3 += 90
            self.x3 = self.x3
            self.alien_army.append({
                "alien":self.scale_image3,
                "x":self.x3,
                "y":self.y3,
                "speed":self.speed3,
                "alive":True
            })


    def alien_move(self):
        try:
            rect_max = max([alien["x"] for alien in self.alien_army if alien["alive"]])
            rect_min = min([alien["x"] for alien in self.alien_army if alien["alive"]])
        except ValueError:
            return
        
        if self.move["left"] and rect_min <= 0:
            self.move["left"] = False
            self.move["right"] = True

        elif self.move["right"] and rect_max >= self.screen.width - self.width:
            self.move["right"] = False
            self.move["left"] = True

        for alien in self.alien_army[:]:
            if self.move["left"]:
                alien["x"] -= alien["speed"]
            elif self.move["right"]:
                alien["x"] += alien["speed"]



    

    

                

                    
        

        
            
          