import pygame
from scripts.structure.assets import LifeBarAssets


class ShipLifeBar(pygame.sprite.Sprite):
    def __init__(self, position, size, state):
        pygame.sprite.Sprite.__init__(self)

        self.pos = position
        self.size = size

        self.image = pygame.transform.scale(LifeBarAssets.life_bar_images[state], self.size)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position[0], position[1]

        self.current_state = state
        self.previous_state = self.current_state

    def update(self, *args, **kwargs):
        self.current_state = kwargs.get('state', self.current_state)
        self.current_state += kwargs.get('increase_state', 0)
        if self.current_state != self.previous_state:
            self.image = pygame.transform.scale(LifeBarAssets.life_bar_images[self.current_state], self.size)
            self.previous_state = self.current_state


