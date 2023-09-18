import pygame

WINDOWS = 780
TILE_SIZE = 60
RANGE = (1, (WINDOWS // TILE_SIZE) + 1)
screen = pygame.display.set_mode([WINDOWS] * 2)

mapa = {(posx, posy): (i, j) for posx, i in enumerate(range(0, WINDOWS, TILE_SIZE), start=1) for posy, j in
        enumerate(range(0, WINDOWS, TILE_SIZE), start=1)}

FPS = 10
