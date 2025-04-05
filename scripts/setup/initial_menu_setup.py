import pygame

def initial_menu_setup(self):
    self.initial_menu_writing = 'Press Space'
    self.initial_menu_font = pygame.font.SysFont('Rockwell', 80)
    self.initial_menu_writing_surface = self.initial_menu_font.render(self.initial_menu_writing, True, (0,255,0))
    self.initial_menu_writing_position = (300 - self.initial_menu_writing_surface.get_width() / 2, 425 - self.initial_menu_writing_surface.get_height() / 2)
    

def gameplay_start_animation_setup(self):
    self.gsa_font = pygame.font.SysFont('Rockwell', 80)
    self.gsa_writing_position = (280,380)