import pygame.locals
from engine.component import Component

class PlayerMovementComponent(Component):

    DIR_UP = 0
    DIR_DOWN = 1
    DIR_LEFT = 2
    DIR_RIGHT = 3
    DIR_STILL = 4

    def __init__(self):
        super().__init__()
        self.speed = 100
        self.gridSize = 50
        self.gridSnapThreshold = 2
        self.direction = self.DIR_STILL
        self.desiredDirection = self.DIR_STILL

        from engine import Engine
        
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_LEFT, self.leftPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_RIGHT, self.rightPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_UP, self.upPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_DOWN, self.downPressed)

    def leftPressed(self, key):
        self.desiredDirection = self.DIR_LEFT

    def rightPressed(self, key):
        self.desiredDirection = self.DIR_RIGHT
    
    def upPressed(self, key):
        self.desiredDirection = self.DIR_UP
    
    def downPressed(self, key):
        self.desiredDirection = self.DIR_DOWN

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        self.speed = descriptor["speed"]

    def update(self, deltaTime):
        pass
        # update position

        # check if near to grid snap point

        # if it is, and the desiredDirection is different from direction
            # snap and change direction

    
        