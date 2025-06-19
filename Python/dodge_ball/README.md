# 🎮 Dodge Game - 공 피하기 게임

PyGame을 활용한 간단한 공 피하기 형식의 게임입니다.  
하늘에서 떨어지는 고양이(공)를 피해 좌우로 움직이며 최대한 오래 살아남으세요!

![](../../docs/dodge_ball/oiiaii.gif)

## 📌 주요 기능

- 방향키 좌우 키로 플레이어 이동
- 난이도 증가 (3초마다 고양이 수 증가)
- 점수 시스템 및 최고 기록 표시
- 일정 조건에서 **춤추는 큰 고양이 등장**
- 큰 고양이 프레임에 따라 **낙하 정지 or 빠른 낙하**
- 큰 고양이 상태에 따라 **mode 사운드 자동 재생**
- 충돌 시 `GAME OVER` 메시지 출력 및 점수 표시

---

## ⚙️ 설치 및 실행 방법

### 1. 가상환경(권장) 설정

    # 폴더 이동
    cd dodge-game

    # 가상환경 생성 (윈도우 기준)
    python -m venv venv

    # 가상환경 활성화
    venv\Scripts\activate

    # macOS/Linux 사용자의 경우
    source venv/bin/activate

### 2. 필요한 라이브러리 설치

    pip install pygame

### 3. ▶️ 게임 실행

    python main.py

---

## 📁 폴더 구조

    dodge-game/
    ├── main.py              # 메인 루프 실행
    ├── player.py            # 플레이어 클래스
    ├── ball.py              # 공 클래스
    ├── sound.py             # 효과음 로딩 및 재생
    ├── config.py            # 설정 상수 (색상, 크기 등)
    ├── utils.py             # 공통 유틸 (충돌 검사 등)
    ├── sounds/              # 효과음 폴더
    ├── images/              # 고양이 공 프레임 이미지들
    └── README.md

---

## 🎵 사운드 파일 참고

- ball1.wav ~ ball5.wav: 공 생성 시 랜덤 효과음
- mode1.wav, mode2.wav: 특정 고양이 프레임에서 재생
- death.wav, highscore.wav: 충돌/신기록 발생 시 효과음

> 이미지는 images/ 폴더에 cat_ball_0.png ~ cat_ball_93.png 순서대로 있어야 합니다.

> 사운드는 sounds/ 폴더에 WAV 형식으로 준비되어 있어야 합니다.
