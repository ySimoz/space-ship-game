import pygame, math


def enemies_ships_movement(self):
    enemies_ships_list = self.enemies_ships.sprites()
    current_tick: int = pygame.time.get_ticks()
    if current_tick- self.last_e_ships_movement > self.e_ships_movement_interval:
        for e_ship in enemies_ships_list:
            movement = (0, self.e_ships_movement_y)
            e_ship.move(movement[0], movement[1])
            self.last_e_ships_movement = current_tick

def enemies_ships_secondary_movement(self):
    enemies_ships_list = self.enemies_ships.sprites()
    current_tick: int = pygame.time.get_ticks()
    positions = []
    #pos1, pos2, pos3, pos4 = 
    
