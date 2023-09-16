WINDOWS = 800
TILE_SIZE = 50
RANGE = (1, (WINDOWS//TILE_SIZE)+1)

mapa = {(posx, posy): (i, j) for posx, i in enumerate(range(0, WINDOWS, TILE_SIZE), start=1) for posy, j in
        enumerate(range(0, WINDOWS, TILE_SIZE), start=1)}
