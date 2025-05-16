# config.py

import pygame

# 화면 설정
WIDTH, HEIGHT = 480, 640

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)

# 플레이어 설정
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 10
PLAYER_SPEED = 7

# 공 설정
BALL_RADIUS = 15
INITIAL_BALL_SPEED = 3
BALL_ADD_INTERVAL = 3

# 폰트
pygame.font.init()
BIG_FONT = pygame.font.SysFont(None, 60)
FONT = pygame.font.SysFont(None, 36)
SMALL_FONT = pygame.font.SysFont(None, 24)
TINY_FONT = pygame.font.SysFont(None, 18)
