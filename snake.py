from collections import deque
from random import randrange

import pygame as pg
import pygame.time

from bloque import Bloque
from constantes import *

clock = pygame.time.Clock()
# culebra = pg.sprite.Group()
bloq = Bloque(randrange(*RANGE), randrange(*RANGE), "")

# cola = bloque.Bloque('green', culebra)

manzana = pg.sprite.GroupSingle()


def main():
    desbloqueado = True
    cuerpo = deque([bloq])
    direccion = ""
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if desbloqueado:
                    for parte in cuerpo:
                        if event.key == pygame.K_UP and parte.direccion != "abajo":
                            print("arriba")
                            direccion = 'arriba'
                        elif event.key == pygame.K_DOWN and parte.direccion != "arriba":
                            direccion = 'abajo'
                        elif event.key == pygame.K_LEFT and parte.direccion != "derecha":
                            direccion = 'izquierda'
                        elif event.key == pygame.K_RIGHT and parte.direccion != "izquierda":
                            direccion = 'derecha'
                        desbloqueado = False

        screen.fill('black')  # limpia pantalla
        for i in range(0, WINDOWS, TILE_SIZE):
            for j in range(0, WINDOWS, TILE_SIZE):
                pg.draw.rect(screen, 'white', (i, j, TILE_SIZE, TILE_SIZE), 1)

        for parte in cuerpo:
            parte.update()

        cuerpo.appendleft(Bloque(cuerpo[0].posicion[0], cuerpo[0].posicion[1], direccion))
        if cuerpo[0].posicion == [2, 2]:
            pass
        else:
            cuerpo.pop()

        pg.display.flip()

        clock.tick(FPS)
        desbloqueado = True


if __name__ == '__main__':
    main()
