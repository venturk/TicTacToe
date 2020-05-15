import pygame


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

