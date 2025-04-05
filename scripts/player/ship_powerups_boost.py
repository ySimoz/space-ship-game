import pygame

def receive_powerups_boost(self, **kwargs):
    power = kwargs.get("power", {})
    if power is not {}:
        current_time = pygame.time.get_ticks()

        if not self.lives + power.get('lives', 0) > self.max_lives:
            self.lives += power.get('lives', 0)

        self.bullets += power.get('bullets', 0)

        # orange powerup immunity effet
        self.immunity = power.get('immunity', self.immunity)
        self.immunity_effect_time = power.get('immunity_effect_time', self.immunity_effect_time)
        self.immunity_effect_recept_time = power.get('orange_powerup_recept_time', self.immunity_effect_recept_time)

        # blue powerup speed & triple bullets effect
        self.speed += power.get('speed', 0)
        self.speed_effect_time = power.get('speed_effect_time', self.speed_effect_time)
        self.speed_effect_recept_time = power.get('blue_powerup_recept_time', self.speed_effect_recept_time)

        self.triple_bullets_boost = power.get("triple_bullets_boost", self.triple_bullets_boost)
        self.triple_bullets_effect_time = power.get('triple_bullets_effect_time', self.triple_bullets_effect_time)
        self.triple_bullets_effect_recept_time = power.get('blue_powerup_recept_time', self.triple_bullets_effect_recept_time)

    if current_time - self.immunity_effect_recept_time > self.immunity_effect_time:
        self.immunity = False

    if current_time - self.speed_effect_recept_time > self.speed_effect_time:
        self.speed = self.original_speed
        
    if current_time - self.triple_bullets_effect_recept_time > self.triple_bullets_effect_time:
        self.triple_bullets_boost = False


def ship_shield_effect(self):
    if self.ship.immunity and not self.ship_shield_.has(self.ship_shield):
        self.ship_shield_.add(self.ship_shield)
    if not self.ship.immunity and self.ship_shield_.has(self.ship_shield):
        self.ship_shield_.remove(self.ship_shield)

    if self.ship_shield_.has(self.ship_shield):
        self.ship_shield_.update(position=(self.ship.rect.x, self.ship.rect.y))
        self.ship_shield_.draw(self.screen)