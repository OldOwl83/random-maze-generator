import time

import pygame as pg
from classes.Maze import Maze

pg.init()

screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)

maze = Maze((40, 30), screen)

# for coord, pos in maze._board.items():
#     print(coord, ': ', pos._rect)

running = True
maze._fill_board()
maze._print_walls()
maze._print_main_path()


while running:
    for ev in pg.event.get():
        #print(ev)
        if ev.type == pg.QUIT:
            running = False

    pg.display.flip()

