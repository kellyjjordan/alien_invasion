import sys

import pygame

from setting import Settings
class AlienInvasion:
    #class to maange game assests and behaviour
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #size of window screen
        pygame.display.set_caption("Alien Invasion")
        
        #changing the background colour
        self.bg_color = (self.settings.bg_color) #light grey color

    def run_game(self):
            #start main loop for the game
            while True:
                #watches for keyboard and mouse venets
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                self.screen.fill(self.bg_color)
                pygame.display.flip() #continously updates the game for each event

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()