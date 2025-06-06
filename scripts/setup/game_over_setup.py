import pygame

def game_over_animation_setup(self):
    self.game_over_animation_font_bold = pygame.font.SysFont('Honeymoon', int(self.screen.get_height() * 0.22))
    self.game_over_animation_font_bold.set_bold(True)
    # Dynamically scale text to fit window width
    game_text = "Game"
    over_text = "Over"
    # Render once to get size
    temp_game_surface = self.game_over_animation_font_bold.render(game_text, True, (0, 255, 0))  # Green
    temp_over_surface = self.game_over_animation_font_bold.render(over_text, True, (255, 255, 255))
    # Calculate scale factors
    max_text_width = int(self.screen.get_width() * 0.7)
    scale_game = min(1.0, max_text_width / temp_game_surface.get_width())
    scale_over = min(1.0, max_text_width / temp_over_surface.get_width())
    # Rescale surfaces
    game_size = (int(temp_game_surface.get_width() * scale_game), int(temp_game_surface.get_height() * scale_game))
    over_size = (int(temp_over_surface.get_width() * scale_over), int(temp_over_surface.get_height() * scale_over))
    self.game_over_animation_game_text = pygame.transform.smoothscale(temp_game_surface, game_size)
    self.game_over_animation_over_text = pygame.transform.smoothscale(temp_over_surface, over_size)
    # Position: 'Game' upper, 'Over' lower
    center_x = self.screen.get_width() // 2
    game_y = self.screen.get_height() // 2 - game_size[1] - 20
    over_y = self.screen.get_height() // 2 + 20
    self.game_over_animation_game_x, self.game_over_animation_game_y = -game_size[0], game_y
    self.game_over_animation_over_x, self.game_over_animation_over_y = self.screen.get_width(), over_y
    self.game_over_animation_game_end_x = center_x - game_size[0] // 2
    self.game_over_animation_over_end_x = center_x - over_size[0] // 2
    self.game_over_animation_speed = max(1, int(self.screen.get_width() * 0.003))