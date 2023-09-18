import pygame
pygame.font.init()

puntos = 0
fondo = pygame.font.SysFont("verdana", 15)
fondo_surf = fondo.render(f'Puntos {puntos}', True, "white")
fondo_rect = fondo_surf.get_rect()
fondo_rect.topleft = (5, 5)  # poscion del texto
