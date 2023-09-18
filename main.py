from random import randrange

from conf import *
from snake import Snake


def main():
    pygame.init()
    clock = pygame.time.Clock()
    culebra = Snake(randrange(*RANGE), randrange(*RANGE))
    fps = 10

    puntos = 0
    fondo = pygame.font.SysFont("verdana", 15)
    fondo_surf = fondo.render(f'Puntos: {puntos}    Velocidad: {round(clock.get_fps())}', True, "white")
    fondo_rect = fondo_surf.get_rect()
    fondo_rect.topleft = (5, 5)  # poscion del texto

    desbloqueado = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if desbloqueado:
                    if event.key == pygame.K_UP and culebra.direccion != "abajo":
                        culebra.direccion = 'arriba'
                    elif event.key == pygame.K_DOWN and culebra.direccion != "arriba":
                        culebra.direccion = 'abajo'
                    elif event.key == pygame.K_LEFT and culebra.direccion != "derecha":
                        culebra.direccion = 'izquierda'
                    elif event.key == pygame.K_RIGHT and culebra.direccion != "izquierda":
                        culebra.direccion = 'derecha'
                    desbloqueado = False

        screen.fill('black')  # limpia pantalla
        for i in range(0, WINDOWS, TILE_SIZE):
            for j in range(0, WINDOWS, TILE_SIZE):
                pygame.draw.rect(screen, 'white', (i, j, TILE_SIZE, TILE_SIZE), 1)

        colisiono = culebra.update()
        if colisiono:
            # dibujar puntos
            puntos += 1
            fps += 1

        fondo_surf = fondo.render(f'Puntos: {puntos}    Velocidad: {round(clock.get_fps())}', True, "white")
        screen.blit(fondo_surf, fondo_rect)
        pygame.display.flip()

        clock.tick(fps)
        desbloqueado = True


if __name__ == '__main__':
    main()
