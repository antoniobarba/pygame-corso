from ..actor import Actor


# Right now we don't have special things in this class, i need this class only for loading and saving purpose.
class BaseActor(Actor):
    pass

    @staticmethod
    def loadFromDict(actorDescriptor):
        actor = BaseActor()
        actor.name = actorDescriptor["name"]
        actor.x = actorDescriptor["x"]
        actor.y = actorDescriptor["y"]

        # Loading each component in the actor
        from ..component import Component

        for componentDescriptor in actorDescriptor["components"]:
            component = Component.loadFromDict(componentDescriptor)
            actor.addComponent(component)

        return actor

    def saveToDict(self):
        savedict = super().saveToDict()
        components_dict = []
        for component in self.components:
            components_dict.append(component.saveToDict())
        savedict["components"] = components_dict
        return savedict
