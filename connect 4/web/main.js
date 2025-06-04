async function getState() {
    const res = await fetch('/api/state');
    return res.json();
}

async function postMove(col) {
    const res = await fetch('/api/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ col })
    });
    return res.json();
}

async function postReset() {
    const res = await fetch('/api/reset', { method: 'POST' });
    return res.json();
}

function renderBoard(board) {
    const boardDiv = document.getElementById('board');
    boardDiv.innerHTML = '';
    for (let r = 0; r < board.length; r++) {
        for (let c = 0; c < board[r].length; c++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            const val = board[r][c];
            if (val === 1) cell.classList.add('player1');
            if (val === 2) cell.classList.add('player2');
            cell.dataset.col = c;
            cell.addEventListener('click', async () => {
                const state = await postMove(c);
                update(state);
            });
            boardDiv.appendChild(cell);
        }
    }
}

function update(state) {
    renderBoard(state.board);
    const status = document.getElementById('status');
    if (state.winner) {
        status.textContent = `Player ${state.winner} wins!`;
    } else {
        status.textContent = `Player ${state.turn}'s turn`;
    }
}

document.getElementById('reset').addEventListener('click', async () => {
    const state = await postReset();
    update(state);
});

window.addEventListener('load', async () => {
    const state = await getState();
    update(state);
});
