import pygame
from scripts.structure.handle_events import *
from scripts.structure.time_control import *
from scripts.game_states.game_states import *

def initial_state(self):
    while self.initial_running_state:
        handle_events(self)
        self.screen.blit(self.initial_menu_writing_surface, self.initial_menu_writing_position)
        pygame.display.flip()
    


    