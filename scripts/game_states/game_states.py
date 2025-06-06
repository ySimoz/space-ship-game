import pygame
from scripts.game_states import game_over_state
from scripts.game_states.initial_state import *
from scripts.game_states.gameplay_state import *

def setup_states(self):
    self.INITIAL_STATE = 0
    self.GAMEPLAY_STATE = 1
    self.GAME_OVER_STATE = 2
    self.current_state = self.INITIAL_STATE

def states_running_state(self):
    self.initial_running_state = True
    self.gameplay_running_state = False
    self.game_over_running_state = False

def change_state(self, state):
    self.current_state = state


def run_states(self):
    if self.current_state is self.INITIAL_STATE:
        initial_state(self)
    elif self.current_state is self.GAMEPLAY_STATE:
        gameplay_state(self)
    elif self.current_state is self.GAME_OVER_STATE:
        game_over_state.game_over_state(self)