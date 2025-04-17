# 🎯 Number Guess Game

> **ArrayList**와 **Thread**를 활용한 숫자 추측 게임

---

## 📌 게임 개요

- 3개의 숫자를 추첨하여, **플레이어가 5번 안에 맞추는 게임**
- **동시성**을 고려하여 각 플레이어는 **스레드(Thread)** 로 처리됨
- 각 플레이어는 **ArrayList**를 통해 추측해야 할 숫자 목록을 관리함

---

## 🧠 사용된 개념

### 1. ArrayList

- `Player` 클래스에서 `targetNumbers`는 `ArrayList<Integer>`로 선언됨
- 정답을 맞췄을 때 `removeFromTargetNumbers()`로 제거됨

### 2. Thread (스레드)

- `Player` 클래스는 `Runnable`을 구현함
- `run()` 메서드를 통해 각 플레이어는 **동시에 숫자를 추측**함
- `GuessGame` 클래스는 스레드를 생성해 플레이어 차례를 병렬로 진행

---

## 🧱 주요 클래스 설명

### 🔹 Player.java

- 플레이어 정보를 담는 클래스 (ID, 점수, 정답 목록 등)
- 주요 메서드:
  - `makeGuess()` : 숫자 추측
  - `checkGuess(int guess)` : 정답 여부 판단
  - `increaseScore()` : 점수 +1
  - `removeFromTargetNumbers(int number)` : 맞춘 숫자 제거
  - `run()` : 플레이어의 차례 진행

### 🔹 GuessGame.java

- 게임 진행을 담당하는 클래스
- 플레이어 초기화, 게임 루프 처리
- 승리 조건: 플레이어 중 누군가 **모든 숫자 정답 시 종료**

### 🔹 GameLauncher.java

- 메인 실행 클래스
- `GuessGame` 인스턴스를 만들어 `startGame()` 호출

---

## ▶️ 실행 방법

```bash
# 경로: src/ 디렉토리 기준에서
cd src
javac numberGame/*.java
java numberGame.GameLauncher
```

---

## 🖥️ 실행 화면 예시 (터미널 출력)

```
플레이어 1가 게임을 시작합니다.
플레이어 2가 게임을 시작합니다.
플레이어 3가 게임을 시작합니다.
플레이어 1: 3
플레이어 1이(가) 정답을 틀렸습니다.
플레이어 2: 5
플레이어 2이(가) 정답을 맞췄습니다.
...
플레이어 2이(가) 3개의 숫자를 모두 맞췄습니다! 우승입니다!
```

---

## ✨ 프로젝트 목적

이 프로젝트는 Java에서의 **동시성(Thread)**, **자료구조(ArrayList)**, **게임 로직 구성 능력**을 실습하기 위한 **사이드 프로젝트**입니다.  
Java의 기초 문법을 익힌 후 객체지향적 설계와 스레드 활용 능력을 강화하는 데 중점을 두었습니다.

---

## 📁 디렉토리 구조

```
NumberGuessGame/
├── .gitignore
├── README.md
└── src/
    └── numberGame/
        ├── GameLauncher.java
        ├── GuessGame.java
        └── Player.java
```

---

## 👨‍💻 개발자

- **Woojin Jeon (Joycong)**  
  GitHub: [github.com/Joycong](https://github.com/Joycong)
