import time

import pygame as pg
from classes.Maze import Maze
from functions.printfunc import print_main_path, print_walls

pg.init()

screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)

maze = Maze((18, 15), screen.get_rect())

marble = pg.image.load('../resources/bolita32.png')
marble_x, marble_y = maze._marble['topleft']

move_marble_x = move_marble_y = 0
move_rate = .7

running = True
moving = False

while running:
    screen.fill('black')

    for ev in pg.event.get():
        #print(ev)
        if ev.type == pg.QUIT:
            running = False

        if ev.type == pg.KEYDOWN:
            moving = True

            if ev.key == pg.K_LEFT:
                move_marble_x = -move_rate
            elif ev.key == pg.K_RIGHT:
                move_marble_x = move_rate
            elif ev.key == pg.K_UP:
                move_marble_y = -move_rate
            elif ev.key == pg.K_DOWN:
                move_marble_y = move_rate

        if ev.type == pg.KEYUP:
            moving = True

            if ev.key == pg.K_LEFT or ev.key == pg.K_RIGHT:
                move_marble_x = 0
            elif ev.key == pg.K_UP or ev.key == pg.K_DOWN:
                move_marble_y = 0

    print_walls(screen, maze)
    
    marble_x += move_marble_x
    marble_y += move_marble_y

    screen.blit(marble, (marble_x, marble_y))

    pg.display.update()

