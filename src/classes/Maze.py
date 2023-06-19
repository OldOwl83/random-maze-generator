import random as rdm
from typing import Literal

import pygame as pg

from classes.Position import Position
from classes.Board import Board


# Type hints
dimension = coordinates = tuple[int, int]

#direction = Literal['up', 'down', 'left', 'right']


class Maze:
    def __init__(
        self, 
        dim: dimension,
        # screen_rect: pg.Rect,
        # proportion: float=.8
    ) -> None:    

        # self._rect = pg.Rect(
        #     (
        #         screen_rect.width * (1 - proportion) / 2,
        #         screen_rect.height * (1 - proportion) / 2
        #     ),
        #     (
        #         screen_rect.width * proportion, 
        #         screen_rect.height * proportion
        #     )
        # )

        self._board = Board(dim)

        self._trace_maze()

        # self._marble = {max_position[0] + 1
        #     'coord': self._path_initials[0][0],
        #     'center': self._board[self._path_initials[0][0]]._rect.center
        # }

    
    def __str__(self):
        return str(self._board)
        

    def _trace_maze(self):

        while not self._board.is_full:
            self._trace_path(
                rdm.choice(
                    self._board.get_open_positions() or 
                    self._board.get_all_positions()
                )
            )


    def _trace_path(self, init_position: Position):
        while free_neighbors := self._board.get_free_neighbors(init_position):
        
            next_position = rdm.choice(free_neighbors)
            self._board.connect_neighbor(init_position, next_position)
            init_position = next_position

    
    # def move_marble(self, direction: Direction):
    #     current_x, current_y = self._marble['coord']

    #     if direction == 'up':
    #         new_coord = current_x, current_y - 1 if current_y > 0 else current_y
    #     elif direction == 'down':
    #         new_coord = current_x, current_y + 1 \
    #             if current_y < self._shape[1] - 1 else current_y
    #     elif direction == 'left':
    #         new_coord = current_x - 1 if current_x > 0 else current_x, current_y
    #     elif direction == 'right':
    #         new_coord = current_x + 1 if current_x < self._shape[0] - 1 \
    #             else current_x, current_y
    #     else:
    #         raise ValueError(
    #             '"direction" sólo acepta "up", "down", "left" y'
    #             ' "right" como argumentos.'
    #         )
        
    #     if (
    #         (common_path := list(
    #             set(self._board[self._marble['coord']]._path_initials.keys()) 
    #             & 
    #             set(self._board[new_coord]._path_initials.keys())))
    #         and
    #         abs(self._board[self._marble['coord']]._path_initials[common_path[0]] - 
    #             self._board[new_coord]._path_initials[common_path[0]]) == 1
    #     ):
    #         self._marble['coord'] = new_coord
    #         self._marble['center'] = self._board[
    #             self._marble['coord']]._rect.center

    #     return self._marble['center']
