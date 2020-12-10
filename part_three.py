import os
import part_one
import part_two
from part_one import init_board, get_move, mark
from part_two import has_won, is_full, print_board

def clear_console():
    os.system('cls')

def display_result(player, board):
    clear_console()
    print_result(player)
    print_board(board)
    return True

def mode_human_human(mode):
    board = init_board()
    isPlayerChanged = True
    end_game = False

    while not end_game:
        player = 'x' if isPlayerChanged else 'o'    
        clear_console()

        print("=== TIC TAC TOE ===")
        print(f"Playing: {mode}")
        print("")
        print(f"Current Player: {player.upper()}")
        print_board(board)
        row, col = get_move(board, player)
        mark(board, player, row, col)

        if(has_won(board, player)):
            end_game = display_result(player, board)
        elif is_full(board):
            player = '0'
            end_game = display_result(player, board)
        isPlayerChanged = not isPlayerChanged
    
    return end_game


# def tictactoe_game(mode='HUMAN-HUMAN'):
#     options = {'human-human': 'HUMAN-HUMAN'}


#     if mode == options['human-human']:
#         mode_human_human(mode)
#     else:
#         print("other options")
# ==================================================================


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""

    if winner.lower() == 'x':
        print("X has won!")
    elif winner.lower() == 'o':
        print("O has won!")
    else:
        print("It's a tie!")


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    isPlayerChanged = True
    end_game = False

    while not end_game:
        player = 'x' if isPlayerChanged else 'o'    
        clear_console()

        print("=== TIC TAC TOE ===")
        print(f"Playing: {mode}")
        print("")
        print(f"Current Player: {player.upper()}")
        print_board(board)
        row, col = get_move(board, player)
        mark(board, player, row, col)

        if(has_won(board, player)):
            clear_console()
            print_result(player)
            print_board(board)
            end_game = True
        elif is_full(board):
            clear_console()
            player = '0'
            print_result(player)
            print_board(board)
            end_game = True

        isPlayerChanged = not isPlayerChanged


tictactoe_game()