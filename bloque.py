from random import randrange
from typing import Any

import pygame

from constantes import *


class Bloque(pygame.sprite.Sprite):

    def __init__(self, color: str, *groups):
        super().__init__(*groups)

        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.fill(color)
        self.posicion = [randrange(*RANGE), randrange(*RANGE)]
        self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]

        self.direccion = ""  # arriba, abajo, derecha, izquierda

    def input(self):
        keys = pygame.key.get_pressed()
        try:
            if keys[pygame.K_UP]:
                self.posicion[1] -= 1
            if keys[pygame.K_DOWN]:
                self.posicion[1] += 1
            if keys[pygame.K_LEFT]:
                self.posicion[0] -= 1
            if keys[pygame.K_RIGHT]:
                self.posicion[0] += 1

            self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]
        except KeyError:
            pass
            # perdio por salir del mapa
            # exit()

    def movimiento(self):
        pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.input()
