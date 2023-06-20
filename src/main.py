import pygame as pg
from classes.maze import Maze
from classes.coordinates import Coordinates, Dimensions, Position
from functions.printfunc import *


pg.init()

pg.display.set_caption("Random Maze")
icono = pg.image.load("../resources/bolita24.png")
pg.display.set_icon(icono)
screen = pg.display.set_mode((800, 600))
screen_rect = screen.get_rect()

maze_width = 24
maze_height = 20
maze = Maze(Dimensions(maze_width, maze_height), Dimensions(760, 560))

# pos_size = maze._board[0, 0]._rect.width, maze._board[0, 0]._rect.height
# marble_size = [size for size in [(64, 64), (32, 32), (24, 24), (16, 16)] 
#                  if size < pos_size]
# marble_size = marble_size[0][0] if marble_size else 16
# marble_image = pg.image.load(f'../resources/bolita{marble_size}.png')

# reset_font = pg.font.Font(pg.font.get_default_font(), 11)
# reset_button_color = 'violet'
# reset_button_rect = pg.Rect(
#         (maze._rect.bottomright[0] + (screen.get_rect().width - maze._rect.width) / 2 * .2,
#         maze._rect.bottomright[1] - (screen.get_rect().height - maze._rect.height) / 2 * .8),
#         ((screen.get_rect().width - maze._rect.width) / 2 * .6,
#         (screen.get_rect().width - maze._rect.width) / 2 * .4)
#     )

running = True
finished = False
maze_sur = maze._board.get_surface()

while running:
    screen.blit(maze_sur, (10, 10))

    # screen.fill('black')
    # print_walls(screen, maze)
    # print_marble(screen, maze, marble_image)
    # print_button(
    #     screen, reset_button_rect, reset_font, 'Reset',
    #     'red', reset_button_color
    # )

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False

        # if ev.type == pg.KEYDOWN and not finished:
        #     print_walls(screen, maze)
            
        #     if ev.key == pg.K_LEFT:
        #         maze.move_marble('left')
        #     elif ev.key == pg.K_RIGHT:
        #         maze.move_marble('right')
        #     elif ev.key == pg.K_UP:
        #         maze.move_marble('up')
        #     elif ev.key == pg.K_DOWN:
        #         maze.move_marble('down')


        # if ev.type == pg.MOUSEMOTION:
        #     if reset_button_rect.collidepoint(ev.pos):
        #         reset_button_color = 'yellow'
        #     else:
        #         reset_button_color = 'violet'

        # if ev.type == pg.MOUSEBUTTONDOWN:
        #     if reset_button_rect.collidepoint(ev.pos):
        #         maze = Maze((maze_width, maze_height), screen_rect, .8)
        #         finished = False


    # if maze._marble['coord'] == maze._paths[0][-1]:
    #     print_main_path(screen, maze)

    #     finished = True

    pg.display.update()
