from Coordinates import Coordinates
from Position import Position

dimensions = tuple[int, int]

class Board():
    def __init__(self, dimensions: dimensions):
        if (
            not isinstance(dimensions, tuple) or len(dimensions) != 2 or
            not isinstance(dimensions[0], int) or 
            not isinstance(dimensions[1], int)
        ):
            raise TypeError(
                'The "dimensions" parameter must be a tuple with two integers.'
            )
        
        if (dimensions[0] < 0 or dimensions[1] < 0):
            raise ValueError(
                'The coordinates of the dimensions parameter must be '
                'positive integers.'
            )
            
        self._board = {
            Coordinates(x, y): Position()
            for y in range(dimensions[1]) 
            for x in range(dimensions[0]) 
        }
        
        def get_position(self, coordinates: Coordinates):
            if not isinstance(coordinates, Coordinates):
                raise TypeError (
                    'The "coordinates" parameter must be a Coordinates object.'
                )
            
            return self._board.get(coordinates)
        
        def add_path_order(self, coordinates: Coordinates, path: int, order: int):
            if not isinstance(coordinates, Coordinates):
                raise TypeError (
                    'The "coordinates" parameter must be a Coordinates object.'
                )
                
            if (
                not isinstance(path, int) or not isinstance(order, int) or 
                path < 0 or order < 0
            ):
                raise ValueError(
                    'The "path" and "order" arguments must be positive integers.'
                )
            
            self._board[coordinates].add_path(path, order)