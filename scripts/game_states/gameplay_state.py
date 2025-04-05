import pygame
#structure import
from scripts.structure.handle_events import *
from scripts.structure.collision import *
from scripts.structure.time_control import *

#game_states import
from scripts.game_states.game_states import *

#pojectiles
from scripts.projectiles.projectile_creation import *
from scripts.projectiles.projectile_movement import *
from scripts.projectiles.projectiles_counter import *
from scripts.projectiles.projectile_recharge import *

#enemies
from scripts.enemies.enemies_creation import *
from scripts.enemies.enemies_movement import *

#ship
from scripts.player.ship_movement import *
from scripts.player.ship_powerups_boost import *

#poweups
from scripts.powerups.powerups_creation import *
from scripts.powerups.powerups_movement import *

#setup
from scripts.setup.general_setup import *
from scripts.setup.initial_menu_setup import *


def gameplay_start_animation(self):
    for j in range(1,4):
        handle_events(self)
        
        self.screen.fill((0, 0, 0))
        gsa_writing = str(4 - j)
        gsa_writing_surface = self.gsa_font.render(gsa_writing, True, (0,255,0))
        self.screen.blit(gsa_writing_surface, self.gsa_writing_position)
        pygame.display.flip()
        pygame.time.delay(1000)
    

def gameplay_state(self):
    # main loop of the game, each section control one aspect:
    # handles events, time control, enemies, enemies projectile,
    # player ship, ship projectile.
    # each frame check for collision, move, update and draw sprites
    
    gameplay_start_animation(self)
    
    while self.gameplay_running_state:
        self.screen.fill((0, 0, 0))

        #event and time control
        handle_events(self)  # event control
        time_frame_control(self) #time control
        update_timer(self) # update and draw the timer on the screen

        # projectiles counter
        # if "total_bullets" its passed it will update directly the counter with the new bullets, if "additional_bullets" is passed
        # the counter with the new bullets, it will add the values (positive values for addition, negative for soctaction)
        projectiles_recharge(self, self.r_bullets_1)
        self.projectiles_counter_.draw(self.screen)
        self.projectiles_counter.update(total_bullets = self.ship.bullets, ship = self.ship)


        # enemies, creates, moves, update,jkgk draw, explode, remove the enemies, ship
        create_enemies_ship(self)
        enemies_ships_collision(self)
        enemies_ships_movement(self)
        self.enemies_ships.update()
        self.enemies_ships.draw(self.screen)
        self.enemies_ships_exploded.draw(self.screen)
        remove_enemies_ship(self)

        #updtate and draw thew enemies ships score counter
        self.enemies_score_counter_.update(total_score = self.enemies_ships_total_score)
        self.enemies_score_counter_.draw(self.screen)

        # enemies projectile, launch, move, update, draw, the enemies projectiles
        e_launch_projectile(self)
        move_e_projectiles(self)
        self.projectiles.update()
        self.e_projectiles.draw(self.screen)

        # powerups, draw the powerups groups
        powerups_movement(self)
        for powerups in self.powerups: powerups.draw(self.screen)

        # ship, moves, update, draw the player ship, and the ships effects
        ship_collision(self)
        move_ship(self)
        self.ship_.update()
        self.ship_.draw(self.screen)
        ship_shield_effect(self)

        #updtae and draw the player ship life bar
        self.ship_life_bar_.update(state = self.ship.lives)
        self.ship_life_bar_.draw(self.screen)

        # ship projectile, launch, move, update, draw, the player ship projectiles
        launch_projectile(self)
        vanish_projectile(self) # make all the projectiles outside borders be removed from the projectiles, e_projectiles Groups
        move_projectiles(self)
        self.projectiles.update() 
        self.projectiles.draw(self.screen)


        # show the changes on the display
        pygame.display.flip()
        