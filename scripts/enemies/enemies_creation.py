import pygame, random
from scripts.enemies.enemies import *
from scripts.structure.collision import *
from scripts.powerups.powerups_creation import *


def create_enemies_ship(self):
    if pygame.time.get_ticks() - self.last_ship < 2000:
        return
    creation = True
    while creation:
        position = (random.randint(0, 500), random.randint(100, 200))
        rect = pygame.Rect(position[0], position[1], self.enemies_ships_size[0], self.enemies_ships_size[1])
        if not e_ship_creation_collision(self, rect):
            if self.enemies_ships_created % 5 == 0:
                self.enemies_ships.add(EnemiesShip2(self.enemies_ships_size, position, 0, self.enemies_ships_score_2))  # add to the ships Group
            else:
                self.enemies_ships.add(EnemiesShip(self.enemies_ships_size, position, 0, self.enemies_ships_score_1))  # add to the ships Group
            self.enemies_ships_created += 1
            self.last_ship = pygame.time.get_ticks()
            creation = False


def remove_enemies_ship(self):
    enemies_ships_list_exploded = self.enemies_ships_exploded.sprites()
    for e_ship in enemies_ships_list_exploded:  # iterate through the list to remove the exploded ships
        if not e_ship.alive_state and pygame.time.get_ticks() - e_ship.exploded_time >= self.time_of_explosion:  # calculate the time passed after the explosion
            self.enemies_ships_exploded.remove(e_ship)# remove the ship
            self.enemies_ships_total_score += e_ship.score  # add the score of the exploded ship on the total score
            powerup_creation(self,(e_ship.rect.x + (self.powerups_size[0] / 2), e_ship.rect.y + (self.powerups_size[1] / 2)))  # call the powerup function to create a powerup at the exploded ship position
