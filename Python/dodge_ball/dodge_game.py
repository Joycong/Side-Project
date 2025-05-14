import pygame
import random
import time
import os

# 초기화
pygame.init()
pygame.mixer.init()

# 화면 크기
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("공 피하기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)

# 폰트 설정
big_font = pygame.font.SysFont(None, 60)
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)
tiny_font = pygame.font.SysFont(None, 18)

# 사운드 로드
sound_folder = "sounds"
death_sound = pygame.mixer.Sound(os.path.join(sound_folder, "death.wav"))
death_sound.set_volume(0.2) # 죽음 사운드 볼륨
highscore_sound = pygame.mixer.Sound(os.path.join(sound_folder, "highscore.wav"))
highscore_sound.set_volume(0.4)  # 점수 갱신 사운드 볼륨
ball_sounds = []
for i in range(1, 6):
    sound = pygame.mixer.Sound(os.path.join(sound_folder, f"ball{i}.wav"))
    sound.set_volume(1.0)  # 공 생성 사운드 볼륨
    ball_sounds.append(sound)

# 플레이어 설정
player_width = 50
player_height = 10
player_speed = 7

# 공 설정
ball_radius = 15
initial_ball_speed = 3
ball_add_interval = 3

# 시계
clock = pygame.time.Clock()

# 점수관련 변수
max_score = 0
show_new_high_score = False
high_score_time = 0


def reset_game():
    return {
        "player_x": WIDTH // 2 - player_width // 2,
        "player_y": HEIGHT - player_height - 10,
        "balls": [{"x": random.randint(ball_radius, WIDTH - ball_radius),
                   "y": random.randint(-300, -20)}],
        "ball_speed": initial_ball_speed,
        "start_time": time.time(),
        "score": 0,
        "last_ball_add_time": time.time(),
        "game_over": False,
        "has_shown_high_score": False
    }


def check_collision(player_rect, ball_rect):
    return player_rect.colliderect(ball_rect)


# 게임 초기 상태
state = reset_game()

running = True
while running:
    screen.fill(WHITE)
    now = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not state["game_over"]:
        if keys[pygame.K_LEFT] and state["player_x"] > 0:
            state["player_x"] -= player_speed
        if keys[pygame.K_RIGHT] and state["player_x"] < WIDTH - player_width:
            state["player_x"] += player_speed

        # 공 추가
        if now - state["last_ball_add_time"] > ball_add_interval:
            # 경과 시간 기반으로 공 누적 추가
            elapsed_time = int(now - state["start_time"])
            target_ball_count = 1 + (elapsed_time // ball_add_interval)

            while len(state["balls"]) < target_ball_count:
                new_ball = {"x": random.randint(ball_radius, WIDTH - ball_radius), "y": -ball_radius}
                state["balls"].append(new_ball)
                random.choice(ball_sounds).play()


        # 공 이동
        for ball in state["balls"]:
            ball["y"] += state["ball_speed"]

        # 공 제거 및 점수 증가
        state["balls"] = [b for b in state["balls"] if b["y"] < HEIGHT]
        state["score"] = int(now - state["start_time"])

        # 최대 점수 갱신
        if state["score"] > max_score:
            if not state["has_shown_high_score"]:
                show_new_high_score = True
                high_score_time = now
                state["has_shown_high_score"] = True
                highscore_sound.play()
            max_score = state["score"]

        # 충돌 검사
        player_rect = pygame.Rect(state["player_x"], state["player_y"], player_width, player_height)
        for ball in state["balls"]:
            ball_rect = pygame.Rect(ball["x"] - ball_radius, ball["y"] - ball_radius,
                                    ball_radius * 2, ball_radius * 2)
            if check_collision(player_rect, ball_rect):
                state["game_over"] = True
                death_sound.play()
                break

    else:
        if keys[pygame.K_r]:
            state = reset_game()

    # 플레이어 그리기
    pygame.draw.rect(screen, BLACK,
                     (state["player_x"], state["player_y"], player_width, player_height))

    # 공 그리기
    for ball in state["balls"]:
        pygame.draw.circle(screen, RED, (ball["x"], ball["y"]), ball_radius)

    # 점수 및 최대 점수 출력 (오른쪽 상단)
    score_text = font.render(f"Score: {state['score']}", True, BLACK)
    screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

    max_text = small_font.render(f"Max: {max_score}", True, GRAY)
    screen.blit(max_text, (WIDTH - max_text.get_width() - 10, 40))

    # New High Score 메시지
    if show_new_high_score and now - high_score_time < 2:
        new_high_text = small_font.render("New High Score!", True, YELLOW)
        screen.blit(new_high_text, (WIDTH - new_high_text.get_width() - 10, 70))
    elif now - high_score_time >= 2:
        show_new_high_score = False

    # 게임 오버 시 메시지
    if state["game_over"]:
        game_over_text = big_font.render("GAME OVER", True, RED)
        restart_text = small_font.render("Press R to Restart", True, GRAY)
        score_info_1 = small_font.render(f"Score: {state['score']}", True, BLACK)
        score_info_2 = small_font.render(f"Max: {max_score}", True, GRAY)

        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 2 - 40))
        screen.blit(score_info_1, ((WIDTH - score_info_1.get_width()) // 2, HEIGHT // 2 + 10))
        screen.blit(score_info_2, ((WIDTH - score_info_2.get_width()) // 2, HEIGHT // 2 + 30))
        screen.blit(restart_text, ((WIDTH - restart_text.get_width()) // 2, HEIGHT // 2 + 55))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
