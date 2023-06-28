import pygame as pg

import classes.env_vars as env
from classes.maze import Maze
from classes.coordinates import Dimensions

class MazeGame: 
    def __init__(self, maze_dimensions: Dimensions):
        title = "Random Maze Generator"
        icon = f'{env.resources_path}bolita64.png'
        screen_mode = pg.FULLSCREEN

        pg.font.init()
        pg.display.set_caption(title)
        pg.display.set_icon(pg.image.load(icon))
        self._screen = pg.display.set_mode(flags=screen_mode)
        self._screen.fill('orange')
        self._screen_dimensions = Dimensions(
            self._screen.get_rect().width, self._screen.get_rect().height
        )
        
        self._maze_dimensions = maze_dimensions
        self._create_maze()

        self._running = True

        self._banner_size = self._screen_dimensions * (.1, .06)
        self._button_color = '#666666'
        self._button_hover_color = '#bbbbbb'
        self._buttons = (
            Button('Reset', self._banner_size, self._create_maze),
            Button('Toggle solution', self._banner_size, self._toggle_solution),
            Button('Quit', self._banner_size, self._quit)
        )


    def _create_maze(self):
        self._maze = Maze(self._maze_dimensions, self._screen_dimensions * 0.8)

    def _toggle_solution(self):
        self._maze.toggle_solution()

    def _quit(self):
        self._running = False


    def start_game(self):
        while self._running:
            self._screen.blit(
                self._maze.get_surface(), self._screen_dimensions * (.1, .14)
            )
            buttons = {
                button: self._screen.blit(
                    button.get_surface(), 
                    self._screen_dimensions * (.12 * i, .05)
                )
                for i, button in enumerate(self._buttons, 1)
            }

            self._screen.blit(
                Banner(
                    f'Steps: {self._maze.step_counter}/{self._maze.solution_steps_count}',
                    self._banner_size
                ).get_surface(), 
                self._screen_dimensions * (.12 * 6, .05)
            )

            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    self._running = False
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
                    for button, rect in buttons.items():
                        if rect.collidepoint(ev.pos):
                            button.color = self._button_hover_color
                        else:
                            button.color = self._button_color

                if ev.type == pg.MOUSEBUTTONDOWN:
                    for button, rect in buttons.items():
                        if rect.collidepoint(ev.pos):
                            button.callback(*button.callback_args)

            pg.display.update()


class Banner:
    def __init__(self, text:str, size: Dimensions):
        self._text = pg.font.Font.render(
            pg.font.Font(pg.font.get_default_font(), int(size.x * .12)), 
            text, False, 'beige'
        )
        
        self._size = size
        self.color = '#000000'

    def get_surface(self):
        surface = pg.Surface(self._size)
        surface.fill(self.color)
        surface.blit(
            self._text,
            self._text.get_rect(center=surface.get_rect().center).topleft
        )

        return surface
    

class Button(Banner):
    def __init__(self, text:str, size: Dimensions, callback, *args):
        super().__init__(text, size)
        self.callback = callback
        self.callback_args = args

