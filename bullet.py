import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #class to manage bullets fried from shio

    def __init__(self, ai_game):
        super().__init__() #inherits from sprite class

        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color

        #creating a buillet rect at 0,0 and then set correct pos 
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullets pos as a deciaml value
        self.y = float(self.rect.y)

        #using update function to manage the bullets position
    def update(self):
        #moving bullet up the screen
        self.y -=self.settings.bullet_speed
        self.rect.y = self.y #updating the rect position

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)