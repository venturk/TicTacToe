from Player import HumanPlayer, AIPlayer, has_won
import pygame


class Board(object):
    def __init__(self, cell_size=100):
        self.board = [' '] * 9
        self.width = self.height = cell_size * 3
        self.cell_size = cell_size

        self.display = self.init_display()
        self.font = pygame.font.SysFont('Arial', self.cell_size // 2)  # Set font
        self.draw_grid()

    def init_display(self):
        pygame.init()  # Init pygae
        pygame.display.set_caption('Tic Tac Toe')  # Set window title
        display = pygame.display.set_mode((self.width, self.height))
        display.fill((0, 0, 0))

        return display

    def empty_cells(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def redraw_board(self):
        self.display.fill((0, 0, 0))
        self.draw_grid()
        self.board = [' '] * 9

    def draw_grid(self, thic=8, color=(255, 255, 255)):  # draw a grid of 3x3 on a given pygame display
        # Horizontal lines
        pygame.draw.lines(self.display, color, False, [(0, self.cell_size), (self.width, self.cell_size)], thic)
        pygame.draw.lines(self.display, color, False, [(0, 2 * self.cell_size), (self.width, 2 * self.cell_size)], thic)

        # Vertical lines
        pygame.draw.lines(self.display, color, False, [(self.cell_size, 0), (self.cell_size, self.height)], 5)
        pygame.draw.lines(self.display, color, False, [(2 * self.cell_size, 0), (2 * self.cell_size, self.height)], thic)

        pygame.display.update()

    def update_board(self, row, col, player):
        if self.update_cell(row, col, player.shape):  # If update successful, draw shape on board
            self.draw_shape(row, col, player)
            return True

        return False

    def update_cell(self, row, col, shape):
        if self.board[3 * row + col] == ' ':
            self.board[3 * row + col] = shape
            return True
        return False

    def draw_shape(self, row, col, player):
        x, y = self.get_shape_pos(row, col)
        self.display.blit(self.font.render(player.shape, True, player.color), (x, y))
        pygame.display.update()

    def get_cell_pos_from_cords(self, coords):
        row = col = 2  # Default value is last cell

        if coords[1] < self.cell_size:        # In 1st row
            row = 0
        elif coords[1] < 2 * self.cell_size:  # In 2nd row
            row = 1

        if coords[0] < self.cell_size:        # In 1st column
            col = 0
        elif coords[0] < 2 * self.cell_size:  # In 2nd column
            col = 1

        return row, col

    def get_shape_pos(self, row, col):
        x, y = self.cell_size // 3, self.cell_size // 6

        x += col * self.cell_size
        y += row * self.cell_size

        return x, y


if __name__ == "__main__":
    board = Board()
    player1 = AIPlayer('X', (255, 255, 0))
    player2 = HumanPlayer('O', (0, 0, 255))
    current_player = player1

    while True:  # Animation loop (game flow loop)
        row, column = current_player.play_turn(board)  # Get selected cell's row and col, for current player
        if row is None:  # No move was selected
            continue

        board.update_board(row, column, current_player)  # Update board with selected cell
        if has_won(board.board, 3 * row + column):  # Check if last move was a wining move
            print("{} has won!".format(current_player.shape))
            break

        if not board.empty_cells():  # Check for a tie
            print("TIE")
            break

        current_player = player2 if current_player is player1 else player1  # Update current player
