# sound.py

import pygame
import os
import random

class SoundManager:
    def __init__(self, folder="sounds"):
        self.death = pygame.mixer.Sound(os.path.join(folder, "death.wav"))
        self.death.set_volume(0.2)

        self.highscore = pygame.mixer.Sound(os.path.join(folder, "highscore.wav"))
        self.highscore.set_volume(0.4)

        self.ball_sounds = []
        for i in range(1, 6):
            sound = pygame.mixer.Sound(os.path.join(folder, f"ball{i}.wav"))
            sound.set_volume(1.0)
            self.ball_sounds.append(sound)

    def play_death(self):
        self.death.play()

    def play_highscore(self):
        self.highscore.play()

    def play_random_ball(self):
        random.choice(self.ball_sounds).play()