import pygame
from scripts.projectiles.projectile import Projectile, e_Projectile
from scripts.projectiles.projectile_movement import *


def launch_projectile(self):
    current_tick = pygame.time.get_ticks()
    # interval between to different projectiles-
    # projectile launch state
    if self.ship.bullets > 0 and self.space_press_state and current_tick - self.last_projectile >= self.projectile_interval:
    #triple projectile state
        position1 = (self.ship.rect.x + ((self.ship.size[0] / 2) - (self.projectile_size[0] / 2)),
                                    self.ship.rect.y)  # position of the projectile
        self.projectiles.add(Projectile(position1, self.projectile_speed, self.projectile_size))
        if self.ship.triple_bullets_boost == True:
            position2, position3 = (self.ship.rect.x, self.ship.rect.y), ((self.ship.rect.x + self.ship.size[0]) - self.projectile_size[0], self.ship.rect.y)
            self.projectiles.add(Projectile(position2, self.projectile_speed, self.projectile_size))
            self.projectiles.add(Projectile(position3, self.projectile_speed, self.projectile_size))
        self.ship.bullets -= 1
        self.last_projectile = current_tick


def e_launch_projectile(self):
    current_tick = pygame.time.get_ticks()
    enemies_ships_list = self.enemies_ships.sprites()
    for ship in enemies_ships_list:
        if current_tick - ship.last_projectile >= self.e_projectile_interval:
            if ship.projectile_state:
                position = (ship.rect.x + ((self.ship.size[0] / 2) - (self.e_projectile_size[0] / 2)),
                            ship.rect.y + self.enemies_ships_size[1] - 10)  # position of the projectile
                self.e_projectiles.add(e_Projectile(position, self.e_projectile_speed,
                                                    self.e_projectile_size, calculate_e_projectiles_angle(self,
                                                                                                          position)))  # create and add the e_proj to the group
                ship.last_projectile = current_tick


# vanish projectiles
def vanish_projectile(self):  # remove the projectiles once the've reached the border
    projectiles_list = self.projectiles.sprites()
    e_projectiles_list = self.enemies_ships.sprites()
    for proj in projectiles_list:
        if proj.rect.y <= 0:
            self.projectiles.remove(proj)
    for e_proj in e_projectiles_list:
        if e_proj.rect.y > self.screen.get_height() or e_proj.rect.x > self.screen.get_width() or e_proj.rect.x < -e_proj.rect[2]:
            self.e_projectiles.remove(e_proj)