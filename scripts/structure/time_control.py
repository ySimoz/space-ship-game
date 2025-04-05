import pygame


def time_frame_control(self):
    self.clock.tick(60)
    current_tick = pygame.time.get_ticks()  # Get the current time
    self.time_elapsed = current_tick - self.last_tick  # Calculate the time elapsed since the last frame
    self.last_tick = current_tick  # Update the last tick for the next frame


# method for updating the timer by passing the current ticks and the ticks of the previous call
# update the rendered text to blit
def update_timer(self):
    color = (255, 255, 255)
    if self.active_timer:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= self.timer_interval:
            self.timer -= 1
            self.timer = max(self.timer, 0)
            self.last_time = current_time
            self.timer_text = self.timer_font.render(
                f"{format_time(self.timer)}", True, color
            )
                    # Blit timer onto the screen
    self.screen.blit(self.timer_text, self.timer_rect)


# convert the time passed in seconds to formatted text in seconds and minutes
def format_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    return '{:02d}:{:02d}'.format(minutes, seconds)
