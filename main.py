from GUI import game_flow


def print_board(board, indexed=False):
    for i in range(3):
        for j in range(3):
            empty = 3*i + j if indexed else ' '
            cell = board[3*i + j] if board[3*i + j] != ' ' else empty
            print("{} |".format(cell), end=' ')
        print()
    print()


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


def possible_moves(board):  # each empty cell is a possible move
    return [i for i, x in enumerate(board) if x == ' ']


def is_board_full(board):  # Board is full if there is no empty space left
    return ' ' not in board


def minimax(board, is_maximizing):  # The well known AI minimax algorithm
    if has_won(board, 'O'):
        return 1 * (board.count(' ') + 1)

    if has_won(board, 'X'):
        return -1 * (board.count(' ') + 1)

    if is_board_full(board):  # Board is full and no one won --> i.e it's a TIE
        return 0

    if is_maximizing:
        best_score = -6

        for possible_move in possible_moves(board):
            board[possible_move] = 'O'  # Assuming AI is the 'O'
            score = minimax(board, False)
            best_score = max(best_score, score)
            board[possible_move] = ' '

        return best_score
    else:
        best_score = 6

        for possible_move in possible_moves(board):
            board[possible_move] = 'X'  # Assuming AI is the 'O'
            score = minimax(board, True)
            best_score = min(best_score, score)
            board[possible_move] = ' '
        return best_score


def ai_player(board):
    moves = possible_moves(board)
    if moves:
        print("AI's turn... evaluating!")
        best_score = -6
        best_move = None

        for pos in moves:
            board[pos] = 'O'  # Assign current cell as 'O'
            score = minimax(board, False)  # Evaluate the assignment with the minimax algorithm

            if score > best_score:  # Update best score and best move
                best_score = score
                best_move = pos

            board[pos] = ' '  # Clean current cell for next iteration

        print("DONE! AI choose to put its shape at {}".format(best_move))

        return best_move
    else:
        return None


def human_player(board):
    moves = possible_moves(board)
    print("Your turn! Please choose an index: ", *moves)
    try:
        move = int(input())
        if move not in moves:
            raise ValueError

        return move
    except (ValueError, IndexError) as e:
        print("Wrong value! Please try again...")
        return None


def cmd_game_flow():
    b = [' '] * 9  # Board is represented as a single list
    current_player = 'X'

    while True:
        if has_won(b, current_player):
            print("GAME OVER! {} WON!".format(current_player))
            break

        if is_board_full(b):
            print("Well... technically, you didn't lose.")
            break

        move = None
        while move is None:
            move = human_player(b)
        b[move] = 'X'
        print_board(b)

        ai_move = ai_player(b)
        if ai_move is None:  # Happens only if board is full
            continue

        b[ai_move] = 'O'
        print_board(b)


if __name__ == "__main__":
    game_flow()
