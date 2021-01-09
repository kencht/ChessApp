import pygame
from board import Board

pygame.init()
screen = pygame.display.set_mode((600, 600))
board = Board()
running = True
while running:
    for event in pygame.event.get():
        board.show_board()

    if event.type == pygame.MOUSEBUTTONDOWN:
        board.pick_up_piece(event)

    if pygame.mouse.get_pressed()[0]:
        board.drag_piece(event)

    if event.type == pygame.MOUSEBUTTONUP:
        board.drop_piece(event)



    pygame.display.update()
    if event.type == pygame.QUIT:
        running = False
