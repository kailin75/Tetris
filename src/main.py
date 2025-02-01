from settings import *
from sys import exit

class Main:
    def __init__(self):

        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # exit everything
                    exit()

            # display
            self.display_surface.fill(background)

            # update game
            pygame.display.update()
            self.clock.tick()

# only run main.py
if __name__ == '__main__':
    main = Main()
    main.run()
