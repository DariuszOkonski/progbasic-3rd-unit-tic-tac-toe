def get_proper_coordinates(row_dictionary, column_dictionary):
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

    return (input_row, input_col)

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
    row_dictionary = { 'A': 0, 'B': 1, 'C': 2}
    column_dictionary = {'1': 0, '2': 1, '3': 2}

    row, col = 0, 0
    print(board)

    # isCoordinatesCorrect = False
    # while not isCoordinatesCorrect:
    #     coordinates = input("Please enter coordinates: ").upper()
    #
    #     if(len(coordinates) != 2):
    #         print("Something is wrong, Please repeat your coordinates")
    #         continue
    #
    #     input_row = coordinates[0:1]
    #     input_col = coordinates[1]
    #
    #     is_input_row_in_dictionary = input_row in row_dictionary
    #     is_input_col_in_dictionary = input_col in column_dictionary
    #
    #     if is_input_row_in_dictionary and is_input_col_in_dictionary:
    #         print("coordinates are ok")
    #         isCoordinatesCorrect = True
    #     else:
    #         print("Some coordinates are wrong")


    row_position, col_position = get_proper_coordinates(row_dictionary, column_dictionary)
    print(row_position, col_position)


    # if coordinates are out of board, keep asking
    # if coordinates are already taken, keep asking
    # if coordinates doesn't look like coordinates, keep asking




    # player specifies coordinates i.e: A2, C1
    # return tuple of tow int (row, col) - coordinates starts from 0
    # coordinates has to indicate a valid empty position in board




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
# print(row, col)
