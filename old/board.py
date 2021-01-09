import pygame
from pieces import *

class Board():
    def __init__(self):
        self.image = pygame.image.load('../images/board.png')
        self.piece_list = []
        for row, colour in zip([1,6], ['w','b']):
            for column in range(8):
                self.piece_list.append(Pawn(row, column, colour))


board = Board()