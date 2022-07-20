from engine.actor import Actor
import pygame

class TestActor(Actor):

    def __init__(self, scene):
        super().__init__(scene)
        self.started = False
        # self.sfx = pygame.mixer.Sound("pacman/assets/sfx/bell.wav")

    def update(self, deltaTime):
        '''if not self.started:
            import engine
            e = engine.Engine()
            e.soundSystem.play(self.sfx, e.soundSystem.PLAYER_CHANNEL)
            self.started = True'''
        
        