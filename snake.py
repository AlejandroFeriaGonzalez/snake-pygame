from collections import deque
from random import randrange, randint

import manzana
from conf import *


class Snake:

    def __init__(self, x, y):
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.posicion = [x, y]
        self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]

        self.cuerpo = deque([self])
        self.cabeza = self.cuerpo[0]
        self.direccion = ""  # arriba, abajo, derecha, izquierda
        self.colisiono = False
        self.tiempo_espera_manzana = 0  # si es cero se genera nueva manzana

        self.contador = 0

    def update(self) -> bool:

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

        #  mover culebra
        self.cuerpo.appendleft(Snake(self.posicion[0], self.posicion[1]))

        if self.cabeza.posicion == manzana.manzana_posicion or self.contador <= 1:
            self.contador += 1
            print(self.contador)
            while True:
                manzana.manzana_posicion = [randrange(*RANGE), randrange(*RANGE)]
                if manzana.manzana_posicion in [p.posicion for p in self.cuerpo]:
                    manzana.manzana_posicion = [randrange(*RANGE), randrange(*RANGE)]
                    print("manzana cambio de posicion")
                else:
                    break
            manzana.manzana_rect.topleft = mapa[manzana.manzana_posicion[0], manzana.manzana_posicion[1]]
            self.tiempo_espera_manzana = randint(0, 10)
            self.colisiono = True
        else:
            self.cuerpo.pop()
            self.colisiono = False

        #  detectar colision
        posiciones_partes = []
        for parte in self.cuerpo:
            screen.blit(parte.image, parte.rect)  # forma 2
            posiciones_partes.append(parte.posicion)
        # if self.cabeza.posicion in posiciones_partes[1:]:
        #     exit()

        # dibuja manzana
        if self.tiempo_espera_manzana == 0:
            screen.blit(manzana.manzana_surf, manzana.manzana_rect)
        else:
            self.tiempo_espera_manzana -= 1 if self.tiempo_espera_manzana >= 1 else 0
            screen.blit(manzana.manzana_surf, (800, 800))  # saca la manzana del mapa

        return self.colisiono
