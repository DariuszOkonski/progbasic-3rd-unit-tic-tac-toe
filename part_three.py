import part_one
import part_two
from part_one import init_board, get_move, mark
from part_two import has_won, is_full, print_board

def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    print(winner)

    if winner.lower() == 'x':
        print("X has won!")
    elif winner.lower() == 'o':
        print("O has won!")
    else:
        print("It's a tie!")


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)



tictactoe_game()