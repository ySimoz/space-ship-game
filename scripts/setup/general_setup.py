import pygame
from scripts.setup.ship_setup import *
from scripts.setup.enemies_setup import *
from scripts.setup.projectile_setup import *
from scripts.setup.timer_setup import *
from scripts.setup.powerups_setup import *
from scripts.setup.initial_menu_setup import *
from scripts.game_states.game_states import *

def general_setup(self):
    #sprites setup
    #player
    ship_setup(self)
    ship_shield_setup(self)
    ship_life_bar_setup(self)

    #enemies
    enemies_ships_setup(self)
    enemies_score_counter_setup(self)

    #projectiles
    projectiles_setup(self)
    e_projectiles_setup(self)

    #powerups
    powerups_setup(self)

    # structure set up
    timer_setup(self)
    ship_movement_setup(self)
    projectiles_counter_setup(self)
    projectiles_recharge_setup(self)
    setup_states(self)


    #initial menu setup
    initial_menu_setup(self)
    gameplay_start_animation_setup(self)
