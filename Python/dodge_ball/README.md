# 🎮 Dodge Game - 공 피하기 게임

PyGame을 활용한 간단한 공 피하기 게임입니다.  
하늘에서 떨어지는 공을 피해 좌우로 움직이며 최대한 오래 살아남으세요!

## 📌 주요 기능

- 방향키 좌우 키로 플레이어 이동
- 공이 점점 많아지는 난이도 증가
- 충돌 시 GAME OVER 메시지 출력
- 점수 시스템 및 최고 기록 표시

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

    python dodge_game.py

---

## 📁 폴더 구조

    dodge-game
    ├── dodge_game.py          # 메인 게임 파일
    ├── sounds                # 효과음 폴더
    │   ├── death.wav
    │   ├── highscore.wav
    │   └── ball1.wav ~ ball5.wav
    └── README.md

---
