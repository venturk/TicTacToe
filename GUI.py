from main import print_board, is_board_full, has_won, ai_player
import pygame
import sys

WINDOW_WIDTH = WINDOW_HEIGHT = 1050
BLOCK_SIZE = WINDOW_WIDTH // 3  # We want 3 cells in each row and each column


def draw_grid(window):
    for i in range(BLOCK_SIZE, WINDOW_WIDTH, BLOCK_SIZE):
        pygame.draw.lines(window, (255, 255, 255), False, [(i, 0), (i, WINDOW_WIDTH)], 5)
        pygame.draw.lines(window, (255, 255, 255), False, [(0, i), (WINDOW_WIDTH, i)], 5)


def get_cell_pos_from_cords(cords):
    row, col = 2, 2

    if cords[1] < BLOCK_SIZE:
        row = 0
    elif cords[1] < 2 * BLOCK_SIZE:
        row = 1

    if cords[0] < BLOCK_SIZE:
        col = 0
    elif cords[0] < 2 * BLOCK_SIZE:
        col = 1

    return row, col


def get_shape_pos(row, col):
    x, y = BLOCK_SIZE // 3, BLOCK_SIZE // 6

    x += col * BLOCK_SIZE
    y += row * BLOCK_SIZE

    return x, y


if __name__ == "__main__":
    pygame.init()
    board = [' '] * 9  # Init board with 9 cells
    pygame.display.set_caption('Tic Tac Toe')  # Set window title
    font = pygame.font.SysFont('Arial', BLOCK_SIZE // 2)  # Set font
    window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    window.fill((0, 0, 0))
    draw_grid(window)
    game_over = False

    while not game_over:  # Animation loop (game flow loop)
        for event in pygame.event.get():  # for each event
            if event.type == pygame.QUIT:  # Quit
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
                coordinates = pygame.mouse.get_pos()
                row, column = get_cell_pos_from_cords(coordinates)

                if board[3 * row + column] != ' ':  # If spot is unavailable, DO NOTHING
                    continue

                x, y = get_shape_pos(row, column)

                board[3 * row + column] = 'X'
                print_board(board)
                window.blit(font.render('X', True, (255, 0, 0)), (x, y))
                # current_player = 'X' if current_player == 'O' else 'O'

                ai_move = ai_player(board)
                if ai_move is not None:  # Happens only if board is full
                    x, y = get_shape_pos(ai_move // 3, ai_move % 3)
                    board[ai_move] = 'O'
                    window.blit(font.render('O', True, (255, 0, 0)), (x, y))

                if has_won(board, 'O'):
                    game_over = True

                if is_board_full(board):
                    game_over = True

        pygame.display.update()
