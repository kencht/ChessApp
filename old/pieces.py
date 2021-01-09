import util
import pygame

class Pawn():
    def __init__(self, row, column, c):
        self.row = row
        self.column = column
        self.c = c
        self.image = pygame.image.load('images/pawn{}.png'.format('_b' if c == 'b' else ''))
        self.w, self.h = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (int(self.w / 10), int(self.h / 10)))
        self.w, self.h = self.image.get_size()
        self.pos = self.int_to_pos(row, column)

    def int_to_pos(self, row, column):
        x = (75 * column) + int(37.5 - self.w/2)
        y = (75 * (7 - row)) + int(70 - self.h)
        return x, y

    def move(self, newsquare):
        ic, ir = util.square_to_int(self.square)
        nc, nr = util.square_to_int(newsquare)
        print(ir, ic, nr, nc)
        if nr == ir + 1 and nc == ic:
            self.square = newsquare

