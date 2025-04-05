import pygame, random
from scripts.powerups.powerups_creation import *

# player ship projectiles group collision with enenmies ship

def enemies_ships_collision(self):
    collided_projectiles = pygame.sprite.groupcollide(self.projectiles, self.enemies_ships, True, dokillb= False, collided= pygame.sprite.collide_mask)
    for ships in collided_projectiles.values():
        for ship in ships:
            ship.lives -= 1  # life check and explosion
            if ship.lives == 0:
                ship.explode()
                self.enemies_ships.remove(ship)
                self.enemies_ships_exploded.add(ship)

#method to check for the creation of new enemies ships calculating the rect collision at specific position
def e_ship_creation_collision(self, rect):
    enemies_ship_list = self.enemies_ships.sprites()
    for e_ship in enemies_ship_list:
        if e_ship.rect.colliderect(rect):
            return True


#group collision between player ship single group and enemies projectiles, and powerups
def ship_collision(self):
    for powerup in self.powerups:
        if p_collided := pygame.sprite.groupcollide(
            self.ship_,
            powerup,
            dokilla=False,
            dokillb=True,
            collided=pygame.sprite.collide_mask,
        ):
            give_ship_powerups(self, p_collided.values())



    if self.ship.immunity:
        if pygame.sprite.groupcollide(self.ship_shield_, self.e_projectiles, False, dokillb= True, collided= pygame.sprite.collide_mask):
            print("collision blocked")

    elif pygame.sprite.groupcollide(self.ship_, self.e_projectiles, False, dokillb= True, collided= pygame.sprite.collide_mask):
        self.ship.lives -= 1
        print("collision detected")






