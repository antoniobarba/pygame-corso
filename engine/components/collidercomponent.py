from ..component import Component
from pygame.rect import Rect

class ColliderComponent(Component):

    def __init__(self):
        super().__init__()
        self.AABB = Rect(0,0,0,0)
        self.originalAABB = Rect(0,0,0,0)

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        rd = descriptor["AABB"]
        self.AABB = Rect(rd["x"], rd["y"], rd["width"], rd["height"])
        self.originalAABB = Rect(rd["x"], rd["y"], rd["width"], rd["height"])

    def load(self):
        super().load()
        from engine import Engine
        self.collisionSystem = Engine().collisionSystem
        self.collisionSystem.registerCollider(self)
        self.update(0)

    def onDestroyed(self):
        self.collisionSystem.deregisterCollider(self)
        super().onDestroyed()

    def update(self, deltaTime):
        self.AABB.x = self.originalAABB.x + self.owner.x 
        self.AABB.y = self.originalAABB.y + self.owner.y

    def onCollision(self, otherCollider):
        pass
        

    