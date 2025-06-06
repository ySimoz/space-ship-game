import pygame
from scripts.structure import time_control
from scripts.structure.handle_events import *
from scripts.structure.time_control import *
from scripts.game_states.game_states import *

def fadeout_surface(surface, alpha):
    fade = pygame.Surface(surface.get_size()).convert_alpha()
    fade.fill((0, 0, 0, alpha))
    surface.blit(fade, (0, 0))

def game_over_animation(self):
    running = True
    # Fade out everything on the screen
    fade_duration = 1000  # ms
    fade_start = pygame.time.get_ticks()
    while True:
        now = pygame.time.get_ticks()
        elapsed = now - fade_start
        alpha = min(255, int(255 * (elapsed / fade_duration)))
        self.screen.blit(self.last_gameplay_surface, (0, 0))
        fadeout_surface(self.screen, alpha)
        pygame.display.flip()
        if elapsed >= fade_duration:
            break
        self.clock.tick(60)
    # Game over text animation
    game_over_anim_start = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.quit_game()
        # Move the "Game" text
        if self.game_over_animation_game_x < self.game_over_animation_game_end_x:
            self.game_over_animation_game_x += self.game_over_animation_speed
        # Move the "Over" text from the right
        if self.game_over_animation_over_x > self.game_over_animation_over_end_x:
            self.game_over_animation_over_x -= self.game_over_animation_speed
        # Draw
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_over_animation_game_text, (self.game_over_animation_game_x, self.game_over_animation_game_y))
        self.screen.blit(self.game_over_animation_over_text, (self.game_over_animation_over_x, self.game_over_animation_over_y))
        pygame.display.flip()
        # Check if both texts have reached their destinations
        if self.game_over_animation_game_x >= self.game_over_animation_game_end_x and self.game_over_animation_over_x <= self.game_over_animation_over_end_x:
            running = False
        self.clock.tick(300)

def game_over_state(self):
    # Wait for ship explosion to finish (1 second)
    explosion_duration = 1000  # ms
    while pygame.time.get_ticks() - getattr(self, 'ship_exploded_time', 0) < explosion_duration:
        # Draw the last gameplay frame (with ship exploded)
        self.last_gameplay_surface = self.screen.copy()
        pygame.display.flip()
        self.clock.tick(60)
    game_over_animation(self)
    while self.game_over_running_state:
        handle_events(self)
        time_frame_control(self)
