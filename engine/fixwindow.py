from engine.scene import Scene
import pygame


class FixWindow(Scene):
    def init(self):
        super.__init__()
        self.window = None

    def load(self):
        self.window = pygame.display.set_mode((800, 600), 0, 32)
        for a in self.actors:
            a.load()
