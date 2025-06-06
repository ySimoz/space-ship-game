from dataclasses import dataclass
from utils import resource_path
import pygame


@dataclass
class ShipAssets:
    def __init__(self):
        self.ship_image = pygame.image.load(resource_path("assets/sprites/space-ship.png"))
        self.ship_shield_image = pygame.image.load(resource_path("assets/sprites/bubble-shield.png"))

@dataclass
class EnemiesShipsAssets:
    def __init__(self):
        self.e_ships_1 = pygame.image.load(resource_path("assets/sprites/red-ship.png"))
        self.e_ships_2 = pygame.image.load(resource_path("assets/sprites/purple-ship.png"))
        self.e_ships_exploded_1 = pygame.image.load(resource_path("assets/sprites/exploded-ship.png"))

@dataclass
class ProjectileAssets:
    def __init__(self):
        self.projectile = pygame.image.load(resource_path("assets/sprites/yellow-beam.png"))
        self.e_projectile = pygame.image.load(resource_path("assets/sprites/red-beam.png"))

@dataclass
class BossesAssets:
    def __init__(self):
        self.bosses_image_1 = pygame.image.load(resource_path("assets/sprites/boss-ship.png"))

@dataclass
class PowerUpAssets:
    def __init__(self):
        self.powerups = {
            "red_powerup"    : (0, pygame.image.load(resource_path("assets/sprites/red-orb.png"))),
            "blue_powerup"   : (1, pygame.image.load(resource_path("assets/sprites/blue-orb.png"))),
            "green_powerup"  : (2, pygame.image.load(resource_path("assets/sprites/green-orb.png"))),
            "orange_powerup" : (3, pygame.image.load(resource_path("assets/sprites/orange-orb.png")))
        }

@dataclass
class LifeBarAssets:
    def __init__(self):
        self.life_bar_image_0 = pygame.image.load(resource_path("assets/sprites/life-bar-0.png"))
        self.life_bar_image_1 = pygame.image.load(resource_path("assets/sprites/life-bar-1.png"))
        self.life_bar_image_2 = pygame.image.load(resource_path("assets/sprites/life-bar-2.png"))
        self.life_bar_image_3 = pygame.image.load(resource_path("assets/sprites/life-bar-3.png"))
        self.life_bar_image_4 = pygame.image.load(resource_path("assets/sprites/life-bar-4.png"))
        self.life_bar_image_5 = pygame.image.load(resource_path("assets/sprites/life-bar-5.png"))
        self.life_bar_images = [
            self.life_bar_image_0,
            self.life_bar_image_1,
            self.life_bar_image_2,
            self.life_bar_image_3,
            self.life_bar_image_4,
            self.life_bar_image_5
        ]