// GuessGame.java
package numberGame;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class GuessGame {
    private int playerCount; // 플레이어 수
    private int targetCount; // 정답 개수
    private List<Player> players; // 플레이어 목록

    public GuessGame(int playerCount, int targetCount) {
        this.playerCount = playerCount;
        this.targetCount = targetCount;
        this.players = new ArrayList<>();
    }

    public void startGame() {
        List<Integer> targetNumbers = generateTargetNumbers(); // 정답 숫자 목록 생성

        // 플레이어 초기화
        for (int i = 1; i <= playerCount; i++) {
            Player player = new Player(i, new ArrayList<>(targetNumbers));
            players.add(player);
            player.start();
        }

        int turn = 1; // 현재 턴
        int maxTurns = 5; // 최대 턴 수
        boolean gameWon = false; // 게임 종료 여부

        // 게임 루프
        while (true) {
            gameWon = false;

            for (Player player : players) {
                System.out.print("플레이어 " + player.getPlayerId() + ": ");
                int guess = player.makeGuess(); // 플레이어의 추측 입력

                if (player.checkGuess(guess)) { // 추측한 숫자가 정답인 경우
                    player.increaseScore(); // 플레이어의 점수 증가
                    System.out.println("플레이어 " + player.getPlayerId() + "이(가) 정답을 맞췄습니다.");

                    player.removeFromTargetNumbers(guess); // 정답 처리 후 숫자 목록에서 제거

                    if (player.getScore() == targetCount) { // 플레이어가 모든 숫자를 맞춘 경우
                        System.out.println("플레이어 " + player.getPlayerId() + "이(가) " + targetCount + "개의 숫자를 모두 맞췄습니다! 우승입니다!");
                        gameWon = true; // 게임 종료 플래그 설정
                        break;
                    }
                } 
                else { // 추측한 숫자가 정답이 아닌 경우
                    System.out.println("플레이어 " + player.getPlayerId() + "이(가) 정답을 틀렸습니다.");
                }
            }

            if (gameWon || turn >= maxTurns) { // 게임 종료 조건 확인
                break;
            }

            turn++; // 턴 증가
        }

        if (gameWon) {
            System.out.println("게임 종료.");
        } else {
            System.out.println("5턴이 모두 종료되었습니다. 정답자가 없습니다.");
        }
    }

    private List<Integer> generateTargetNumbers() {
        List<Integer> numbers = new ArrayList<>();
        Random random = new Random();

        for (int i = 0; i < targetCount; i++) {
            int number = random.nextInt(9) + 1; // 1부터 9까지의 범위에서 랜덤한 숫자 생성
            numbers.add(number);
        }

        return numbers;
    }
}
