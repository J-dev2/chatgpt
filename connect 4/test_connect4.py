import connect4 as c4


def test_horizontal_win():
    board = c4.create_board()
    # Place four pieces for player 1 in the bottom row
    for col in range(4):
        row = c4.get_next_open_row(board, col)
        c4.drop_piece(board, row, col, 1)
    assert c4.winning_move(board, 1), "Player 1 should win horizontally"


def run_tests():
    test_horizontal_win()
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
