import pygame

def projectiles_recharge(self, r_bullets):
    current_tick = pygame.time.get_ticks()
    if self.r_key_press_state and current_tick - self.recharge_initial_time >= self.recharge_time:
        if self.ship.bullets + r_bullets < self.ship_max_bullets:
            self.ship.bullets += r_bullets
        else:
            self.ship.bullets = self.ship_max_bullets
        self.r_key_press_state = False