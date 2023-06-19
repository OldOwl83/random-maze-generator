from classes.Position import Position

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
            
        self._board = {
            Position(x, y): []
            for y in range(dimensions[1]) 
            for x in range(dimensions[0])
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
            for pos in self._board.keys():
                if pos[1] == y:
                    draw_string += '|' if pos[0] == 0 else ''
                    draw_string += '\t|' if pos.right not in self._board[pos] else '\t '

            draw_string += '\n'

            for pos in [x for x in self._board.keys() if x[1] == y]:
                draw_string += '--------' if pos.down not in self._board[pos] else '        ' 
                
            draw_string += '\n'
                
        return draw_string
    

    def get_dimensions(self):
        return max(self._board.keys()).right.down
    
    def get_all_positions(self):
        return tuple(self._board.keys())
    
    def get_open_positions(self):
        return tuple(pos for pos, conn_neigh in self._board.items() 
                     if conn_neigh)

    def get_free_neighbors(self, position: Position):
        return tuple(
            pos for pos in (
                position.up, position.down, position.left, position.right
            ) if not self._board.get(pos, True)
        )
    
    def connect_neighbor(
        self, position: Position|coordinates, neighbor: Position|coordinates
    ):
        self._board.get(position).append(neighbor)
        self._board.get(neighbor).append(position)

    
    

    
    
    