import pygame


def has_won(board, index):
    if board.count(' ') > 4:
        return False

    row_i = (index//3)*3
    if board[row_i] == board[row_i + 1] and board[row_i + 1] == board[row_i + 2]:
        return True

    col_i = index % 3
    if board[col_i] == board[col_i + 3] and board[col_i + 3] == board[col_i + 6]:
        return True

    if not index % 2:
        return (board[0] == board[4] and board[4] == board[8]) or (board[2] == board[4] and board[4] == board[6])


class HumanPlayer(object):
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    @staticmethod
    def play_turn(board):
        for event in pygame.event.get():  # for each event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If left mouse button is clicked
                coordinates = pygame.mouse.get_pos()  # Get click coordinates
                row, column = board.get_cell_pos_from_cords(coordinates)  # Translate coordinates into row, col

                return row, column

        return None, None


class AIPlayer(object):
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def minimax(self, board, index, is_maximizing):  # The well known AI minimax algorithm
        if has_won(board.board, index):                     # Check if last move was a winning move
            factor = -1 if is_maximizing else 1             # If it's the maximizing player's turn,
            return factor * (len(board.empty_cells()) + 1)  # it means that the enemy made the last winning move

        if not board.empty_cells():  # Last player to play didn't win AND the board is full --> i.e it's a TIE
            return 0

        best_score = -6 if is_maximizing else 6          # Init best score with default value
        enemy_shape = 'X' if self.shape == 'O' else 'O'  # Init enemy shape
        for possible_move in board.empty_cells():
            board.board[possible_move] = self.shape if is_maximizing else enemy_shape  # Assign shape to current cell
            score = self.minimax(board, possible_move, not is_maximizing)
            best_score = max(best_score, score) if is_maximizing else min(best_score, score)
            board.board[possible_move] = ' '  # Clean current cell for next iteration

        return best_score

    def play_turn(self, board):
        moves = board.empty_cells()
        if moves:
            if len(moves) == 9:
                return 0, 0  # Best opening move is one of the corners
            best_score = -6
            best_move = None

            for move in moves:
                board.board[move] = self.shape
                score = self.minimax(board, move, False)  # Evaluate the assignment with the minimax algorithm

                if score > best_score:  # Update best score and best move
                    best_score = score
                    best_move = move

                board.board[move] = ' '  # Clean current cell for next iteration
            print("{} PLAYED {}!".format(self.shape, best_move))
            return best_move // 3, best_move % 3

        return None, None  # There are no moves to play
