from Position import Position

dimensions = coordinates = tuple[int, int]

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
            
        self._board = sorted(tuple(
            Position(x, y)
            for y in range(dimensions[1]) 
            for x in range(dimensions[0]) 
        ))
        
    def _get_all_positions(self):
        return self._board
    
    def is_empty(self):
        return not any(self._board)
        
    def get_position(self, coordinates: coordinates):
        if not isinstance(coordinates, tuple):
            raise TypeError (
                'The "coordinates" parameter must be a tuple with two positive integers.'
            )
        
        return self._board[self._board.index(coordinates)]
    
    def set_path_step(
        self, coordinates: coordinates, path: int, next: Position=None
    ):
        if not isinstance(coordinates, tuple):
            raise TypeError (
                'The "coordinates" parameter must be a tuple with two positive integers.'
            )
            
        if not isinstance(path, int):
            raise TypeError(
                'The "path" parameter type must be integer.'
            )
        
        if path < 0:
            raise ValueError(
                'The "path" parameter must be a positive integer.'
            )
        
        if not isinstance(next, Position):
            raise TypeError(
                'The "position" parameter must be a Position object.'
            )
            
        self.get_position[coordinates].add_path(path, next)

    def remove_path(self, path, initial_coord):
        current_position = self._board.get_position(initial_coord)
        while current_position.paths.get(path):
            