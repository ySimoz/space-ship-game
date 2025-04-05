import pygame
from scripts.projectiles.projectiles_counter import ProjectilesCounter
from scripts.structure.assets import ProjectileAssets
from scripts.projectiles.projectile import Projectile

def projectiles_setup(self):
    self.projectiles = pygame.sprite.Group()  # player ship proj group
    self.last_projectile = - 500  # parameter for projectile creation
    self.projectile_interval = 300  # parameter for projectile time interval
    self.projectile_speed = 250  # player ship proj speed
    self.projectile_size = (30, 50)  # player ship projectile size


def e_projectiles_setup(self):
    self.e_projectiles = pygame.sprite.Group()  # enemies proj group
    self.e_projectile_interval = 700  # parameter for e_projectile time interval
    self.e_projectile_speed = 250  # enemies projectile speed
    self.e_projectile_size = (30, 50)


def projectiles_counter_setup(self):
    self.projectile_counter_font = pygame.font.SysFont('Rockwell', 40)
    self.projectile_counter_position = (215, 32)
    self.prjectiles_counter_bullets = self.ship_max_bullets
    self.projectiles_counter_color, self.projectiles_counter_color2 = (255, 255, 255), (255, 0, 0)  #color 1 = white, color 2 = red
    self.projectiles_counter = ProjectilesCounter(self.projectile_counter_position,
                                                                        self.projectile_counter_font,
                                                                        self.projectiles_counter_color,
                                                                        self.projectiles_counter_color2,
                                                                        self.prjectiles_counter_bullets)

    self.projectiles_counter_projectile = Projectile(position= (250, 23), speed = 0, size= (23,40))  # sample projectile image for projectile counter

    self.projectiles_counter_ = pygame.sprite.Group(self.projectiles_counter, self.projectiles_counter_projectile)


def projectiles_recharge_setup(self):
    self.r_key_press_state = False  # control the pressing of the r_key to recharge bullets
    self.recharge_initial_time = 0
    self.recharge_time = 700
    self.r_bullets_1 = 15
