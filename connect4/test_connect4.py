from . import game as c4


def test_horizontal_win():
    board = c4.create_board()
    # Place four pieces for player 1 in the bottom row
    for col in range(4):
        row = c4.get_next_open_row(board, col)
        c4.drop_piece(board, row, col, 1)
    assert c4.winning_move(board, 1), "Player 1 should win horizontally"

def test_vertical_win():
    board = c4.create_board()
    for _ in range(4):
        row = c4.get_next_open_row(board, 0)
        c4.drop_piece(board, row, 0, 1)
    assert c4.winning_move(board, 1), "Player 1 should win vertically"

def test_diagonal_win():
    board = c4.create_board()
    # set up a positive slope diagonal win
    c4.drop_piece(board, c4.get_next_open_row(board, 0), 0, 1)

    c4.drop_piece(board, c4.get_next_open_row(board, 1), 1, 2)
    c4.drop_piece(board, c4.get_next_open_row(board, 1), 1, 1)

    c4.drop_piece(board, c4.get_next_open_row(board, 2), 2, 2)
    c4.drop_piece(board, c4.get_next_open_row(board, 2), 2, 2)
    c4.drop_piece(board, c4.get_next_open_row(board, 2), 2, 1)

    c4.drop_piece(board, c4.get_next_open_row(board, 3), 3, 2)
    c4.drop_piece(board, c4.get_next_open_row(board, 3), 3, 2)
    c4.drop_piece(board, c4.get_next_open_row(board, 3), 3, 2)
    c4.drop_piece(board, c4.get_next_open_row(board, 3), 3, 1)

    assert c4.winning_move(board, 1), "Player 1 should win diagonally"


def run_tests():
    test_horizontal_win()
    test_vertical_win()
    test_diagonal_win()
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
