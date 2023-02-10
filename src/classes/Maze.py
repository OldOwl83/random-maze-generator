from Position import Position
from Location import Location

import random as rdm


class Maze:
    @staticmethod
    def _validate_positive_integer(integer, arg_name: str='(s/n)'):
        if not isinstance(integer, int) or integer < 0:
            raise TypeError(
                f'El argumento pasado como "{arg_name}" debe ser un '
                'entero positivo.'
            )
        
    @staticmethod
    def _validate_boolean(boolean, arg_name: str='(s/n)'):
        if not isinstance(boolean, bool):
            raise TypeError(
                f'El argumento pasado como "{arg_name}" debe ser un '
                'valor booleano.'
            )
        
    @staticmethod
    def _validate_coordinates(coordinate: tuple[int, int], arg_name: str='coordinate'):
        if (
                (not isinstance(coordinate, tuple) or 
                len(coordinate) != 2 or
                not isinstance(coordinate[0], int) or
                coordinate[0] < 0 or
                not isinstance(coordinate[1], int) or 
                coordinate[1] < 0) and coordinate is not None
            ):
            raise TypeError(
                f'El argumento pasado como "{arg_name}" debe ser una tupla '
                'de dos enteros positivos.'
            )
        
    
    def __init__(self, dim_x, dim_y) -> None:
        self._validate_positive_integer(dim_x, 'dim_x')
        self._validate_positive_integer(dim_y, 'dim_y')

        self._board = {(x, y): Location() 
                        for x in range(dim_x) for y in range(dim_y)}
        
        self._path_initial_positions = []
        
        self._shape = (dim_x, dim_y)

    
    # def __str__(self):
    #     unicode_subins = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084',
    #                       '\u2085', '\u2086', '\u2087', '\u2088', '\u2089']
        
    #     return(
    #         '-'.join([
    #         (f'{pos.path}'
    #          f'{"".join([unicode_subins[int(dig)] for dig in str(ord)])}')
    #         for ord, pos in enumerate(self.positions.values(), 1)])
    #     )
        
    def _trace_path(self):
        if len(self._paths) == 0:
            pos_x = 0
            pos_y = rdm.randint(0, self._shape[1] - 1)
        else:
            start_path = rdm.randint(0, len(self._paths) -1)
            start_order = rdm.randint(0, len(self._paths[start_path] -1))
            start_pos = self._paths[start_path][start_order]

            pos_x = start_pos[0]
            pos_y = start_pos[1]

        new_path = [(pos_x, pos_y)]

        bounded_path = False

        while not bounded_path:
            test_pos = (
                (pos_x, pos_y - 1) if pos_y > 0 else True, 
                (pos_x + 1, pos_y) if pos_x < len(self._shape[0] - 1) else True, 
                (pos_x, pos_y + 1) if pos_y < len(self._shape[1] - 1) else True, 
                (pos_x - 1, pos_y) if pos_x > 0 else True
            )

            free_pos = [pos for pos in test_pos if not self._board.get(pos)]

            if not free_pos:
                bounded_path = True
            
            else:

                next_pos = rdm.choice(free_pos)

                new_path.append(next_pos)

        return new_path if len(new_path) > 1 else False
    
    def _generate_next_path(self):
        existing_paths = len(self._path_initial_positions)

        if existing_paths == 0:
            pos_x = 0
            pos_y = rdm.randint(0, self._shape[1] - 1)
        else:
            start_path = rdm.randint(0, existing_paths - 1)
            start_order = rdm.randint(0, len(self._paths[start_path] -1))
            start_pos = self._paths[start_path][start_order]

            pos_x = start_pos[0]
            pos_y = start_pos[1]




m = Maze(6, 8)



#print(get_size(m))
#print(m.__dict__)