import pygame
from scripts.player.ship import Ship, ShipShield
from scripts.player.ship_life_bar import ShipLifeBar


def ship_setup(self):
    self.ship_size = (60, 60)  # player ship size
    self.ship_speed = 350  # player ship speed
    self.ship_max_bullets = 70  # number of bullets player ship can max have
    self.ship_max_bullets = 70  # number of bullets player ship can max have
    self.ship_initial_position = (270, 600)  # initial position of player ship on the screen
    self.ship_max_lives = 5  # number lives of playe ship
    self.ship = Ship(self.ship_initial_position, self.ship_speed, self.ship_size,
                                                self.ship_max_bullets, self.ship_max_lives)  # player ship
    self.ship_ = pygame.sprite.GroupSingle(
        self.ship)  # single ship group containing player ship, used for drawing and updating method
    self.y_boundaries = 400  # boundaries for ship movement

def ship_shield_setup(self):
    self.ship_shield_size = (80, 80)
    self.ship_shield_speed = 350
    self.ship_shield_initial_position = (0, 0)
    self.ship_shield = ShipShield(self.ship_shield_initial_position, self.ship_shield_speed, self.ship_shield_size)
    self.ship_shield_ = pygame.sprite.GroupSingle()

def ship_movement_setup(self):
    self.movement_state = True
    self.movement = [False, False, False, False]  # up down lef right
    self.space_press_state = False  # control the pressing of the space to launche projectile


def ship_life_bar_setup(self):
    self.ship_life_bar_position = (30, 25)
    self.ship_life_bar_size = (150, 38)
    self.life_bar_initial_state = 5
    self.ship_life_bar = ShipLifeBar(self.ship_life_bar_position, self.ship_life_bar_size, self.life_bar_initial_state)
    self.ship_life_bar_ = pygame.sprite.GroupSingle(self.ship_life_bar)
