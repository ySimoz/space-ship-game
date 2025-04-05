import pygame
from scripts.structure.assets import *

#enemies ship sprite class definition,
# enemie ship 1 and 2 and bosses

class EnemiesShip(pygame.sprite.DirtySprite):
    def __init__(self, size, position, speed, score, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)

        self.pos: tuple = position
        self.size: tuple = size
        self.speed: int = speed
        self.score: int = score
        self.image: pygame.Surface = pygame.transform.scale(EnemiesShipsAssets().e_ships_1,
                                            self.size)  # bad ship size
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)

        # explosion control
        self.alive_state: bool = True
        self.exploded_time: int = 0
        # life control
        self.lives: int = 3
        # projectile control
        self.projectile_state: bool = False
        self.last_projectile: int = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def explode(self):
        self.image = pygame.transform.scale(EnemiesShipsAssets().e_ships_exploded_1,
                                            (110, 80))  # bad ship size
        self.rect.x -= 30
        self.rect.y -= 10
        self.exploded_time = pygame.time.get_ticks()
        self.alive_state = False


class EnemiesShip2(pygame.sprite.DirtySprite):
    def __init__(self, size, position, speed, score, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)

        self.pos = position
        self.size = size
        self.speed: int = speed
        self.score: int = score
        self.image = pygame.transform.scale(EnemiesShipsAssets().e_ships_2,
                                            self.size)  # bad ship size
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)

        # explosion control
        self.alive_state = True
        self.exploded_time = 0
        # life control
        self.lives = 2
        # projectile control
        self.projectile_state = True
        self.last_projectile = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def explode(self):
        self.image = pygame.transform.scale(EnemiesShipsAssets().e_ships_exploded_1,
                                            (110, 80))  # bad ship size
        self.rect.x -= 30
        self.rect.y -= 10
        self.exploded_time = pygame.time.get_ticks()
        self.alive_state = False



class Boss_1(pygame.sprite.DirtySprite):
    def __init__(self, position, size, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)
        self.image = pygame.transform.scale(pygame.image.load('files/images'))
