import pygame as pg
from classes.Maze import Maze
from functions.printfunc import *


pg.init()

screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)
pg.display.set_caption("Random Maze")
icono = pg.image.load("../resources/bolita24.png")
pg.display.set_icon(icono)

maze = Maze((26, 20), screen.get_rect())
print_walls(screen, maze)

pos_size = maze._board[0, 0]._rect.width, maze._board[0, 0]._rect.height
marble_size = [size for size in [(64, 64), (32, 32), (24, 24), (16, 16)] 
                 if size < pos_size][0][0]
marble_image = pg.image.load(f'../resources/bolita{marble_size}.png')

print_marble(screen, maze, marble_image)

pg.display.flip()

running = True
finished = False

while running:
    screen.fill('black')

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False

        if ev.type == pg.KEYDOWN and not finished:
            print_walls(screen, maze)
            
            if ev.key == pg.K_LEFT:
                maze.move_marble('left')
            elif ev.key == pg.K_RIGHT:
                maze.move_marble('right')
            elif ev.key == pg.K_UP:
                maze.move_marble('up')
            elif ev.key == pg.K_DOWN:
                maze.move_marble('down')

            print_marble(screen, maze, marble_image)

            pg.display.update()

    if maze._marble['coord'] == maze._paths[0][-1]:
        print_walls(screen, maze)
        print_main_path(screen, maze)
        print_marble(screen, maze, marble_image)
        finished = True

        pg.display.update()

