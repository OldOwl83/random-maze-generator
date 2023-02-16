import time

import pygame as pg
from classes.Maze import Maze
from functions.printfunc import print_main_path, print_walls

pg.init()

screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)

maze = Maze((30, 26), screen.get_rect())

bolita = pg.image.load('../resources/bolita32.png')


running = True

while running:
    for ev in pg.event.get():
        #print(ev)
        if ev.type == pg.QUIT:
            running = False

    print_walls(screen, maze)
    print_main_path(screen, maze)

    pg.display.flip()

