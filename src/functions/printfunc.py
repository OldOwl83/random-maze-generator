from typing import Literal

import pygame as pg
from classes.Maze import Maze


def print_walls(surface: pg.Surface, maze: Maze):
    # Imprimo paredes exteriores superior e izquierda
    pg.draw.lines(
        surface, 
        'red', 
        False, 
        [
            maze._rect.bottomleft, maze._rect.topleft, maze._rect.topright
        ],
        3
    )

    # Imprimo paredes internas (siempre la pared derecha e inferior de cada
    # posición, siempre que no comparta el mismo path con su vecina, con
    # orders sucisivos)
    for coord, pos in maze._board.items():
        if not (
            coord[0] + 1 < maze._shape[0]
            and
            (common_path := list(set(pos._paths.keys()) 
            & 
            set(maze._board[coord[0] + 1, coord[1]]._paths.keys())))
            and
            abs(pos._paths[common_path[0]] - maze._board[
                coord[0] + 1, coord[1]]._paths[common_path[0]]) == 1
        ):
            pg.draw.line(
                surface, 
                'red', 
                pos._rect.topright, 
                pos._rect.bottomright,
                2
            )

        if not (
            coord[1] + 1 < maze._shape[1]
            and
            (common_path := list(set(pos._paths.keys()) 
            & 
            set(maze._board[coord[0], coord[1] + 1]._paths.keys())))
            and
            abs(pos._paths[common_path[0]] - maze._board[
                coord[0], coord[1] + 1]._paths[common_path[0]]) == 1
        ):
            pg.draw.line(
                surface, 
                'red', 
                pos._rect.bottomleft, 
                pos._rect.bottomright,
                2
            )

    # Imprimo las puertas
    # Entrada
    pg.draw.line(
        surface, 
        'blue', 
        maze._board[maze._paths[0][0]]._rect.topleft,
        maze._board[maze._paths[0][0]]._rect.bottomleft,
        4
    )

    pg.draw.line(
        surface, 
        'blue', 
        maze._board[maze._paths[0][-1]]._rect.topright,
        maze._board[maze._paths[0][-1]]._rect.bottomright,
        4
    )


def print_main_path(surface: pg.Surface, maze: Maze):
    for coord in maze._paths[0]:
        pg.draw.circle(
            surface, 
            'green',
            maze._board[coord]._rect.center,
            1
        )


def print_marble(surface: pg.Surface, maze: Maze, marble_image: pg.Surface):
    marble_x = maze._marble['center'][0] - marble_image.get_rect().width / 2
    marble_y = maze._marble['center'][1] - marble_image.get_rect().height / 2
    surface.blit(marble_image, (marble_x, marble_y))


def print_button(
    surface: pg.Surface, 
    position: pg.Rect, 
    font: pg.font.Font,
    text: str,
    font_color: str,
    button_color: Literal['violet', 'yellow']
):   
    pg.draw.rect(surface, button_color, position, 0, border_radius=3)

    reset_text = pg.font.Font.render(font, text, False, font_color)

    surface.blit(reset_text, reset_text.get_rect(center=position.center).topleft) 

