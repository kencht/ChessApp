import numpy as np
from util import *


def move_piece(pos, ir, ic, nr, nc):
    # pieces list
    piece = pos[ir, ic]  # index board at initial square
    nsqu = pos[nr, nc]  # index board at new square
    piece_col = occ_colour(piece)  # uses a function to assign a piece colour to initial square
    nsqu_col = occ_colour(nsqu)  # uses a function to assign a piece colour to new square

    if nsqu_col == piece_col:  # stops move_piece function if you try take a piece of the same colour
        return False

    # pawn
    if abs(piece) == 1:  # enters pawn rules if starting piece is a pawn
        # move
        if nc == ic and not nsqu:  # if the pieces stays in the same column and nsqu = 0 (making 'not nsqu' True)
            # one square
            if nr == ir - piece:  # indexes from top left, moves white piece up one space, black piece down
                return True
            # two square
            if nr == ir - 2*piece and ir == (1 if piece == -1 else 6):  # allows a two square if ir is 1 for b pawn or otherwise row 6.
                return True
        # take piece
        if abs(nc - ic) == 1 and nr == ir - piece and nsqu:  # if change in column is 1 and change in row is the same as piece (ie +/- 1) and the square is non zero allow a take
            return True

    # file move
    if abs(piece) in [2, 5]:  # both queens and rooks can move along files
        queen = abs(piece) == 5  # defines a queen as a 5
        # move
        d_hor = nc != ic  # defines d_hor as a boolean which is True if column changes
        d_ver = nr != ir  # defines d_ver as a boolean which is True if row changes
        queen_diag = False  # sets starting value for queen_diag as false
        if d_hor and d_ver:  # if both the row and column change...
            if not queen:  # and if the piece is not a queen
                return False  # disallow the move
            else:
                queen_diag = True  # if the piece is a queen and has moved row and column switch value of queen_diag
        if not queen_diag:  # skips section if piece if diagonal queen move.
            # move horizontal
            if d_ver:
                step = 1 if nr > ir else -1  # sets up file directionality to sum along
                if abs(np.sum(pos[ir + step:nr:step, ic])):  # sums row file after piece square to the new square in correct direction. Non zero sum returns False
                    return False
            # move vertical
            if d_hor:
                step = 1 if nc > ic else -1
                if abs(np.sum(pos[ir, ic + step:nc:step])):  # same as above but for column file
                    return False
            return True  # allows file move for rook or queen. Code skipped for diagonally moving queen

    # knight
    if abs(piece) == 3:  # selects square for knight
        d_hor = abs(nc - ic)  # change in column
        d_ver = abs(nr - ir)  # change in row
        shifts = [d_hor, d_ver]  # defines shifts as an array
        if 1 in shifts and 2 in shifts:  # if both 1 and 2 are in the array allow a move
            return True

    # move diagonal
    if abs(piece) in [4, 5]:  # allows move for bishop and queen
        # move
        d_hor = nc - ic
        d_ver = nr - ir
        if abs(d_hor) == abs(d_ver):  # if movement is a square
            step_r = 1 if nr > ir else -1  # row step directionality
            step_c = 1 if nc > ic else -1  # column step directionality
            for it_r, it_c in zip(np.arange(ir + step_r, nr, step_r), np.arange(ic + step_c, nc, step_c)):  # iterates values to index over two separate ranges
                if pos[it_r, it_c]:  # indexes the iterated values and returns false if an int is hit
                    return False
            return True

    # king
    if abs(piece) == 6:  # selects king
        if abs(nr-ir) < 2 and abs(nc-ic) < 2:  # can only move one square
            return True

