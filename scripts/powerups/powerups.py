import pygame
from scripts.structure.assets import *
powerup_assets = PowerUpAssets()

class Powerup(pygame.sprite.DirtySprite):
    def __init__(self, position, size, speed, powerup_name, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)

        self.pos: tuple = position
        self.size: tuple = size
        self.speed: int = speed
        self.name = powerup_name
        self.powerup: tuple = powerup_assets.powerups.get(self.name)

        self.image: pygame.Surface = pygame.transform.scale(self.powerup[1], self.size)  # powerup[1] gives the png image from assets

        self.rect: pygame.Rect = self.image.get_rect()  # parameters for sprite rect values
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]  # parameters for sprite position

        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)  # mask for perfect pixel collision

    def move(self, dx, dy):  # movemnt function
        self.rect.x += dx
        self.rect.y += dy

