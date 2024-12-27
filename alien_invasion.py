import sys

import pygame

from setting import Settings
from ship import Ship

class AlienInvasion:
    #class to maange game assests and behaviour
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #size of window screen
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        #changing the background colour
        self.bg_color = (self.settings.bg_color) #light grey color
    def run_game(self):
            
            #start main loop for the game
            
            while True:
                #watches for keyboard and mouse venets
                self._check_events()
                self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        #update the images on the screen, flip to new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()