import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #class alien ship

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #load the image and set its rect attribute
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        #position ufo at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)