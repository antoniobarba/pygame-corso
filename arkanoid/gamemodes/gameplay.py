from engine.gamemode import GameMode

class GamePlay(GameMode):

    def __init__(self):
        self.startingLives = 0
        self.lives = 0
        self.engine = None

    def ballDropped(self):
        self.lives -= 1

    def loadFromDescriptor(self, descriptor):
        self.startingLives = descriptor["lives"]

    def load(self):
        from engine import Engine
        self.engine = Engine()
        self.reset()

    def reset(self):
        self.lives = self.startingLives

    def update(self, deltaTime):
        brick = self.scene.findActor("brick")

        if brick is None:
            # there are no more bricks in the scene, you win!
            self.engine.loadScene("arkanoid/levels/start.json")

        if self.lives <= 0:
            self.engine.loadScene("arkanoid/levels/lost.json")

    

        