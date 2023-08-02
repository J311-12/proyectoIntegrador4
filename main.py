#Proyecto integrador parte 4

import os
import readchar

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_map(mapa):
    clear_screen()
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa, pos_inicial, pos_final):
    px, py = pos_inicial

    while (px, py) != pos_final:
        mapa[py][px] = 'P'
        print_map(mapa)

        tecla = readchar.readkey()
        mapa[py][px] = '.'

        if tecla == '\x1b[A':  # Flecha arriba
            nueva_py = py - 1
            if nueva_py >= 0 and mapa[nueva_py][px] != '#':
                py = nueva_py
        elif tecla == '\x1b[B':  # Flecha abajo
            nueva_py = py + 1
            if nueva_py < len(mapa) and mapa[nueva_py][px] != '#':
                py = nueva_py
        elif tecla == '\x1b[D':  # Flecha izquierda
            nueva_px = px - 1
            if nueva_px >= 0 and mapa[py][nueva_px] != '#':
                px = nueva_px
        elif tecla == '\x1b[C':  # Flecha derecha
            nueva_px = px + 1
            if nueva_px < len(mapa[0]) and mapa[py][nueva_px] != '#':
                px = nueva_px

    mapa[py][px] = 'P'
    print_map(mapa)
    print("¡Has llegado al final del laberinto!")

# Ejemplo de uso
laberinto = "#####.#....#\n#.....#.###.\n###.#.###.#.\n#...#.....#\n###.#######\n"
mapa = [list(fila) for fila in laberinto.split("\n")]
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0])-1, len(mapa)-1)

main_loop(mapa, posicion_inicial, posicion_final)

