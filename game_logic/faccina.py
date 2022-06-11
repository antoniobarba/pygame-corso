import pygame
from engine.actor import Actor


class Faccina(Actor):
    def __init__(self):
        super().__init__()
        self.assetFileName = "faccina.png"

    def load(self):
        self.image = pygame.image.load(self.assetFileName)


if __name__ == "__main__":
    test = Faccina()
    print(test.assetFileName, test.components)
