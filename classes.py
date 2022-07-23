import pygame,sys

from settings import RESOLUTION, TITLE


class Ball:
    pass

class Paddle:
    pass

class Game:
    
    contains = []

    def __init__(self, running = True):
        pygame.init()

        self.running = running
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(RESOLUTION)
        
        pygame.display.set_caption(TITLE)

        if running:
            self.run()
        
    # Function that updates the code and objects of the game class
    def update(self):

        # Put game updates here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Updates the objects it contains
        for i in self.contains:
            i.update()

    # Function that draws objects and things within the game class
    def draw(self):

        # Put game draw stuff here

        # Draws the objects the game class contains
        for i in self.contains:
            i.update()

        pygame.display.flip()
        self.clock.tick(60)

    def run(self):
        print("starting game...")

        while self.running:
            self.update()
            self.draw()

