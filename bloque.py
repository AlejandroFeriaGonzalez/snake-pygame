from collections import deque
from random import randrange

import pygame

import manzana
from constantes import *


class Bloque:

    def __init__(self, x, y):

        self.relentizacion = 10
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.posicion = [x, y]
        self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]

        self.cuerpo = deque([self])
        self.cabeza = self.cuerpo[0]
        self.direccion = ""  # arriba, abajo, derecha, izquierda

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

        self.cuerpo.appendleft(Bloque(*self.posicion))

        if self.cabeza.posicion == manzana.manzana_posicion:
            manzana.manzana_posicion = [randrange(*RANGE), randrange(*RANGE)]
            manzana.manzana_rect.topleft = mapa[manzana.manzana_posicion[0], manzana.manzana_posicion[1]]
        else:
            self.cuerpo.pop()

        #  detectar colision
        posiciones_partes = []

        for parte in self.cuerpo:
            # pygame.draw.rect(screen, "green", parte.rect)  # forma 1
            screen.blit(parte.image, parte.rect)  # forma 2
            posiciones_partes.append(parte.posicion)
        # print(posiciones_partes)
        if self.cabeza.posicion in posiciones_partes[1:]:
            exit()
        # dibuja manzana
        screen.blit(manzana.manzana_surf, manzana.manzana_rect)
