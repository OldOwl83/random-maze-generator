import random as rdm
from typing import Literal

import pygame as pg

from classes.coordinates import Position, Coordinates, Dimensions
from classes.board import Board

#direction = Literal['up', 'down', 'left', 'right']


class Maze:
    def __init__(self, dimensions: Dimensions, size: Dimensions) -> None:    
        if (
            not isinstance(dimensions, Dimensions) or 
            not isinstance(size, Dimensions)
        ):
            raise TypeError(
                'The Maze parameters must be Dimensions object.'
            )
        
        #self._size = size
        
        self._board = Board(dimensions, size)

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


