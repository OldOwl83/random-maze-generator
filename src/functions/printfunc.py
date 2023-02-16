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
        ])

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
                pos._rect.bottomright)

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
                pos._rect.bottomright)

    # Imprimo las puertas
    # Entrada
    pg.draw.line(
        surface, 
        'blue', 
        maze._board[maze._paths[0][0]]._rect.topleft,
        maze._board[maze._paths[0][0]]._rect.bottomleft,
        3
    )

    pg.draw.line(
        surface, 
        'blue', 
        maze._board[maze._paths[0][-1]]._rect.topright,
        maze._board[maze._paths[0][-1]]._rect.bottomright,
        3
    )

def print_main_path(surface: pg.Surface, maze: Maze):
    for coord in maze._paths[0]:
        pg.draw.circle(
            surface, 
            'green',
            maze._board[coord]._rect.center,
            1
        )