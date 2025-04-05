import pygame


def powerups_movement(self):
    # create a list of powerups.spites(), and then iterate trhough each one of them
    powerups_list: list =  [powerups.sprites() for powerups in self.powerups]
    for powerups in powerups_list:
        for powerup in powerups:
            powerup.move(0, powerup.speed * (self.time_elapsed / 1000))
