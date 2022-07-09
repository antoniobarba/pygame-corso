from pygame import rect
from .actor import Actor
import json

class Scene:

    def __init__(self):
        # there will be actors acting things
        self.actors = []
        self.windowRect = rect.Rect(0,0,0,0)
        self.title = ""

    def staticCreateFromFile(fileName):
        with open(fileName, "r") as f:
            try:
                # this is a dictionary
                sceneDescriptor = json.load(f)

                scene = Scene()
                scene.loadFromDescriptor(sceneDescriptor)

                return scene
                
            except Exception as e:
                print(f"Error on filename : {fileName}")
                print(str(e))

    def loadFromDescriptor(self, descriptor):
        windowDescriptor = descriptor["window"]
        self.windowRect.height = windowDescriptor["height"]
        self.windowRect.width = windowDescriptor["width"]
        self.title = windowDescriptor["title"]

        for actorDescriptor in descriptor["actors"]:
            actor = Actor(self)
            actor.loadFromDescriptor(actorDescriptor)

            self.actors.append(actor)

    def load(self):
        for a in self.actors:
            a.load()

    def render(self, surface):
        for a in self.actors:
            a.render(surface)

    def update(self, deltaTime):
        for a in self.actors:
            a.update(deltaTime)