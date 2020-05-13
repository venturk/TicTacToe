from main import print_board, is_board_full, has_won, ai_player
import pygame
import sys

WIDTH = HEIGHT = 300
CELL_SIZE = WIDTH // 3  # We want 3 cells in each row and each column


def draw_grid(window, thickness=5, color=(255, 255, 255)):  # draw a grid of 3x3 on a given pygame display
    # Horizontal lines
    pygame.draw.lines(window, color, False, [(0, CELL_SIZE), (WIDTH, CELL_SIZE)], thickness)
    pygame.draw.lines(window, color, False, [(0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE)], thickness)

    # Vertical lines
    pygame.draw.lines(window, color, False, [(CELL_SIZE, 0), (CELL_SIZE, WIDTH)], 5)
    pygame.draw.lines(window, color, False, [(2 * CELL_SIZE, 0), (2 * CELL_SIZE, WIDTH)], thickness)


def get_cell_pos_from_cords(coords):
    row = col = 2  # Default value is last cell

    if coords[1] < CELL_SIZE:        # In 1st row
        row = 0
    elif coords[1] < 2 * CELL_SIZE:  # In 2nd row
        row = 1

    if coords[0] < CELL_SIZE:        # In 1st column
        col = 0
    elif coords[0] < 2 * CELL_SIZE:  # In 2nd column
        col = 1

    return row, col


def get_shape_pos(row, col):
    x, y = CELL_SIZE // 3, CELL_SIZE // 6

    x += col * CELL_SIZE
    y += row * CELL_SIZE

    return x, y


def update_board(board, window, player, row, col):
    # Update board
    board[3 * row + col] = player
    print_board(board)

    # Update GUI
    x, y = get_shape_pos(row, col)
    window.blit(font.render(player, True, (255, 0, 0)), (x, y))
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Tic Tac Toe')  # Set window title
    font = pygame.font.SysFont('Arial', CELL_SIZE // 2)  # Set font
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    display.fill((0, 0, 0))
    draw_grid(display)

    board = [' '] * 9
    game_over = False

    while not game_over:  # Animation loop (game flow loop)
        for event in pygame.event.get():  # for each event
            if event.type == pygame.QUIT:  # Quit
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
                coordinates = pygame.mouse.get_pos()
                row, column = get_cell_pos_from_cords(coordinates)

                if board[3 * row + column] == ' ':  # If spot is unavailable, DO NOTHING
                    update_board(board, display, 'X', row, column)

                    ai_move = ai_player(board)
                    if ai_move is not None:  # Happens only if board is full
                        update_board(board, display, 'O', ai_move // 3, ai_move % 3)

                    if has_won(board, 'O'):
                        game_over = True

                    if is_board_full(board):
                        game_over = True

        pygame.display.update()
