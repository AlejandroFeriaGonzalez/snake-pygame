from random import randrange
import pygame

from constantes import *


class Bloque(pygame.sprite.Sprite):

    def __init__(self, color: str, *groups):
        super().__init__(*groups)

        self.relentizacion = 10
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.fill(color)
        self.posicion = [randrange(*RANGE), randrange(*RANGE)]

        self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]

        self.direccion = ""  # arriba, abajo, derecha, izquierda
        self.contador = 0

    def input(self):
        keys = pygame.key.get_pressed()
        try:
            if keys[pygame.K_UP] and self.direccion != "abajo":
                self.direccion = "arriba"
            if keys[pygame.K_DOWN] and self.direccion != "arriba":
                self.direccion = "abajo"
            if keys[pygame.K_LEFT] and self.direccion != "derecha":
                self.direccion = "izquierda"
            if keys[pygame.K_RIGHT] and self.direccion != "izquierda":
                self.direccion = "derecha"

            self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]
        except KeyError:
            exit()  # perdio por salir del mapa

    def movimiento(self):
        pass

    def update(self) -> None:
        self.input()
        self.contador += 1
        if self.contador > self.relentizacion:
            if self.direccion == "arriba":
                self.posicion[1] -= 1
            elif self.direccion == "abajo":
                self.posicion[1] += 1
            elif self.direccion == "izquierda":
                self.posicion[0] -= 1
            elif self.direccion == "derecha":
                self.posicion[0] += 1
            self.contador = 0
