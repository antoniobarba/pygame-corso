from engine.actor import Actor
import pygame.locals

class Ball(Actor):
    def __init__(self, scene):
        super().__init__(scene)
        self.resting = True

    def reset(self):
        self.resting = True
        self.x = self.originalX
        self.y = self.originalY

    def load(self):
        super().load()
        from engine import Engine
        engine = Engine()
        self.player = engine.scene.findActor("Player")
        engine.inputSystem.bindToKeyboard(pygame.locals.K_SPACE, self.launch, True)
        self.originalX = self.x
        self.originalY = self.y

    def update(self, deltaTime):
        super().update(deltaTime)

        if self.resting:
            self.x = self.player.x
            self.y = self.player.y - 6

    def launch(self, key):
        self.resting = False
    