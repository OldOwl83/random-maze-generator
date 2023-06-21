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
        
        self._board = Board(dimensions, size)

        self._trace_maze()

        self._start_position = Coordinates(0, rdm.choice(range(dimensions.y)))
        self._finish_position = Coordinates(
            dimensions.x - 1, rdm.choice(range(dimensions.y))
        )
        
        self._marble = Marble(
            self._start_position,
            self._board.get_position_size() * 0.8
        )

    
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


class Marble:
    def __init__(self, initial_position: Coordinates, size: Dimensions):
        self._position = initial_position
        self._image = pg.transform.scale(
            pg.image.load(r'..\resources\portico.png'),
            size
        )
        
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(_, __):
        raise AttributeError('The Marble properties are immutables.')
    
    @position.deleter
    def position(_):
        raise AttributeError('The Marble properties cannot be erased.')
    
    
    def move_up(self):
        self._position = self._position.up
        
    def move_down(self):
        self._position = self._position.down
        
    def move_left(self):
        self._position = self._position.left
        
    def move_right(self):
        self._position = self._position.right
        
    