import math


def print_board(board):  # Board is represented as a single list
    for i in range(3):
        for j in range(3):
            print(board[3*i + j]+" |", end=' ')
        print("")


def has_won(board, shape):  # Check rows, diagonals and columns
    return (shape == board[0] and shape == board[1] and shape == board[2]) or \
           (shape == board[3] and shape == board[4] and shape == board[5]) or \
           (shape == board[6] and shape == board[7] and shape == board[8]) or \
 \
           (shape == board[0] and shape == board[4] and shape == board[8]) or \
           (shape == board[2] and shape == board[4] and shape == board[6]) or \
 \
           (shape == board[0] and shape == board[3] and shape == board[6]) or \
           (shape == board[1] and shape == board[4] and shape == board[7]) or \
           (shape == board[2] and shape == board[5] and shape == board[8])


def possible_moves(board):  # each empty space is a possible move
    return [i for i, x in enumerate(board) if x == ' ']


def is_board_full(board):  # Board is full if there is no empty space left
    return ' ' not in board


# Should check for validity?
# Or is it already being checked?
# (Note to self - Make sure you don't make wasteful work)
def make_move(board, position, shape):
    pass


def minimax(board, is_maximizing):  # The well known AI minimax algorithm
    if has_won(board, 'O'):
        return 1 * (board.count(' ') + 1)

    if has_won(board, 'X'):
        return -1 * (board.count(' ') + 1)

    if is_board_full(board):  # Board is full and no one won --> i.e it's a TIE
        return 0

    if is_maximizing:
        best_score = -math.inf

        for possible_move in possible_moves(board):
            board[possible_move] = 'O'  # Assuming AI is the 'O'
            score = minimax(board, False)
            best_score = max(best_score, score)
            board[possible_move] = ' '

        return best_score
    else:
        best_score = math.inf

        for possible_move in possible_moves(board):
            board[possible_move] = 'X'  # Assuming AI is the 'O'
            score = minimax(board, True)
            best_score = min(best_score, score)
            board[possible_move] = ' '
        return best_score


if __name__ == "__main__":
    pass
