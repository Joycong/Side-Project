const puzzle = document.getElementById("puzzle");
const tiles = [];
let emptyX = 2;
let emptyY = 2;
let moveCount = 0;
let bestScore = localStorage.getItem("bestScore");

const sounds = [
  new Audio("sounds/click1.mp3"),
  new Audio("sounds/click2.mp3"),
  new Audio("sounds/click3.mp3"),
  new Audio("sounds/click4.mp3"),
  new Audio("sounds/click5.mp3"),
];

// 퍼즐 초기화
function initTiles() {
  tiles.length = 0;
  let numbers = [...Array(8).keys()].map((n) => n + 1);
  numbers.sort(() => Math.random() - 0.5);
  numbers.push(null);

  for (let i = 0; i < 9; i++) {
    tiles.push(numbers[i]);
  }
  emptyX = 2;
  emptyY = 2;
}

// 퍼즐 그리기
function render() {
  puzzle.innerHTML = "";
  for (let y = 0; y < 3; y++) {
    for (let x = 0; x < 3; x++) {
      const value = tiles[y * 3 + x];
      const tile = document.createElement("div");
      tile.className = value ? "tile" : "tile empty";
      tile.textContent = value || "";
      tile.dataset.x = x;
      tile.dataset.y = y;
      puzzle.appendChild(tile);
    }
  }
}

// 타일 이동
function moveTile(x, y) {
  const dx = Math.abs(x - emptyX);
  const dy = Math.abs(y - emptyY);
  if (dx + dy === 1) {
    const fromIdx = y * 3 + x;
    const toIdx = emptyY * 3 + emptyX;
    [tiles[fromIdx], tiles[toIdx]] = [tiles[toIdx], tiles[fromIdx]];
    emptyX = x;
    emptyY = y;
    moveCount++;
    document.getElementById(
      "moveCount"
    ).textContent = `이동 횟수: ${moveCount}`;

    // 랜덤 사운드
    const randomSound = sounds[Math.floor(Math.random() * sounds.length)];
    randomSound.play();

    render();
    if (isSolved()) {
      setTimeout(() => {
        alert("퍼즐 완성!");
      }, 100);

      // 최고 기록 갱신
      if (bestScore === null || moveCount < bestScore) {
        bestScore = moveCount;
        localStorage.setItem("bestScore", bestScore);
        updateBestScoreUI();
      }
    }
  }
}

// 퍼즐 완성 상태 체크
function isSolved() {
  for (let i = 0; i < 8; i++) {
    if (tiles[i] !== i + 1) return false;
  }
  return tiles[8] === null;
}

// 리셋
function resetPuzzle() {
  initTiles();
  moveCount = 0;
  document.getElementById("moveCount").textContent = `이동 횟수: ${moveCount}`;
  render();
}

// 최고 기록 UI 업데이트
function updateBestScoreUI() {
  const bestScoreText = bestScore !== null ? `${bestScore}회` : "-";
  document.getElementById(
    "bestScore"
  ).textContent = `최고 기록: ${bestScoreText}`;
}

// 디버깅용 퍼즐 완성 버튼
function completePuzzleForTest() {
  tiles.length = 0;
  for (let i = 1; i <= 8; i++) {
    tiles.push(i);
  }
  tiles.push(null); // 마지막 빈칸
  emptyX = 2;
  emptyY = 2;
  render();
}

// 초기화
initTiles();
render();
updateBestScoreUI();

// 이벤트 등록
puzzle.addEventListener("click", (e) => {
  if (e.target.classList.contains("tile")) {
    const x = parseInt(e.target.dataset.x);
    const y = parseInt(e.target.dataset.y);
    moveTile(x, y);
  }
});

document.getElementById("resetButton").addEventListener("click", resetPuzzle);
document
  .getElementById("completeButton")
  .addEventListener("click", completePuzzleForTest);
