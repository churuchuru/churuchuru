const gameBoard = document.getElementById("gameBoard");
const message = document.getElementById("message");
const restartBtn = document.getElementById("restartBtn");

let board = Array(9).fill("");
let currentPlayer = "X";
let gameActive = true;

const winningConditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
    [0, 4, 8], [2, 4, 6]             // diagonals
];

function createBoard() {
    board.forEach((_, index) => {
        const cell = document.createElement("div");
        cell.classList.add("flex", "justify-center", "items-center", "text-5xl", "cursor-pointer", "bg-white", "border-2", "border-gray-800", "transition-colors", "hover:bg-gray-200", "h-24", "w-24");
        cell.setAttribute("data-cell-index", index);
        cell.addEventListener("click", handleCellClick);
        gameBoard.appendChild(cell);
    });
}

function handleCellClick(event) {
    const cellIndex = event.target.getAttribute("data-cell-index");

    if (board[cellIndex] !== "" || !gameActive) return;

    board[cellIndex] = currentPlayer;
    event.target.textContent = currentPlayer;

    checkWinner();
    currentPlayer = currentPlayer === "X" ? "O" : "X";
}

function checkWinner() {
    for (let condition of winningConditions) {
        const [a, b, c] = condition;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            message.textContent = `Player ${board[a]} wins!`;
            gameActive = false;
            return;
        }
    }

    if (!board.includes("")) {
        message.textContent = "It's a draw!";
        gameActive = false;
    }
}

function restartGame() {
    board = Array(9).fill("");
    currentPlayer = "X";
    gameActive = true;
    message.textContent = "";
    gameBoard.innerHTML = "";
    createBoard();
}

restartBtn.addEventListener("click", restartGame);

createBoard();
