def get_proper_coordinates(row_dictionary, column_dictionary, board):
    isCoordinatesCorrect = False
    while not isCoordinatesCorrect:
        coordinates = input("Please enter coordinates: ").upper()

        if (len(coordinates) != 2):
            print("Something is wrong, Please repeat your coordinates")
            continue

        input_row = coordinates[0:1]
        input_col = coordinates[1]

        is_input_row_in_dictionary = input_row in row_dictionary
        is_input_col_in_dictionary = input_col in column_dictionary

        if is_input_row_in_dictionary and is_input_col_in_dictionary:
            isCoordinatesCorrect = True
        else:
            print("Some coordinates are wrong")

        if isCoordinatesCorrect:
            input_row = row_dictionary[input_row]
            input_col = column_dictionary[input_col]
            isCoordinatesCorrect = check_if_position_in_board_is_empty(input_row, input_col, board)

    return (input_row, input_col)

def check_if_position_in_board_is_empty(row, col, board):
    if(board[row][col] == '.'):
        return True
    else:
        print("Current position is occupied")
        return False

# ==========================================================================
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
    row_dictionary = {'A': 0, 'B': 1, 'C': 2}
    column_dictionary = {'1': 0, '2': 1, '3': 2}

    row, col = get_proper_coordinates(row_dictionary, column_dictionary, board)

    return row, col

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


#
board = init_board()

board[0][0] = 'x'
board[1][1] = 'x'
board[2][0] = "o"

row, col = get_move(board, 'player1')
print(row, col)
print("check github")
