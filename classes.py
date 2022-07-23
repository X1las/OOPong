from abc import abstractmethod
import pygame,sys

from settings import BALLSIZE, PADDLESIZE, RESOLUTION, TITLE

class GraphicsObj:

    contains = []

    def add(self,obj):
        self.contains.append(obj)
    
    # Update function that updates objects the object contains
    def update(self):
        for i in self.contains:
            i.update()

    # Draw function that draws objects it contains
    def draw(self):
        for i in self.contains:
            i.draw()


class Ball(GraphicsObj):
    
    def __init__(self,parent, size = BALLSIZE):
        self.parent = parent
        self.size = size

        if parent:
            parent.add(self)

    def update():
        super().update()

    def draw():
        super().draw()

class Paddle(GraphicsObj):
    
    def __init__(self,parent, size = PADDLESIZE):
        self.parent = parent
        self.size = size

        if parent:
            parent.add(self)

    def update():
        super().update()

    def draw():
        super().draw()

class Game(GraphicsObj):
    
    def __init__(self, running = True):
        pygame.init()

        self.running = running
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(RESOLUTION)
        
        pygame.display.set_caption(TITLE)

        if running:
            self.run()
        
    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        super().update()

    def draw(self):
        super().draw()
        pygame.display.flip()
        self.clock.tick(60)

    def run(self):
        print("starting game...")

        while self.running:
            self.update()
            self.draw()

