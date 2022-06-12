class Scene:
    def __init__(self, name):
        # there will be actors acting things
        self.actors = []
        self.name = name

    def load(self):
        for a in self.actors:
            a.load()

    def render(self, surface):
        for a in self.actors:
            a.render(surface)

    # There will be timing involved
    def update(self):
        for a in self.actors:
            a.update()
