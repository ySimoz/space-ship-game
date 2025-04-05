import math

import pygame
from scripts.structure.assets import *


class Projectile(pygame.sprite.DirtySprite):
    def __init__(self, position, speed, size, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)

        self.pos: tuple= position  # position and speed
        self.speed: int = speed
        self.size: tuple = size
        self.image: pygame.Surface = pygame.transform.scale(ProjectileAssets().projectile, self.size)  # projectile size

        self.rect: pygame.Rect  = self.image.get_rect()  # parameters for sprite rect values
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]  # parameters for sprite position

        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)  # mask for perfect pixel collision

    def move(self, dx, dy):  # movement function
        self.rect.x += dx
        self.rect.y += dy


class e_Projectile(pygame.sprite.DirtySprite):
    def __init__(self, position, speed, size, angle, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)

        self.pos: tuple = position  # postion and speed
        self.speed: int = speed
        self.size: tuple = size
        self.angle: int = angle

        self.vector_x: float = math.sin(math.radians(self.angle)) * self.speed  # coordinates system swapped (y, x)
        self.vector_y: float = math.cos(math.radians(self.angle)) * self.speed  # coordinates system swapped (y, x)

        self.pre_image = pygame.transform.scale(ProjectileAssets().e_projectile, self.size)
        self.image: pygame.Surface = pygame.transform.rotate(self.pre_image, self.angle)  # projectile size

        self.pre_rect = self.pre_image.get_rect()
        self.rect: pygame.Rect = self.image.get_rect()  # parameters for sprite rect values
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]  # parameters for sprite position

        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)  # mask for perfect pixel collision

    def move(self, dx, dy):  # movemnt function
        self.rect.x += dx
        self.rect.y += dy

    def direction(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.vector_x: float = math.sin(math.radians(angle)) * self.speed  # coordinates system swapped (y, x)
        self.vector_y: float = math.cos(math.radians(angle)) * self.speed
