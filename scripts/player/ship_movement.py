import pygame
from scripts.player.ship import Ship

# main movement function for the main ship, see handle events for key press event creation

def move_ship(self):
    if self.movement[0] and self.ship.rect.y >= self.y_boundaries:  # Up
        self.ship.move(0, -self.ship.speed * (self.time_elapsed / 1000))
    if self.movement[1] and self.ship.rect.y <= self.screen.get_height() - self.ship.rect.height:  # Down
        self.ship.move(0, self.ship.speed * (self.time_elapsed / 1000))
    if self.movement[2] and self.ship.rect.x >= 0:  # Left
        self.ship.move(-self.ship.speed * (self.time_elapsed / 1000), 0)
    if self.movement[3] and self.ship.rect.x <= self.screen.get_width() - self.ship.rect.width:  # Right
        self.ship.move(self.ship.speed * (self.time_elapsed / 1000), 0)


def move_ship_shield(self):
    self.ship_shield_.update(position = (self.ship.rect.x, self.ship.rect.y))