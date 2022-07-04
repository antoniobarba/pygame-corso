# This class contain the logic for bouncing an image in the window
from engine.component import Component


class BouncingObject(Component):
    def __init__(self, image, boundingRect):
        super().__init__()
        self.image = image
        self.x = 0
        self.y = 0
        self.vx = 0.5
        self.vy = 0.5
        self.boundingRect = boundingRect

    def render(self, surface):
        rect = self.image.get_rect()
        rect.centerx = self.x
        rect.centery = self.y
        surface.blit(self.image, rect)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # bounce on the x axis
        if self.x < 0 or self.x > self.boundingRect.width:
            self.vx = -self.vx

        # bounce on the y axis
        if self.y < 0 or self.y > self.boundingRect.height:
            self.vy = -self.vy
