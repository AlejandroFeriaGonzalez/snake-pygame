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
    desbloqueado = True
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if desbloqueado:
                    if event.key == pygame.K_UP and bloq.direccion != "abajo":
                        bloq.direccion = 'arriba'
                    elif event.key == pygame.K_DOWN and bloq.direccion != "arriba":
                        bloq.direccion = 'abajo'
                    elif event.key == pygame.K_LEFT and bloq.direccion != "derecha":
                        bloq.direccion = 'izquierda'
                    elif event.key == pygame.K_RIGHT and bloq.direccion != "izquierda":
                        bloq.direccion = 'derecha'
                    desbloqueado = False

        screen.fill('black')  # limpia pantalla
        for i in range(0, WINDOWS, TILE_SIZE):
            for j in range(0, WINDOWS, TILE_SIZE):
                pg.draw.rect(screen, 'white', (i, j, TILE_SIZE, TILE_SIZE), 1)

        bloq.update()
        # culebra.update()  # draw incluido en uptade
        # culebra.draw(screen)
        pg.display.flip()

        clock.tick(FPS)
        desbloqueado = True


if __name__ == '__main__':
    main()
