// GameLauncher.java
package numberGame;

public class GameLauncher {
    public static void main(String[] args) {
        GuessGame game = new GuessGame(3, 3); // 플레이어 수와 정답 개수를 3으로 설정
        game.startGame();
    }
}
