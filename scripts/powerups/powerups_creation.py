import pygame, random
from scripts.powerups.powerups import *


def powerup_creation(self, position):
    if random.randint(1,2) == 1:
        powerup_name: str = self.powerups_names[random.randint(0,len(self.powerups_names)-1)]
        self.red_powerups.add(Powerup(position, self.powerups_size, self.powerups_speed, powerup_name))


def give_ship_powerups(self, powerups):
    for pu in powerups:
        for p in pu:
            # put the reception time into the powerups effects dictionary
            self.powerups_effects[p.name][(f"{p.name}_recept_time")] = pygame.time.get_ticks()
            #get the effect from the powerups effects dictionary
            power_effect = self.powerups_effects.get(p.name)
            #pass it to the ship update method
            self.ship.update(power=power_effect)

