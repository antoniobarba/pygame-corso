from .component import Component
import pygame

class ColliderComponent(Component):

    def __init__(self, name, actor, AABB):
        super().__init__(name, actor)
        self.AABB = AABB

    def load(self):
        from .engine import Engine
        e = Engine()
        e.collisionSystem.registerCollider(self)

    def update(self, deltaTime):
        self.AABB.x = self.owner.x
        self.AABB.y = self.owner.y

    def onCollision(self, otherCollider):
        print(f"{self.name} Colliding with {otherCollider.name}")
        

    