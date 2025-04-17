// Player.java
package numberGame;

import java.util.List;
import java.util.Scanner;

public class Player implements Runnable {
    private int playerId; // 플레이어 ID
    private int score; // 플레이어의 점수
    private List<Integer> targetNumbers; // 맞춰야 할 숫자 목록

    public Player(int playerId, List<Integer> targetNumbers) {
        this.playerId = playerId;
        this.score = 0;
        this.targetNumbers = targetNumbers;
    }

    public void start() {
        System.out.println("플레이어 " + playerId + "가 게임을 시작합니다.");
    }

    public int getPlayerId() {
        return playerId;
    }

    public int getScore() {
        return score;
    }

    public synchronized void increaseScore() {
        score++; // 점수 증가
    }

    public int makeGuess() {
        Scanner scanner = new Scanner(System.in);
        return scanner.nextInt(); // 사용자로부터 추측한 숫자 입력
    }

    public boolean checkGuess(int guess) {
        return targetNumbers.contains(guess); // 추측한 숫자가 정답 숫자 목록에 포함되는지 확인
    }

    public void removeFromTargetNumbers(int guess) {
        targetNumbers.remove(Integer.valueOf(guess)); // 정답 처리 후 정답 숫자 목록에서 해당 숫자 제거
    }

    @Override
    public void run() {
        System.out.println("플레이어 " + playerId + "의 차례입니다.");
        System.out.print("플레이어 " + playerId + ": ");
        int guess = makeGuess(); // 숫자 추측 입력

        if (checkGuess(guess)) { // 추측한 숫자가 정답인 경우
            increaseScore(); // 점수 증가
            System.out.println("플레이어 " + playerId + "이(가) 정답을 맞췄습니다.");

            removeFromTargetNumbers(guess); // 정답 처리 후 숫자 목록에서 제거
        } else { // 추측한 숫자가 정답이 아닌 경우
            System.out.println("플레이어 " + playerId + "이(가) 정답을 틀렸습니다.");
        }
    }
}
