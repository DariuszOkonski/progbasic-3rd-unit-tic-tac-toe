import part_one

def has_won(board, player):
    """Returns True if player has won the game."""

    is_first_row_win = board[0][0] == player and board[0][1] == player and board[0][2] == player
    is_second_row_win = board[1][0] == player1 and board[1][1] == player1 and board[1][2] == player1
    is_third_row_win = board[2][0] == player1 and board[2][1] == player1 and board[2][2] == player1
    
    is_first_column_win = board[0][0] == player and board[1][0] == player and board[2][0] == player
    is_second_column_win = board[0][1] == player and board[1][1] == player and board[2][1] == player
    is_third_column_win = board[0][2] == player and board[1][2] == player and board[2][2] == player

    is_a_c_diagonal_win = board[0][0] == player and board[1][1] == player and board[2][2] == player
    is_c_a_diagonal_win = board[0][2] == player and board[1][1] == player and board[2][0] == player

    if (is_first_row_win or is_second_row_win or is_third_row_win or 
        is_first_column_win or is_second_column_win or is_third_column_win or
        is_a_c_diagonal_win or is_c_a_diagonal_win):
            return True

    return False

def is_full(board):
    """Returns True if board is full."""
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == '.'):
                return False
    
    return True

def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    temp_board = f"""
        1   2   3
      A {board[0][0]} | {board[0][1]} | {board[0][2]} 
       ---+---+---
      B {board[1][0]} | {board[1][1]} | {board[1][2]} 
       ---+---+---
      C {board[2][0]} | {board[2][1]} | {board[2][2]}
    """    
    print(temp_board)

# workspace ==================================================

# board = part_one.init_board()

# player1 = 'x'
# board[0][0] = '.'
# board[0][1] = 'o'
# board[0][2] = '.'

# board[1][0] = 'o'
# board[1][1] = 'x'
# board[1][2] = 'x'

# board[2][0] = 'o'
# board[2][1] = 'x'
# board[2][2] = 'x'

# print_board(board)


# print(board)

# is_board_full = is_full(board)
# print(is_board_full)

# iswin = has_won(board, player1)
# print(iswin)
