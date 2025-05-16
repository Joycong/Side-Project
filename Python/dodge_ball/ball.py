# ball.py

import pygame
import random
from config import BALL_RADIUS, RED, WIDTH

class Ball:
    def __init__(self, speed):
        self.x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        self.y = -BALL_RADIUS
        self.radius = BALL_RADIUS
        self.speed = speed

    def update(self):
        self.y += self.speed

    def is_off_screen(self, height):
        return self.y > height

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)