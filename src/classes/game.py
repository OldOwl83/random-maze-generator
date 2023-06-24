import pygame as pg

import classes.env_vars as env
from classes.maze import Maze
from classes.coordinates import Dimensions

class MazeGame: 
    def __init__(self, screen_resolution, maze_dimensions):
        self._title = "Random Maze Generator"
        self._icon = f'{env.resources_path}/bolita64.png'
        self._resolution = screen_resolution
        self._maze_dimensions = maze_dimensions
        self._create_maze()

        self._buttons = (
            Button(
                'Reset', 
                pg.Rect(
                    self._resolution.x * .88, 
                    1 * self._resolution.y / 10,
                    screen_resolution.x * .1,
                    screen_resolution.y * .07
                ), 
                self._create_maze
            ),
            Button(
                'Toggle solution', 
                pg.Rect(
                    self._resolution.x * .88, 
                    2 * self._resolution.y / 10,
                    screen_resolution.x * .1,
                    screen_resolution.y * .07
                ), 
                self._toggle_solution
            )
        )


    def _create_maze(self):
        self._maze = Maze(self._maze_dimensions, self._resolution * 0.8)

    def _toggle_solution(self):
        self._maze.toggle_solution()


    def start_game(self):
        pg.display.set_caption(self._title)
        pg.display.set_icon(pg.image.load(self._icon))
        screen = pg.display.set_mode(self._resolution)
        
        running = True

        while running:
            screen.blit(self._maze.get_surface(), self._resolution * 0.5)
            for button in self._buttons:
                screen.blit(
                    button.get_surface(), 
                    button.rect.topleft
                )

            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    running = False

                if ev.type == pg.KEYDOWN:
                    if ev.key == pg.K_LEFT:
                        self._maze.move_left()
                    elif ev.key == pg.K_RIGHT:
                        self._maze.move_right()
                    elif ev.key == pg.K_UP:
                        self._maze.move_up()
                    elif ev.key == pg.K_DOWN:
                        self._maze.move_down()

                if ev.type == pg.MOUSEMOTION:
                    for button in self._buttons:
                        if button.rect.collidepoint(ev.pos):
                            button.color = '#999999'
                        else:
                            button.color = 'red'

                if ev.type == pg.MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        if button.rect.collidepoint(ev.pos):
                            button._callback()

            pg.display.update()


class Button:
    def __init__(self, text:str, rect: pg.Rect, callback, *args):
        pg.font.init()

        self._text = pg.font.Font.render(
            pg.font.Font(pg.font.get_default_font(), 12), 
            text, False, 'blue'
        )
        self._callback = callback

        self.rect = rect
        self.color = 'red'

    def get_surface(self):
        surface = pg.Surface(self.rect.size)
        surface.fill(self.color)
        surface.blit(
            self._text,
            self._text.get_rect(center=surface.get_rect().center).topleft
        )

        return surface
