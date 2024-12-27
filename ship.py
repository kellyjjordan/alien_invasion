import pygame
class Ship:
    #class to manage the ship

    def __init__(self, ai_game):
        #initialize the ship and its starting pos in the game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship and its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start ship at the bottom center 
        self.rect.midbottom = self.screen_rect.midbottom 

    def blitme(self):
        self.screen.blit(self.image, self.rect)