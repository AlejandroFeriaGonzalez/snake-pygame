import pygame as pg

from constantes import *

screen = pg.display.set_mode([WINDOWS] * 2)
clock = pg.Clock()
bloque = pg.Rect(0, 0, 50, 50)
culebra = []


def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        screen.fill('black')  # limpia pantalla
        for i in range(0, WINDOWS, TILE_SIZE):
            for j in range(0, WINDOWS, TILE_SIZE):
                pg.draw.rect(screen, 'white', (i, j, 50, 50), 1)

        pg.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    main()
