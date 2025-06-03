import pygame

class SoundEfect:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.boss_fight_music = pygame.mixer.music.load("sound/boss_sound_fight.wav")
        self.game_music = pygame.mixer.music.load("sound/game_music.wav")
        pygame.mixer.music.play(-1)

        self.rour = pygame.mixer.Sound("sound/rour_of_boss.wav")
        self.shoot = pygame.mixer.Sound("sound/shoot.wav")

  
      








