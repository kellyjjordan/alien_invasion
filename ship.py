import pygame
class Ship:
    #class to manage the ship

    def __init__(self, ai_game):
        #initialize the ship and its starting pos in the game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the ship and its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #store a decimal value for the ships horizontal pos
        self.x = float(self.rect.x)


        #start ship at the bottom center 
        self.rect.midbottom = self.screen_rect.midbottom 
    #flag for continous movement 
        self.move_right = False
        self.move_left = False
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x+= self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed # - since its going to the negative x value plane 
        #checking if the ship is about to go off the screen = stopping it 
        #update rect object from self.x 
    def blitme(self):
        self.screen.blit(self.image, self.rect)