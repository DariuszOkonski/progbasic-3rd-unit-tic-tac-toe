import part_one
import part_two


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    print(winner)

    if winner.lower() == 'x':
        print("X has won!")
    elif winner.lower() == 'o':
        print("O has won!")
    else:
        print("It's a tie!")


# def tictactoe_game(mode='HUMAN-HUMAN'):
#     board = init_board()
#
#     # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
#     print_board(board)
#     row, col = get_move(board, 1)
#     mark(board, 1, row, col)
#
#     winner = 0
#     print_result(winner)

# ================================================================

board = part_one.init_board()

player1 = 'osdf'
board[0][0] = '.'
board[0][1] = 'o'
board[0][2] = '.'

board[1][0] = 'o'
board[1][1] = 'x'
board[1][2] = 'x'

board[2][0] = 'o'
board[2][1] = 'x'
board[2][2] = 'x'

part_two.print_board(board)
print_result(player1)