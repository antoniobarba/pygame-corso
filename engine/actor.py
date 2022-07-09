from .component import Component

class Actor:

    def __init__(self, scene):
        self.components = []
        self.x = 0
        self.y = 0
        self.name = ""
        self.scene = scene

    def loadFromDescriptor(self, descriptor):
        self.name = descriptor["name"]
        self.x = descriptor["x"]
        self.y = descriptor["y"]
        
        for componentDescriptor in descriptor["components"]:
            component = Component.staticCreateFromDescriptor(componentDescriptor)
            if component is not None:
                self.addComponent(component)

    def load(self):
        for a in self.components:
            a.load()

    def render(self, surface):
        for a in self.components:
            a.render(surface)

    # There will be timing involved
    def update(self, deltaTime):
        for a in self.components:
            a.update(deltaTime)
            
    def addComponent(self, component):
        self.components.append(component)
        component.setOwner(self)

