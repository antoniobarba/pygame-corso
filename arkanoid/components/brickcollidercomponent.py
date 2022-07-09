from engine.components import ColliderComponent
from pygame.rect import Rect

class BrickColliderComponent(ColliderComponent):
    

    def onCollision(self, otherCollider):
        self.owner.destroy()
        