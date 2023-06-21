import pygame as pg

from classes.maze import Maze
from classes.coordinates import Dimensions

class MazeGame: 
    def __init__(self, title, icon, screen_resolution, maze_dimensions):
        self._title = title
        self._icon = icon
        self._resolution = screen_resolution
        self._maze = Maze(
            maze_dimensions, 
            Dimensions(760, 540)
        )
    
    def start_game(self):

        pg.display.set_caption(self._title)
        icono = pg.image.load(self._icon)
        pg.display.set_icon(icono)
        screen = pg.display.set_mode(self._resolution)
        
        running = True
        finished = False
        maze_sur = self._maze._board.get_surface()

        while running:
            screen.blit(maze_sur, (10, 10))


            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    running = False


            pg.display.update()
