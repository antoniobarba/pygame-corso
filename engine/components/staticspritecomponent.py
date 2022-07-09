from ..component import Component
import pygame

class StaticSpriteComponent(Component):
    def __init__(self):
        super().__init__()
        self.assetFileName = ""
        self.image = None

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        self.assetFileName = descriptor["fileName"]

    def load(self):
        self.image = pygame.image.load(self.assetFileName)

    def onDestroyed(self):
        self.image = None

    def render(self, surface):
        rect = self.image.get_rect()
        rect.x = self.owner.x
        rect.y = self.owner.y
        surface.blit(self.image, rect)


