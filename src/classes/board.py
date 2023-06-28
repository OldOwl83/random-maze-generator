import pygame as pg

from classes.coordinates import Coordinates, Dimensions, Position
from datetime import datetime as dt

class Board():
    def __init__(self, dimensions: Dimensions, size: Dimensions):
        if (
            not isinstance(dimensions, Dimensions) or 
            not isinstance(size, Dimensions)
        ):
            raise TypeError(
                'The Board parameters must be Dimensions object.'
            )
        self._open_neighbors = set() # Se registran los vecinos abiertos a los efectos
                                        # optimizar la función get_open_positions()
        self._size = size
        
        self._board = {
            Coordinates(x, y): Position(
                x, y,
                pg.Rect(
                    (size.left.x) / dimensions.x * x,
                    (size.up.y) / dimensions.y * y,
                    (size.left.x) / dimensions.x,
                    (size.up.y) / dimensions.y
                )
            )
            for y in range(dimensions.y) 
            for x in range(dimensions.x)
        }


    @property
    def is_full(self):
        return all(self._board.values())
    
    @is_full.setter
    def is_full(_, __):
        raise TypeError('The Board properties are immutables.')
    
    @is_full.deleter
    def is_full(_):
        raise TypeError('The Board properties cannot be erased.')
    

    def __str__(self):
        draw_string = ''.join(['--------'] * self.get_dimensions()[0]) + '\n'

        for y in range(self.get_dimensions()[1]):
            for pos in self._board.values():
                if pos.y == y:
                    draw_string += '|' if pos.x == 0 else ''
                    draw_string += ('\t|' 
                                    if not pos.is_neighbor_open(pos.right) 
                                    else '\t ')

            draw_string += '\n'

            for pos in self._board.values():
                if pos.y == y:
                    draw_string += ('--------' 
                                    if not pos.is_neighbor_open(pos.down) 
                                    else '        ')
                
            draw_string += '\n'
                
        return draw_string
    
   
    def get_dimensions(self):
        return max(self._board.keys()).right.down
    
    def get_position(self, position: Coordinates):
        return self._board[position]
    
    def get_all_positions(self):
        return tuple(self._board.values())
    
    def get_open_positions(self):
        return tuple(self._open_neighbors)

    def get_open_neighbors(self, position: Coordinates):
        return self._board[position].get_open_neighbors()
        
    def get_closed_neighbors(self, position: Coordinates):
        return tuple(
            pos for pos in (
                position.up, position.down, position.left, position.right
            ) if not self._board.get(pos, True)
        )
    
    def connect_neighbor(self, position: Coordinates, neighbor: Coordinates):
        self._board.get(position).add_open_neighbor(neighbor)
        self._board.get(neighbor).add_open_neighbor(position)
        
        self._open_neighbors |= {position, neighbor}

    def get_shortest_path_positions(
        self, start: Coordinates, finish: Coordinates
    ):
        test_board = {
            pos: list(pos.get_open_neighbors()) for pos in self._board.values()
        }
        test_steps = []
        previous_forks = []
        
        while start != finish:
            if len(test_board[start]) > 0:
                test_steps.append(start)
                
                if len(test_board[start]) > 1:
                    previous_forks.append(start)
                
                next = test_board[start].pop()
                test_board[next].remove(start)
                start = next
            
            else:                    
                start = previous_forks.pop()
                test_steps = test_steps[:test_steps.index(start)]
        
        return tuple(self._board[step] for step in test_steps)                   


    def get_surface(self):
        surface = pg.Surface(self._size)
        surface.fill('beige')
        rect = pg.Rect((0, 0), self._size)
        line_width = int(rect.width * 0.004)

        pg.draw.lines(
            surface, 
            'darkred', 
            False, 
            [rect.bottomleft, rect.topleft, rect.topright],
            line_width
        )

        # Imprimo paredes internas
        for pos in self._board.values():
            if not pos.is_neighbor_open(pos.right):
                pg.draw.line(
                    surface, 
                    'darkred', 
                    pos.rect.topright, 
                    pos.rect.bottomright,
                    line_width
                )
            
            if not pos.is_neighbor_open(pos.down):
                pg.draw.line(
                    surface, 
                    'darkred', 
                    pos.rect.bottomleft, 
                    pos.rect.bottomright,
                    line_width
                )

        return surface
    
    def get_position_rect(self, position: Coordinates):
        return self._board[position].rect
    
    
    