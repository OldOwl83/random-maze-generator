import random as rdm
from typing import Literal

import pygame as pg

from classes.coordinates import Position, Coordinates, Dimensions
from classes.board import Board

from datetime import datetime as dt


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

        self._object_position_ratio = 7/10
        object_size = Dimensions(
            *self._board.get_position_rect((0, 0)).size
        ) * self._object_position_ratio

        self._start = MazeObject(
            Coordinates(0, rdm.choice(range(dimensions.y))),
            object_size, r'../resources/portico.png'
        )
        self._finish = MazeObject(
            Coordinates(dimensions.x - 1, rdm.choice(range(dimensions.y))),
            object_size, r'../resources/portico.png'
        )
        
        self._marble = MazeMovingObject(
            self._start.position,
            object_size, r'../resources/bolita64.png'
        )

        self._finished = False
        self._toggle_solution = False


    def __str__(self):
        return str(self._board)
        

    def _trace_maze(self):
        start = dt.now()
        while not self._board.is_full:
            self._trace_path(
                rdm.choice(
                    self._board.get_open_positions() or 
                    self._board.get_all_positions()
                )
            )
        print(f'trace_maze: {dt.now() - start}')


    def _trace_path(self, init_position: Position):
        while closed_neighbors := self._board.get_closed_neighbors(init_position):
            next_position = rdm.choice(closed_neighbors)
            self._board.connect_neighbor(init_position, next_position)
            init_position = next_position


    def _evaluate_completion(self):
        if self._marble.position == self._finish.position:
            self._finished = True


    def move_up(self):
        if (
            self._marble.position.up in self._board.get_open_neighbors(
                self._marble.position) and not self._finished
        ):
            self._marble.move_up()
            self._evaluate_completion()

    def move_down(self):
        if (
            self._marble.position.down in self._board.get_open_neighbors(
                self._marble.position) and not self._finished
        ):
            self._marble.move_down()
            self._evaluate_completion()

    def move_left(self):
        if (
            self._marble.position.left in self._board.get_open_neighbors(
                self._marble.position) and not self._finished
        ):
            self._marble.move_left()
            self._evaluate_completion()

    def move_right(self):
        if (
            self._marble.position.right in self._board.get_open_neighbors(
                self._marble.position) and not self._finished
        ):
            self._marble.move_right()
            self._evaluate_completion()


    def toggle_solution(self):
        self._toggle_solution = not self._toggle_solution


    def get_surface(self):
        start = dt.now()
        surface = self._board.get_surface()
        margin = (1 - self._object_position_ratio) / 2

        surface.blit(
            self._start.get_surface(), 
            Dimensions(*self._board.get_position_rect(
                self._start.position
            ).topleft) 
            + Dimensions(*self._board.get_position_rect(
                self._start.position
            ).size) * margin
        )

        surface.blit(
            self._finish.get_surface(), 
            Dimensions(*self._board.get_position_rect(
                self._finish.position
            ).topleft) 
            + Dimensions(*self._board.get_position_rect(
                self._finish.position
            ).size) * margin
        )

        surface.blit(
            self._marble.get_surface(), 
            Dimensions(*self._board.get_position_rect(
                self._marble.position
            ).topleft) 
            + Dimensions(*self._board.get_position_rect(
                self._marble.position
            ).size) * margin
        )

        if self._finished or self._toggle_solution:
            self._draw_path(
                surface, 
                self._board.get_shortest_path(
                    self._start.position, self._finish.position
                )
            )
        print(f'get_surface: {dt.now() - start}')
        return surface


    def _draw_path(self, maze_surface: pg.Surface, path: tuple[Position]):
        for pos in path:
            pg.draw.circle(
                maze_surface, 
                'red',
                pos.rect.center,
                5
            )
            
class MazeObject:
    def __init__(self, position: Coordinates, size: Dimensions, image_path: str):
        self._position = position
        self._image = pg.transform.scale(pg.image.load(image_path), size)
        
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(_, __):
        raise AttributeError('The MazeObject properties are immutables.')
    
    @position.deleter
    def position(_):
        raise AttributeError('The MazeObject properties cannot be erased.')
    
    def get_surface(self):
        return self._image


class MazeMovingObject(MazeObject):
    def move_up(self):
        self._position = self._position.up
        
    def move_down(self):
        self._position = self._position.down
        
    def move_left(self):
        self._position = self._position.left
        
    def move_right(self):
        self._position = self._position.right
        
    