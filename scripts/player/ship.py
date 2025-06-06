import pygame
from scripts.structure.assets import ShipAssets
from scripts.setup.powerups_setup import *
from scripts.player.ship_powerups_boost import *

class Ship(pygame.sprite.DirtySprite):  # spaceship class
    def __init__(self, position, speed, size, bullets, lives, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)

        self.pos: tuple= position
        self.size: tuple = size
        # image load
        self.image: pygame.Surface = pygame.transform.scale(ShipAssets().ship_image, self.size)  # ship size
        self.rect: pygame.Rect =  self.image.get_rect()  # parameters for sprite
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)

        self.max_lives: int = lives
        self.lives: int = self.max_lives # number of maximum lives
        self.bullets: int = bullets # number of projectiles ship currently has

        self.speed: int = speed
        self.speed_boost: False
        self.original_speed: int = self.speed
        self.speed_effect_recept_time: int = 0
        self.speed_effect_time: int = 0

        self.immunity = False
        self.immunity_effect_recept_time = 0
        self.immunity_effect_time = 0

        self.triple_bullets_boost = False
        self.triple_bullets_effect_recept_time: int = 0
        self.triple_bullets_effect_time: int = 0

        self.alive_state = True
        self.exploded_time = 0
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


    def update(self, **kwargs):
        receive_powerups_boost(self, **kwargs)

    def explode(self):
        from scripts.structure.assets import EnemiesShipsAssets
        self.image = pygame.transform.scale(EnemiesShipsAssets().e_ships_exploded_1, (110, 80))
        self.rect.x -= 30
        self.rect.y -= 10
        self.exploded_time = pygame.time.get_ticks()
        self.alive_state = False


class ShipShield(pygame.sprite.Sprite):
    def __init__(self, position, speed, size, *groups, **kwargs):
        pygame.sprite.Sprite.__init__(self, *groups)

        self.pos = position
        self.speed = speed
        self.size = size

        self.image: pygame.Surface = pygame.transform.scale(ShipAssets().ship_shield_image, self.size)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)


    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


    def update(self, *args, **kwargs):
        position = kwargs.get('position', 0)
        if position != 0:
            self.rect.x, self.rect.y = position[0] - 10, position[1] - 10

