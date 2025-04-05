from scripts.structure.time_control import *

def timer_setup(self):
    self.last_tick = pygame.time.get_ticks()  # variable for setup
    self.active_timer = True  # state of the timer
    self.timer_font = pygame.font.SysFont('Rockwell', 40)
    self.timer_position = (500, 32)  # position if the timer on the screen
    self.initial_time = 300  # 5 minutes in seconds
    self.timer_interval = 1000  # 1000 milliseconds = 1 second
    self.timer = self.initial_time  # values in milliseconds
    self.timer_text = self.timer_font.render(
        f"{format_time(self.timer)}", True, (255, 255, 255)
    )
    self.timer_rect = self.timer_text.get_rect(topleft=self.timer_position)  # timer position in the screen

    self.last_time = pygame.time.get_ticks()