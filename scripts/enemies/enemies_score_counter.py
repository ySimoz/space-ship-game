import pygame



class EnemiesScoreCounter(pygame.sprite.Sprite):
    def __init__(self, position, font, color, initial_score, *groups, **kwargs):
        pygame.sprite.Sprite.__init__(self, *groups)

        self.position: tuple = position
        self.font: pygame.font.Font = font
        self.color: tuple = color

        self.inital_score: int = initial_score
        self.score: int = self.inital_score

        self.text: str = str(self.score)

        self.image: pygame.Surface = self.font.render(self.text, True, self.color)
        self.rect: pygame.Rect = self.image.get_rect()  # rect values for counter surface
        self.rect.x, self.rect.y = self.position[0], self.position[1]  # x, y position on the screen

    def update(self, *args, **kwargs):  # pass the increment of the score, be positive for adding and negative for subtracting, or pass the total bullets value
        if "additional_score" in kwargs:
            additional_score: int = int(kwargs.get("additional_score", 0))
            self.score += additional_score

        elif "total_score" in kwargs:
            total_score: int = int(kwargs.get("total_score", self.score))
            self.score: int = total_score

        self.text: str = str(self.score)  # pre-rendered text (str)
        self.image: pygame.Surface = self.font.render(self.text, True, self.color)  # change the imagae with the new score