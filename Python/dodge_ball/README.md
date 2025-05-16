# 🎮 Dodge Game - 공 피하기 게임

PyGame을 활용한 간단한 공 피하기 게임입니다.  
하늘에서 떨어지는 공을 피해 좌우로 움직이며 최대한 오래 살아남으세요!

## 📌 주요 기능

- 방향키 좌우 키로 플레이어 이동
- 난이도 증가 (3초마다 공 하나씩 추가)
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
    │   ├── death.wav
    │   ├── highscore.wav
    │   ├── ball1.wav
    │   ├── ball2.wav
    │   ├── ball3.wav
    │   ├── ball4.wav
    │   └── ball5.wav
    └── README.md

---
