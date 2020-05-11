def print_board(board):  # Board is represented as a single list
    for i in range(3):
        for j in range(3):
            print(board[3*i + j]+" |", end=' ')
        print("")


def has_won(board, player):  # Check rows, diagonals and columns
    return (player == board[0] and player == board[1] and player == board[2]) or \
           (player == board[3] and player == board[4] and player == board[5]) or \
           (player == board[6] and player == board[7] and player == board[8]) or \
 \
           (player == board[0] and player == board[4] and player == board[8]) or \
           (player == board[2] and player == board[4] and player == board[6]) or \
 \
           (player == board[0] and player == board[3] and player == board[6]) or \
           (player == board[1] and player == board[4] and player == board[7]) or \
           (player == board[2] and player == board[5] and player == board[8])


def possible_moves(board):  # each empty space is a possible move
    return [i for i, x in enumerate(board) if x == ' ']


def is_board_full(board):  # Board is full if there is no empty space left
    return ' ' not in board


# If board is full AND no player won, there is a TIE...
# Is there a need for this function...?
def is_tie(board):
    pass


# Should check for validity?
# Or is it already being checked?
# (Note to self - Make sure you don't make wasteful work)
def make_move(board, position, shape):
    pass


def minimax(board, isMaximizing):  # The well known AI minimax algorithm
    pass