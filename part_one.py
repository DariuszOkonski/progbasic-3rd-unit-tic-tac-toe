def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    row = 3;
    column = 3;
    board = []

    for item in range(row):
        temp_list = ['.'] * column
        board.append(temp_list)

    return board

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass

#
# board = init_board()
#
# board[1][1] = 'x'
# board[2][0] = "o"
# print(board)