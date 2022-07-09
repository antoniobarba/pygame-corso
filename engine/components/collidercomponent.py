from ..component import Component
from pygame.rect import Rect

class ColliderComponent(Component):

    def __init__(self):
        super().__init__()
        self.AABB = Rect(0,0,0,0)

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        rd = descriptor["AABB"]
        self.AABB = Rect(rd["x"], rd["y"], rd["width"], rd["height"])


    def load(self):
        from engine import Engine
        e = Engine()
        e.collisionSystem.registerCollider(self)

    def update(self, deltaTime):
        self.AABB.x = self.owner.x
        self.AABB.y = self.owner.y

    def onCollision(self, otherCollider):
        print(f"{self.name} Colliding with {otherCollider.name}")
        

    