# main.py

import pygame
import time
import random
from config import *
from player import Player
from ball import Ball
from sound import SoundManager
from utils import check_collision

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("공 피하기 게임")
clock = pygame.time.Clock()

player = Player()
sound = SoundManager()
balls = [Ball(INITIAL_BALL_SPEED)]

max_score = 0
show_new_high_score = False
high_score_time = 0

state = {
    "start_time": time.time(),
    "score": 0,
    "game_over": False,
    "has_shown_high_score": False
}

running = True
last_animated_time = time.time()  # 3초마다 애니메이션 고양이

while running:
    screen.fill(WHITE)
    now = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not state["game_over"]:
        player.move(keys)

        # 모드 판별: calm or wild
        is_any_wild = any(ball.get_mode() == "wild" for ball in balls)
        current_mode = "wild" if is_any_wild else "calm"

        # 음악 및 공 속도 설정
        if current_mode == "wild":
            current_speed = INITIAL_BALL_SPEED + 5 # 가속 설정
            sound.play_random_mode()
        else:
            current_speed = INITIAL_BALL_SPEED
            sound.stop_mode_sound()

        # 난이도 조절 (공 수 증가)
        elapsed = int(now - state["start_time"])
        target_ball_count = 1 + int((elapsed / BALL_ADD_INTERVAL) ** 0.7)  # 완화된 난이도

        while len(balls) < target_ball_count:
            animated = False
            if time.time() - last_animated_time >= 3:
                animated = True
                last_animated_time = time.time()

            if animated:
                speed = INITIAL_BALL_SPEED  # 큰 고양이: 속도는 update()에서 조절
            else:
                speed = random.randint(3, 6)  # 작은 고양이: 낙하 속도 랜덤

            new_ball = Ball(speed, animated=animated, sound=sound)

            balls.append(new_ball)

            # ✅ 새 공이 wild 모드이면 음악 재생
            if new_ball.get_mode() == "wild":
                sound.play_random_mode()

            # 공 생성 시 효과음
            sound.play_random_ball()
            if animated:
                sound.play_random_ball()

        # 공 이동
        for ball in balls:
            ball.update()

        # 공 제거
        balls = [b for b in balls if not b.is_off_screen(HEIGHT)]

        # 점수 계산
        state["score"] = int(now - state["start_time"])

        if state["score"] > max_score:
            if not state["has_shown_high_score"]:
                show_new_high_score = True
                high_score_time = now
                state["has_shown_high_score"] = True
                sound.play_highscore()
            max_score = state["score"]

        # 충돌 검사
        player_rect = player.get_rect()
        for ball in balls:
            if check_collision(player_rect, ball.get_rect()):
                state["game_over"] = True
                sound.play_death()
                break

    else:
        sound.stop_mode_sound()
        if keys[pygame.K_r]:
            player = Player()
            balls = [Ball(INITIAL_BALL_SPEED)]
            state = {
                "start_time": time.time(),
                "score": 0,
                "game_over": False,
                "has_shown_high_score": False
            }
            show_new_high_score = False

    # 그리기
    player.draw(screen)
    for ball in balls:
        ball.draw(screen)

    score_text = FONT.render(f"Score: {state['score']}", True, BLACK)
    screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

    max_text = SMALL_FONT.render(f"Max: {max_score}", True, GRAY)
    screen.blit(max_text, (WIDTH - max_text.get_width() - 10, 40))

    if show_new_high_score and now - high_score_time < 2:
        new_high = SMALL_FONT.render("New High Score!", True, YELLOW)
        screen.blit(new_high, (WIDTH - new_high.get_width() - 10, 70))
    elif now - high_score_time >= 2:
        show_new_high_score = False

    if state["game_over"]:
        game_over_text = BIG_FONT.render("GAME OVER", True, RED)
        restart_text = SMALL_FONT.render("Press R to Restart", True, GRAY)
        score_info_1 = SMALL_FONT.render(f"Score: {state['score']}", True, BLACK)
        score_info_2 = SMALL_FONT.render(f"Max: {max_score}", True, GRAY)

        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 2 - 40))
        screen.blit(score_info_1, ((WIDTH - score_info_1.get_width()) // 2, HEIGHT // 2 + 10))
        screen.blit(score_info_2, ((WIDTH - score_info_2.get_width()) // 2, HEIGHT // 2 + 30))
        screen.blit(restart_text, ((WIDTH - restart_text.get_width()) // 2, HEIGHT // 2 + 55))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
