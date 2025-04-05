import pygame
import sys


def handle_events(self):  # handle the events inside the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:  # Correctly handle K_SPACE
                self.movement_state = not self.movement_state
            else:
                handle_keydown(self, event)
        elif event.type == pygame.KEYUP:
            handle_keyup(self, event)


def handle_keydown(self, event):  # press keys movement control
    keys = event.key
    
    if self.current_state is self.INITIAL_STATE:
        if keys == pygame.K_SPACE:
            self.initial_running_state = False
            self.gameplay_running_state = True
            self.current_state = self.GAMEPLAY_STATE
            
    elif self.current_state is self.GAMEPLAY_STATE:
        if self.movement_state:  # movement condition
            if keys == pygame.K_w:
                self.movement[0] = True
            elif keys == pygame.K_s:
                self.movement[1] = True
            elif keys == pygame.K_a:
                self.movement[2] = True
            elif keys == pygame.K_d:
                self.movement[3] = True

        if keys == pygame.K_r and not self.space_press_state:  # condition for the ship to not shoot
            self.r_key_press_state = True
            self.recharge_initial_time = pygame.time.get_ticks()


        if keys == pygame.K_SPACE:  # key for controlling tne shooting of the ship
            self.space_press_state = True
            self.r_key_press_state = False  # turn on automatic shooting while pressing


def handle_keyup(self, event):  # release keys movement control
    keys = event.key
    
    if self.current_state is self.GAMEPLAY_STATE:
        if self.movement_state:  # movement condition
            if keys == pygame.K_w:
                self.movement[0] = False
            elif keys == pygame.K_s:
                self.movement[1] = False
            elif keys == pygame.K_a:
                self.movement[2] = False
            elif keys == pygame.K_d:
                self.movement[3] = False
        if keys == pygame.K_SPACE:  # key for controlling tne shooting of the ship
            self.space_press_state = False  # turn off automatic shooting

        if keys == pygame.K_r and not self.space_press_state:  # condition for the ship to not shoot
            self.r_key_press_state = False

