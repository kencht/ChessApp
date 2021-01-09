import numpy as np
import pygame
from move_piece import *
from copy import deepcopy as dc

class Board():
    def __init__(self):
        self.current = self.start_board()
        self.position_list = [dc(self.current)]
        self.image_labels = self.setup_images()
        self.screen = pygame.display.set_mode((600, 600))
        self.no_piece = True  # trigger A
        self.sele_piece = False
        self.sele_square = False
        self.sele_nsqu = False
        self.move_done = False  # trigger B
        self.last_colour = -1
        self.this_colour = 1
        self.mouse_hover = 0

    def start_board(self):
        arr = np.zeros((8, 8), 'int')
        start_pieces = np.array([2, 3, 4, 5, 6, 4, 3, 2])
        arr[-2] = 1
        arr[-1] = start_pieces
        arr[1] = -1
        arr[0] = -start_pieces
        return arr

    def setup_images(self):
        image_list = {'board': pygame.image.load('images/board.png')}
        pathlist = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
        for key, path in enumerate(pathlist, 1):  # changing most general aspect
            for i, i_path in zip([key, -key], ['', '_b']):
                image = pygame.image.load('images/' + path + i_path + '.png')
                w, h = image.get_size()
                image = pygame.transform.smoothscale(image, (int(w / 10), int(h / 10)))
                image_list[i] = image
        return image_list

    def move(self, iy, ix, ny, nx):
        if move_piece(self.current, iy, ix, ny, nx):
            # pawn move
            self.current[ny, nx] = self.current[iy, ix]
            self.current[iy, ix] = 0
            self.position_list.append(dc(self.current))
            print(self.current)

    def user_move(self, isqu, nsqu):
        ir, ic = square_to_int(isqu)
        nr, nc = square_to_int(nsqu)
        self.move(ir, ic, nr, nc)

    def poss_take(self, isqu):
        ir, ic = square_to_int(isqu)
        for x in range(8):
            for y in range(8):
                if move_piece(self.current, ir, ic, x, y):
                    if self.current[x, y]:
                        print('can take at ' + int_to_square(x, y))
                    else:
                        print('can move to ' + int_to_square(x, y))

    def poss_piece(self, nsqu):
        nr, nc = square_to_int(nsqu)
        for x in range(8):
            for y in range(8):
                if move_piece(self.current, x, y, nr, nc):
                    if self.current[x, y]:
                        print('can take from ' + int_to_square(x, y))
                    else:
                        print('can move from ' + int_to_square(x, y))

    def pgn_move(self, nsqu):
        nr, nc = square_to_int(nsqu)
        for x in range(8):
            for y in range(8):
                if move_piece(self.current, x, y, nr, nc):
                    if self.current[x, y]:
                        print('can take from ' + int_to_square(x, y))
                    else:
                        print('can move from ' + int_to_square(x, y))

    def show_board(self):
        self.screen.blit(self.image_labels['board'], (0, 0))
        if self.sele_piece:
            self.screen.blit(self.image_labels[self.sele_piece], self.mouse_hover)
        for x in range(8):
            for y in range(8):
                piece = self.current[x, y]
                if piece:
                    image = self.image_labels[piece]
                    w, h = image.get_size()
                    self.screen.blit(self.image_labels[piece], int_to_pos(x, y, w, h))

    def pick_up_piece(self, event):
        if not self.sele_piece:
            c, r = pos_to_int(event.pos)
            self.sele_square = r, c
            self.sele_piece = self.current[self.sele_square]
            self.current[r, c] = 0
            self.no_piece = False  # switches trigger A off to only loop through once


    def drag_piece(self, event):
        if self.sele_piece:
            r, c = event.pos
            image = self.image_labels[self.sele_piece]
            w, h = image.get_size()
            rc = r - w / 2
            cc = c - h / 2
            self.mouse_hover = rc, cc

    def drop_piece(self, event):
        if self.sele_piece:
            if self.sele_piece > 0:
                self.this_colour = 1
            if self.sele_piece < 0:
                self.this_colour = -1
            ir = self.sele_square[0]
            ic = self.sele_square[1]
            nc, nr = pos_to_int(event.pos)
            if move_piece(self.position_list[-1], ir, ic, nr, nc) and self.this_colour != self.last_colour:
                self.current[nr, nc] = self.sele_piece
                self.position_list.append(dc(self.current))
                self.last_colour = -self.last_colour
            else:
                self.current[ir, ic] = self.sele_piece
            self.sele_piece = False


# board = Board()

