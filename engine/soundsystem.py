import pygame

class SoundSystem:

    PLAYER_CHANNEL = 0
    GHOST_CHANNEL = 1
    OTHER_CHANNEL = 2

    def __init__(self):
        pygame.mixer.init()
        self.channels = [
                        pygame.mixer.Channel(self.PLAYER_CHANNEL),
                        pygame.mixer.Channel(self.GHOST_CHANNEL),
                        pygame.mixer.Channel(self.OTHER_CHANNEL)
                        ]

    def play(self, sound, channel):
        self.channels[channel].play(sound)

    def stop(self, channel):
        self.channels[channel].stop()
