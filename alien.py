import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #class alien ship

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the image and set its rect attribute
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        #position ufo at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
    def update(self):
            #moving aliens to the right
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    
