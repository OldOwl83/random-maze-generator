import pygame as pg

from classes.coordinates import Coordinates, Dimensions, Position


class Board():
    def __init__(self, dimensions: Dimensions, size: Dimensions):
        if (
            not isinstance(dimensions, Dimensions) or 
            not isinstance(size, Dimensions)
        ):
            raise TypeError(
                'The Board parameters must be Dimensions object.'
            )
             
        self._size = size
        
        self._board = {
            Position(
                x, y,
                pg.Rect(
                    (size.left.x) / dimensions.x * x,
                    (size.up.y) / dimensions.y * y,
                    (size.left.x) / dimensions.x,
                    (size.up.y) / dimensions.y
                )
            ): []
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

    def get_connected_neighbors(self, position: Coordinates):
        return self._board[position]
        
    def get_free_neighbors(self, position: Coordinates):
        return tuple(
            pos for pos in (
                position.up, position.down, position.left, position.right
            ) if not self._board.get(pos, True)
        )
    
    def connect_neighbor(self, position: Coordinates, neighbor: Coordinates):
        self._board.get(position).append(neighbor)
        self._board.get(neighbor).append(position)

    def get_shortest_path(self, start: Coordinates, finish: Coordinates):
        test_board = {}
        for pos, neigh in self._board.items():
            test_board.update({pos: neigh.copy()})
            
        test_steps = []
        
        previous_forks = []
        
        while start != finish:
            current_neighbors = test_board[start]
            
            if len(current_neighbors) > 0:
                test_steps.append(start)
                
                if len(current_neighbors) > 1:
                    previous_forks.append(start)
                
                next = test_board[start].pop()
                test_board[next].remove(start)
                start = next
            
            else:
                if start in previous_forks:
                    previous_forks.pop()
                    
                start = previous_forks[-1]
                
                test_steps = test_steps[:test_steps.index(start) + 1]
        
        return test_steps                   

    def get_surface(self):
        surface = pg.Surface(self._size)
        surface.fill('green')
        rect = pg.Rect((0, 0), self._size)

        pg.draw.lines(
            surface, 
            'darkred', 
            False, 
            [rect.bottomleft, rect.topleft, rect.topright],
            3
        )

        # Imprimo paredes internas
        for pos, open_neigh in self._board.items():
            if pos.right not in open_neigh:
                pg.draw.line(
                    surface, 
                    'darkred', 
                    pos.rect.topright, 
                    pos.rect.bottomright,
                    3
                )
            
            if pos.down not in open_neigh:
                pg.draw.line(
                    surface, 
                    'darkred', 
                    pos.rect.bottomleft, 
                    pos.rect.bottomright,
                    3
                )

        return surface
    
    def get_position_rect(self, position: Coordinates):
        positions = tuple(self._board.keys())
        return positions[positions.index(position)].rect

    
    

    
    
    