from engine.component import Component
import pygame.locals
from pygame.rect import Rect

class PlayerMovementComponent(Component):
    def __init__(self):    
        from engine import Engine

        super().__init__()
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_LEFT, self.arrowPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_RIGHT, self.arrowPressed)

        self.vx = 0
        self.vy = 0
        self.speed = 0
        self.inertia = 0
        self.rect = Rect(0,0,0,0)
        self.AABB = Rect(0,0,0,0)

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        r = descriptor["AABB"]
        self.AABB = Rect(r["x"], r["y"], r["width"], r["height"])
        self.speed = descriptor["speed"]
        self.inertia = descriptor["inertia"]

    def load(self):
        from engine import Engine
        engine = Engine()
        self.rect = engine.window.get_rect()

    def update(self, deltaTime):
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime

        # inertia
        if self.vx > 0:
            self.vx = self.vx - self.inertia * deltaTime
        if self.vx < 0:
            self.vx = self.vx + self.inertia * deltaTime

        # bounds
        if self.owner.x < 0:
            self.owner.x = 0
            self.vx = 0
        if self.owner.x + self.AABB.width > self.rect.width:
            self.owner.x = self.rect.width - self.AABB.width
            self.vx = 0

    def arrowPressed(self, key):
        if key == pygame.locals.K_LEFT:
            self.vx = -self.speed
        if key == pygame.locals.K_RIGHT:
            self.vx = self.speed
    