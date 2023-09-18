from collections import deque
from random import randrange

import pygame as pg
import pygame.time

from bloque import Bloque
from constantes import *

clock = pygame.time.Clock()
# culebra = pg.sprite.Group()
bloq = Bloque(randrange(*RANGE), randrange(*RANGE))

# cola = bloque.Bloque('green', culebra)

manzana = pg.sprite.GroupSingle()


def main():
    global nuevox, nuevoy
    desbloqueado = True
    cuerpo = deque([bloq])
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pygame.K_UP and cuerpo[0].direccion != "abajo":
                    cuerpo[0].direccion = 'arriba'
                elif event.key == pygame.K_DOWN and cuerpo[0].direccion != "arriba":
                    cuerpo[0].direccion = 'abajo'
                elif event.key == pygame.K_LEFT and cuerpo[0].direccion != "derecha":
                    cuerpo[0].direccion = 'izquierda'
                elif event.key == pygame.K_RIGHT and cuerpo[0].direccion != "izquierda":
                    cuerpo[0].direccion = 'derecha'

        screen.fill('black')  # limpia pantalla
        for i in range(0, WINDOWS, TILE_SIZE):
            for j in range(0, WINDOWS, TILE_SIZE):
                pg.draw.rect(screen, 'white', (i, j, TILE_SIZE, TILE_SIZE), 1)

        if cuerpo[0].direccion == "arriba":
            nuevoy = cuerpo[0].posicion[1] - 1
            nuevox = cuerpo[0].posicion[0]
        elif cuerpo[0].direccion == "abajo":
            nuevoy = cuerpo[0].posicion[1] + 1
            nuevox = cuerpo[0].posicion[0]
        elif cuerpo[0].direccion == "izquierda":
            nuevox = cuerpo[0].posicion[0] - 1
            nuevoy = cuerpo[0].posicion[0]
        elif cuerpo[0].direccion == "derecha":
            nuevox = cuerpo[0].posicion[0] + 1
            nuevoy = cuerpo[0].posicion[0]
        else:
            nuevox = cuerpo[0].posicion[0]
            nuevoy = cuerpo[0].posicion[0]
        # verifica si salio del mapa
        if (cuerpo[0].posicion[0] < 1 or cuerpo[0].posicion[1] < 1
                or cuerpo[0].posicion[0] > WINDOWS // TILE_SIZE or cuerpo[0].posicion[1] > WINDOWS // TILE_SIZE):
            pygame.quit()
            exit()

        cuerpo.appendleft(Bloque(nuevox, nuevoy))
        if cuerpo[0].posicion == [2, 2]:
            pass
        else:
            cuerpo.pop()

        for parte in cuerpo:
            pygame.draw.rect(screen, "green", parte.rect)
        pg.display.flip()

        clock.tick(FPS)


if __name__ == '__main__':
    main()
