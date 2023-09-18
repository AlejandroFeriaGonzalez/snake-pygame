from collections import deque

from constantes import *


class Bloque:

    def __init__(self, x, y):

        self.relentizacion = 10
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.posicion = [x, y]

        self.cuerpo = deque([self])

        self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]

        self.direccion = ""  # arriba, abajo, derecha, izquierda
        self.contador = 0

    # def input(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_UP] and self.direccion != "abajo":
    #         return "arriba"
    #     elif keys[pygame.K_DOWN] and self.direccion != "arriba":
    #         return "abajo"
    #     elif keys[pygame.K_LEFT] and self.direccion != "derecha":
    #         return "izquierda"
    #     elif keys[pygame.K_RIGHT] and self.direccion != "izquierda":
    #         return "derecha"
    #     # self.rect.topleft = mapa[(self.posicion[0], self.posicion[1])]
    #     return self.direccion

    def movimiento(self):
        pass

    def update(self) -> None:
        self.contador += 1
        # self.direccion = self.input()

        # if self.contador > self.relentizacion:

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

        self.contador = 0
        self.cuerpo.appendleft(Bloque(*self.posicion))
        # print([c.rect for c in self.cuerpo])

        if self.cuerpo[0].posicion == [2, 2]:
            pass
        else:
            self.cuerpo.pop()

        for parte in self.cuerpo:
            pygame.draw.rect(screen, "green", parte.rect)
