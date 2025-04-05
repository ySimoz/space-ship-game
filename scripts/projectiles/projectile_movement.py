import pygame, random, math


def move_projectiles(self):  # shi projectile movement
    projectiles_list: list = self.projectiles.sprites()
    for proj in projectiles_list:
        proj.move(0, -proj.speed * (self.time_elapsed / 1000))


def move_e_projectiles(self):  # enemies ship projectiles movement
    e_projectiles_list: list = self.e_projectiles.sprites()
    for e_proj in e_projectiles_list:
        e_proj.move(e_proj.vector_x * (self.time_elapsed / 1000), e_proj.vector_y * (self.time_elapsed / 1000))


def calculate_e_projectiles_angle(self, e_proj_position):
    e_proj_pos = e_proj_position
    ship_pos = (self.ship.rect.x, self.ship.rect.y)

    return math.degrees(
        math.atan2(
            (ship_pos[0] - e_proj_pos[0]), (ship_pos[1] - e_proj_pos[1])
        )
    )

