# ball.py

import pygame
import random
from config import BALL_RADIUS, WIDTH
import os

class Ball:
    def __init__(self, speed):
        self.x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        self.y = -BALL_RADIUS
        self.speed = speed
        image_path = os.path.join("images", "oiia_cat.gif")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (BALL_RADIUS * 2, BALL_RADIUS * 2))

    def update(self):
        self.y += self.speed

    def is_off_screen(self, height):
        return self.y > height

    def get_rect(self):
        offset_x = 6  # 이미지 바깥쪽 여백
        offset_y = 5
        width = self.image.get_width() - 2 * offset_x
        height = self.image.get_height() - 2 * offset_y
        return pygame.Rect(self.x + offset_x, self.y + offset_y, width, height)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        # 충돌범위 확인
        pygame.draw.rect(screen, (0, 255, 0), self.get_rect(), 2)  # 녹색 충돌 박스 그리기

