import pygame
import random
import os
from config import BALL_RADIUS, WIDTH

class Ball:
    def __init__(self, speed, animated=False, sound=None):
        self.y = -BALL_RADIUS
        self.speed = speed
        self.animated = animated
        self.sound = sound
        self.created_at = pygame.time.get_ticks()

        self.frames = []

        # ✅ 먼저 scale_factor와 size를 설정하여 이미지 크기 계산
        if self.animated:
            scale_factor = 5.5  # 큰 고양이는 더 큼
        else:
            scale_factor = 1.5  # 일반 고양이 사이즈

        size = int(BALL_RADIUS * 2 * scale_factor)
        half_width = size // 2

        # ✅ 이미지 크기에 맞춰 X 위치 제한 (화면 밖으로 안 나가도록)
        self.x = random.randint(half_width, WIDTH - half_width)

        if self.animated:
            for i in range(94):
                path = os.path.join("images", f"cat_ball_{i}.png")
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, (size, size))
                self.frames.append(img)

            self.current_frame = random.randint(0, len(self.frames) - 1)
            self.last_frame_time = pygame.time.get_ticks()
            self.frame_interval = 100
            self.wild_sfx_played = False
        else:
            path = os.path.join("images", "cat_ball_0.png")
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (size, size))
            self.frames.append(img)
            self.current_frame = 0
            self.wild_sfx_played = False

        self.last_mode = "calm"

    def get_mode(self):
        if not self.animated:
            return "calm"
        if 0 <= self.current_frame <= 26 or 85 <= self.current_frame <= 93:
            return "calm"
        return "wild"

    def update(self):
        if self.animated:
            mode = self.get_mode()

            if mode == "wild":
                self.speed = 10
                self.frame_interval = 50
                if not self.wild_sfx_played and self.sound:
                    self.sound.play_random_mode()
                    self.wild_sfx_played = True
            else:
                self.speed = 0
                self.frame_interval = 120

            self.last_mode = mode

        self.y += self.speed

        if self.animated:
            now = pygame.time.get_ticks()
            if now - self.last_frame_time > self.frame_interval:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.last_frame_time = now

    def is_off_screen(self, height):
        return self.y > height

    def get_rect(self):
        img = self.frames[self.current_frame]
        if self.animated:
            offset_x = 52
            offset_y = 62
            shift_left = 5
        else:
            offset_x = 12
            offset_y = 15
            shift_left = 2

        width = img.get_width() - 2 * offset_x
        height = img.get_height() - 2 * offset_y
        return pygame.Rect(self.x + offset_x - shift_left, self.y + offset_y, width, height)

    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], (self.x, self.y))
        # pygame.draw.rect(screen, (0, 255, 0), self.get_rect(), 2) # 디버깅 용 충돌범위 표기
