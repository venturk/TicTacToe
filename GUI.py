import sys

import pygame

WINDOW_WIDTH = WINDOW_HEIGHT = 900
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
    x, y = 25, 6

    x += col * BLOCK_SIZE
    y += row * BLOCK_SIZE

    return x, y


if __name__ == "__main__":
    pygame.init()
    board = [' '] * 9  # Init board with 9 cells
    pygame.display.set_caption('Tic Tac Toe')  # Set window title

    window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    window.fill((0, 0, 0))
    draw_grid(window)
    game_over = False

    while not game_over:  # Animation loop (game flow loop)
        for event in pygame.event.get():  # for each event
            if event.type == pygame.QUIT:  # Quit
                pygame.quit()
                sys.exit()

        pygame.display.update()
