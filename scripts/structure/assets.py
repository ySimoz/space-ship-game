import pygame, os
from dataclasses import dataclass



@dataclass
class ShipAssets:
    ship_image = pygame.image.load("assets/sprites/space-ship.png")
    ship_shield_image = pygame.image.load("assets/sprites/bubble-shield.png")

@dataclass
class EnemiesShipsAssets:
    e_ships_1 = pygame.image.load("assets/sprites/red-ship.png")
    e_ships_2 = pygame.image.load("assets/sprites/purple-ship.png")
    e_ships_exploded_1 = pygame.image.load("assets/sprites/exploded-ship.png")

@dataclass
class ProjectileAssets:
    projectile = pygame.image.load("assets/sprites/yellow-beam.png")
    e_projectile = pygame.image.load("assets/sprites/red-beam.png")


@dataclass
class BossesAssets:
    bosses_image_1 = pygame.image.load("assets/sprites/boss-ship.png")


@dataclass
class PowerUpAssets:
    powerups = {
    "red_powerup"    : (0, pygame.image.load("assets/sprites/red-orb.png")),
    "blue_powerup"   : (1, pygame.image.load("assets/sprites/blue-orb.png")),
    "green_powerup"  : (2, pygame.image.load("assets/sprites/green-orb.png")),
    "orange_powerup" : (3, pygame.image.load("assets/sprites/orange-orb.png"))
    }


@dataclass
class LifeBarAssets:
    life_bar_image_0 = pygame.image.load("assets/sprites/life-bar-0.png")
    life_bar_image_1 = pygame.image.load("assets/sprites/life-bar-1.png")
    life_bar_image_2 = pygame.image.load("assets/sprites/life-bar-2.png")
    life_bar_image_3 = pygame.image.load("assets/sprites/life-bar-3.png")
    life_bar_image_4 = pygame.image.load("assets/sprites/life-bar-4.png")
    life_bar_image_5 = pygame.image.load("assets/sprites/life-bar-5.png")
    life_bar_images = [life_bar_image_0, life_bar_image_1, life_bar_image_2, life_bar_image_3, life_bar_image_4, life_bar_image_5]