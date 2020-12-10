def get_proper_coordinates(row_dictionary, column_dictionary, board):
    isCoordinatesCorrect = False
    max_coordinates_length = 2
    end_game = False

    while not isCoordinatesCorrect:
        coordinates = input("Please enter coordinates: ").upper()

        if coordinates.lower() == 'quit':
            end_game = True
            return (0, 0, end_game)

        if (len(coordinates) != max_coordinates_length):
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

    return (input_row, input_col, end_game)

def check_if_position_in_board_is_empty(row, col, board):
    if(board[row][col] == '.'):
        return True
    else:
        print("Current position is occupied")
        return False

# ==========================================================================
def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    row = 3
    column = 3
    board = []

    for item in range(row):
        temp_list = ['.'] * column
        board.append(temp_list)

    return board

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row_dictionary = {'A': 0, 'B': 1, 'C': 2}
    column_dictionary = {'1': 0, '2': 1, '3': 2}

    row, col, quit_game = get_proper_coordinates(row_dictionary, column_dictionary, board)

    return row, col, quit_game

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player