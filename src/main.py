import pygame as pg
from classes.Maze import Maze

pg.init()

screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)

maze = Maze(30, 30)
maze._set_rect(screen.get_rect())


running = True

while running:
    

    for ev in pg.event.get():
        #print(ev)
        if ev.type == pg.QUIT:
            running = False

    pg.draw.rect(screen, (200, 200, 200), maze._rect)

    pg.display.flip()

