const puzzle = document.getElementById("puzzle");
const message = document.getElementById("message");
const moveCountDisplay = document.getElementById("moveCount");

let tiles = [...Array(8).keys()].map((n) => n + 1).concat(null); // [1~8, null]
let moveCount = 0;

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

function isSolved() {
  for (let i = 0; i < 8; i++) {
    if (tiles[i] !== i + 1) return false;
  }
  return true;
}

function updateMoveCount() {
  moveCountDisplay.textContent = `이동 횟수: ${moveCount}`;
}

function render() {
  puzzle.innerHTML = "";
  tiles.forEach((value, i) => {
    const tile = document.createElement("div");
    tile.className = "tile";
    if (value === null) {
      tile.classList.add("empty");
    } else {
      tile.textContent = value;
      tile.addEventListener("click", () => moveTile(i));
    }
    puzzle.appendChild(tile);
  });
}

function moveTile(index) {
  const emptyIndex = tiles.indexOf(null);
  const validMoves = [
    index - 3, // 위
    index + 3, // 아래
    index % 3 !== 0 ? index - 1 : -1, // 왼쪽
    index % 3 !== 2 ? index + 1 : -1, // 오른쪽
  ];

  if (validMoves.includes(emptyIndex)) {
    [tiles[index], tiles[emptyIndex]] = [tiles[emptyIndex], tiles[index]];
    playRandomSound(); // 랜덤 효과음 재생
    moveCount++;
    updateMoveCount();
    render();
    if (isSolved()) {
      message.textContent = `🎉 퍼즐을 완성했습니다! 총 이동 횟수: ${moveCount}`;
    }
  }
}

function startGame() {
  do {
    shuffle(tiles);
  } while (isSolved());

  moveCount = 0;
  updateMoveCount();
  message.textContent = "";
  render();
}

// 사운드
const soundFiles = [
  "sounds/click1.wav",
  "sounds/click2.wav",
  "sounds/click3.wav",
  "sounds/click4.wav",
  "sounds/click5.wav",
];

function playRandomSound() {
  const randomIndex = Math.floor(Math.random() * soundFiles.length);
  const sound = new Audio(soundFiles[randomIndex]);
  sound.play(); // 겹쳐도 재생되도록 새 인스턴스 사용
}

// 리셋
document.getElementById("resetButton").addEventListener("click", startGame);

startGame();
