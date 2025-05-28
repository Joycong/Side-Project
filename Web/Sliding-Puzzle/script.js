const puzzle = document.getElementById("puzzle");
const message = document.getElementById("message");
let tiles = [...Array(8).keys()].map((n) => n + 1).concat(null); // [1,2,...,8,null]

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
    render();
    if (isSolved()) {
      message.textContent = "🎉 퍼즐을 완성했습니다!";
    }
  }
}

function startGame() {
  do {
    shuffle(tiles);
  } while (isSolved()); // 정답 상태로 시작되지 않도록

  message.textContent = "";
  render();
}

startGame();

// 리셋
document.getElementById("resetButton").addEventListener("click", startGame);
