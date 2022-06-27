import json
from engine.scene import *


class SceneFactory:
    @staticmethod
    def newLoadSceneFromFile(filename):
        with open(filename, "r") as f:
            sceneDescriptor = json.load(f)

            # Loading the main scene
            scene = Scene()
            scene.loadFromDict(sceneDescriptor)

        # Returning the whole loaded scene
        return scene

    @staticmethod
    def newSaveSceneToFile(scene, fileName):
        with open(fileName, "w") as f:
            savedict = scene.saveToDict()
            json.dump(savedict, f, indent=6)
