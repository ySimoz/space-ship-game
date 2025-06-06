from main_import import *
from utils import resource_path  # Import the shared resource_path

WIDTH, HEIGHT = (600, 850)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("VadeSpace")
        icon_surface = pygame.image.load(resource_path("VadeSpace.ico"))
        pygame.display.set_icon(icon_surface)
        self.clock = pygame.time.Clock()  # internal clock
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # window setup
        self.running = True  # state of the main loop, set to True runs the program

        general_setup(self) # variables and objects setup)
        setup_states(self)
        states_running_state(self)

    # main function
    def main(self):
        #run through different state of the game
        while self.running:
            run_states(self)
            

if __name__ == "__main__":
    game1 = Game()
    game1.main()