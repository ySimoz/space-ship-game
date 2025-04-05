import pygame
from scripts.structure.assets import ProjectileAssets


class ProjectilesCounter(pygame.sprite.Sprite):
    def __init__(self, position, font, color, color2, bullets):
        pygame.sprite.Sprite.__init__(self)

        self.position: tuple = position
        self.font: pygame.font.Font = font
        self.color: tuple = color
        self.color2: tuple = color2
        self.max_bullets: int = bullets
        self.bullets: int = self.max_bullets

        self.text: str = str(bullets)

        self.image: pygame.Surface =  self.font.render(self.text, True, self.color)
        self.rect: pygame.Rect = self.image.get_rect()  # rect values for counter surface
        self.rect.x, self.rect.y = self.position[0], self.position[1]  # x, y position on the screen

    #update the proj counter accordingly to the argument
    def update(self, *args, **kwargs):  #pass the increment of bullets, be positive for adding and negative for subtracting, or pass the total bullets value
        if "additional_bullets" in kwargs:
            additional_bullets: int = int(kwargs["additional_bullets"])
            self.bullets += additional_bullets
            ship: pygame.sprite.Sprite = kwargs["ship"]
            ship.bullets += additional_bullets
        elif "total_bullets" in kwargs:
            total_bullets: int = int(kwargs["total_bullets"])
            self.bullets: int = total_bullets
            ship: pygame.sprite.Sprite = kwargs["ship"]
            ship.bullets = total_bullets
            color = self.color if self.bullets > 20 else self.color2
        self.text: str = str(self.bullets)  # pre-rendered text (str)
        self.image: pygame.Surface = self.font.render(self.text, True, color)  # rendered text (pygame.Surface)







