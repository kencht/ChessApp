import string

def square_to_int(squ):
    return 8 - int(squ[1]), ord(squ[0])-97

def int_to_pos(row, column, w, h):
    return 75 * column + (75 - w) / 2, 75 * row + (67 - h)

def occ_colour(piece):
    if piece > 0:
        return 'w'
    if piece < 0:
        return 'b'

def int_to_square(r, c):
    return chr(c + 97) + str(8-r)

def pos_to_int(pos):
    x, y = pos
    return int(x / 75), int(y / 75)
