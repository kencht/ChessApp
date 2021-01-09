import numpy as np
import pygame
from move_piece import *
from board import *
from copy import deepcopy as dc

# analyse PGN

pgn = str('1. e4 e5 2. Nf3 Nc6 3. d3 f6 4. d4 exd4 5. Nbd2 b6 6. Nb3 Bc5 7. Nbxd4')
split = pgn.split()
del split[0::3]

corr_split = []

for i in split:
    if i[0].islower():
        i = 'P' + i
        corr_split.append(i)
    else:
        corr_split.append(i)

# make game sequence

def pgn_move(pos, nsqu, piece, choice):
