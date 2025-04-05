import pygame
from scripts.powerups.powerups_creation import *


def powerups_setup(self):
    # four different groups for powerups
    self.red_powerups = pygame.sprite.Group()
    self.blue_powerups = pygame.sprite.Group()
    self.green_powerups = pygame.sprite.Group()
    self.orange_powerups = pygame.sprite.Group()
    self.powerups = [self.red_powerups, self.blue_powerups, self.green_powerups, self.orange_powerups]

    self.powerups_names = ["red_powerup", "blue_powerup", "green_powerup", "orange_powerup"]
    self.powerups_size = (30,30)
    self.powerups_speed = 150

    #powerups effects
    self.powerups_effects = {
        "red_powerup" : {"bullets": 25, "red_powerup_recept_time": 0},
        "blue_powerup": {"speed": 150, "speed_effect_time": 5000, "triple_bullets_boost": True, "triple_bullets_effect_time": 5000, 
                        "blue_powerup_recept_time": 0},
        "green_powerup" : {"lives": 1, "green_powerup_recept_time": 0},
        "orange_powerup": {"immunity": True, "immunity_effect_time": 5000, "orange_powerup_recept_time": 0},
        
    }


