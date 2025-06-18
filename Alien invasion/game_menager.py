
from ship import Ship
from colors import Color
from shoot import Bullet
from sounds import SoundEfect
from aliens import Aliens
from allien_shoot import Laser
from screen_settings import Screen
from upgrade import Upgrade

class GameManager:
    def __init__(self):
        self.ship = Ship()
        self.color = Color()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        self.bullet = Bullet()
        self.sound = SoundEfect()
        self.alien = Aliens()
        self.weapon = Laser()
        self.weapon2 = Laser()
        self.screen = Screen()
        self.upgrade = Upgrade()
