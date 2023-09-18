from collections import deque

import pygame.draw

from constantes import *


class Bloque:

    def __init__(self, x, y, direc):

        self.relentizacion = 10
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.posicion = [x, y]

        # self.cuerpo = deque([self])

        self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]

        self.direccion = direc  # arriba, abajo, derecha, izquierda

    def update(self) -> None:
        if self.direccion == "arriba":
            self.posicion[1] -= 1
        elif self.direccion == "abajo":
            self.posicion[1] += 1
        elif self.direccion == "izquierda":
            self.posicion[0] -= 1
        elif self.direccion == "derecha":
            self.posicion[0] += 1
        # verifica si salio del mapa
        if (self.posicion[0] < 1 or self.posicion[1] < 1
                or self.posicion[0] > WINDOWS // TILE_SIZE or self.posicion[1] > WINDOWS // TILE_SIZE):
            pygame.quit()
            exit()

        pygame.draw.rect(screen, "green", self.rect)

        # self.cuerpo.appendleft(Bloque(*self.posicion))
        # # print([c.rect for c in self.cuerpo])
        #
        # if self.cuerpo[0].posicion == [2, 2]:
        #     pass
        # else:
        #     self.cuerpo.pop()

        # for parte in self.cuerpo:
        #     pygame.draw.rect(screen, "green", parte.rect)
