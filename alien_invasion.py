import sys

import pygame

from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    #class to maange game assests and behaviour
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #size of window screen
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        #grouping bullets that have been fired in the screen
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()        
        self.ship = Ship(self)

        


        #changing the background colour
        self.bg_color = (self.settings.bg_color) #light grey color

    def run_game(self):
            
            #start main loop for the game
            
            while True:
                #watches for keyboard and mouse venets
                self._check_events()
                self.ship.update()
                self._update_bullets()
                
                self._update_screen()

    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()


                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP: #keyup indicates releasing the right arrow key
                self._check_keyup_events(event)
    #event checks for keydown events 
    def _check_keydown_events(self,event):
        #responds to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    #event checks for keyup events
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_q:
            sys.exit()
    #function to fire bullet
    def _fire_bullet(self):
        #create a new bullet and add it to bullet group
        if len(self.bullets) < self.settings.bullet_allowed: #only creates a new bullet sprite of the length of bullets is less than allowed amount (3)
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #update the position of bullets + deleting old bullets
        self.bullets.update() 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        #create a fleet of aliens
        alien = Alien(self)
        self.aliens.add(alien)
    def _update_screen(self):
        #update the images on the screen, flip to new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()