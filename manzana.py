from random import randrange
from constantes import *
import pygame

manzana_surf = pygame.Surface((50, 50))
manzana_surf.fill("red")
manzana_rect = manzana_surf.get_rect()
manzana_posicion = [randrange(*RANGE), randrange(*RANGE)]
manzana_rect.topleft = mapa[manzana_posicion[0], manzana_posicion[1]]
