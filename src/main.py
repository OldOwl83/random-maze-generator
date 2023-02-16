import pygame as pg
from classes.Maze import Maze
from functions.printfunc import print_main_path, print_walls


pg.init()

screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)

maze = Maze((18, 15), screen.get_rect())

marble = pg.image.load('../resources/bolita32.png')

print_walls(screen, maze)
screen.blit(marble, maze._marble['topleft'])

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
                screen.blit(marble, maze.move_marble('left'))
            elif ev.key == pg.K_RIGHT:
                screen.blit(marble, maze.move_marble('right'))
            elif ev.key == pg.K_UP:
                screen.blit(marble, maze.move_marble('up'))
            elif ev.key == pg.K_DOWN:
                screen.blit(marble, maze.move_marble('down'))

            pg.display.update()

    if maze._marble['coord'] == maze._paths[0][-1]:
        print_walls(screen, maze)
        screen.blit(marble, maze._marble['topleft'])
        print_main_path(screen, maze)
        finished = True

        pg.display.update()

