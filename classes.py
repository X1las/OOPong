from email.policy import default
import pygame,sys

from settings import BALLSIZE, BGCOLOR, PADDLESIZE, RESOLUTION, TITLE

class RuntimeObj:

    pos = [0,0]
    contains = []
    parent = None

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


class Ball(RuntimeObj):
    
    def __init__(self,runtime, parent = None, size = BALLSIZE):
        self.parent = parent
        self.size = size
        self.runtime = runtime

        if parent:
            parent.add(self)
        
        if runtime:
            runtime.add(self)

        self.pos = [RESOLUTION[0]/2,RESOLUTION[1]/2]

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.runtime.screen)

class Paddle(RuntimeObj):
    
    def __init__(self,runtime, xstart, parent = None, ai = True, size = PADDLESIZE):
        self.parent = parent
        self.size = size
        self.runtime = runtime
        self.ai = ai

        if parent:
            parent.add(self)

        if runtime:
            runtime.add(self)
        
        self.pos = [xstart,RESOLUTION[1]/2]

    def update():
        pass

    def draw():
        pass

class Game(RuntimeObj):
    
    def __init__(self, running = True, gameState = "DEFAULT"):
        pygame.init()

        self.running = running
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(RESOLUTION)
        
        pygame.display.set_caption(TITLE)

        if running:
            self.run()

        if gameState == "DEFAULT":
            self.defaultStart()
        
    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        super().update()

    def draw(self):

        self.screen.fill(BGCOLOR)

        super().draw()
        pygame.display.flip()

        self.clock.tick(60)

    def run(self):
        print("starting game...")

        while self.running:
            self.update()
            self.draw()

    def defaultStart(self):
        self.contains[0] = Ball(self)
        self.contains[1] = Paddle(self, 5, ai = False)
        self.contains[2] = Paddle(self, RESOLUTION[0]-5-PADDLESIZE[0])
