import pygame
from scripts.enemies.enemies_score_counter import EnemiesScoreCounter


def enemies_ships_setup(self):
    self.enemies_ships = pygame.sprite.Group()  # enemies ships group
    self.enemies_ships_exploded = pygame.sprite.Group()
    self.enemies_ships_size = (50, 60)
    self.enemies_ships_score_1 = 5  # values of the enemies ships n.1
    self.enemies_ships_score_2 = 10  # values of the enemies ships n.2
    self.last_ship = - 2000  # parameter for ship creation
    self.time_of_explosion = 300  # time for the explosion after the collision
    self.enemies_ships_created = 0  # number of enemies ships created
    self.last_e_ships_movement = 0  # counter for the tick of the last movement of the enemies ships
    self.e_ships_movement_interval = 3000  # milliseconds for the interval between each enemies ship movement
    self.e_ships_movement_y, self.e_ships_movement_x = 80, 0
    self.e_ships_secondary_movement_y, self.e_ships_secondary_movement_x = 25, 25
    self.enemies_ships_total_score = 0  # total score obtained by eliminating enemies ships

def enemies_score_counter_setup(self):
    self.enemies_score_counter_font = pygame.font.SysFont('Rockwell', 50)
    self.enemies_score_counter_position = (40, 70)
    self.enemies_score_counter_initial_score = 0
    self.enemies_score_counter_color = (0, 255, 0)  # green
    self.enemies_score_counter = EnemiesScoreCounter(self.enemies_score_counter_position,
                                                     self.enemies_score_counter_font,
                                                     self.enemies_score_counter_color,
                                                     self.enemies_score_counter_initial_score)  # score counter sprite
    self.enemies_score_counter_ = pygame.sprite.GroupSingle(self.enemies_score_counter)  # single group of the counter

