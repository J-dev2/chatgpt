# Connect 4 game in Python

ROWS = 6
COLS = 7

def create_board():
    return [[0] * COLS for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == 0:
            return r
    return None

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        print_board(board)
        col = int(input(f"Player {turn + 1} make your selection (0-{COLS-1}): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, turn + 1)

            if winning_move(board, turn + 1):
                print_board(board)
                print(f"Player {turn + 1} wins!")
                game_over = True

            turn = (turn + 1) % 2
        else:
            print("Column is full. Try again.")

if __name__ == "__main__":
    play_game()
