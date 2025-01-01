import sys
from time import sleep #allows to pause the game when a ship is hit 
import pygame

from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
class AlienInvasion:
    #class to maange game assests and behaviour
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #size of window screen
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        #create instance of game stats to store scores
        self.stats = GameStats(self)
        #grouping bullets that have been fired in the screen
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.ship = Ship(self)
        self._create_fleet()        

        

        


        #changing the background colour
        self.bg_color = (self.settings.bg_color) #light grey color

    def run_game(self):
            
            #start main loop for the game
            
            while True:
                #watches for keyboard and mouse venets
                self._check_events()
                if self.stats.game_active:

                    self.ship.update()
                    self._update_bullets()
                    self._update_aliens()
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
        self._check_bullet_alien_collisions()
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens, True,True) #detects collisions between 2 groups which in this case is bullets and the aliens 
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet
    def _create_fleet(self):
        #create a fleet of aliens
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y =(self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        # create alien fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    def _check_fleet_edges(self):
        #to respond once an alien reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        #drop entire fleet down and changes its direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        #ship to alien collisions
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        #responding to when ship is hit by aliens
        if self.stats.ships_left > 0:

            self.stats.ships_left -= 1 

            #get rid of remaining alienms and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause 
            sleep(0.5)
        else:
            self.stats.game_active = False
    def _check_aliens_bottom(self):
        #checks if aliens have reach the bottom
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #same as if ship got hit by aliens
                self._ship_hit()
                break

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