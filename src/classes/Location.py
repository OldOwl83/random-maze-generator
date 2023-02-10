from Position import Position


class Location:
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

    def __init__(
            self, 
            pos_x: int, 
            pos_y: int
    ) -> None:
        self._validate_positive_integer(pos_x, 'pos_x')
        self._validate_positive_integer(pos_y, 'pos_y')

        self._coordinates = (pos_x, pos_y)
        self._positions = {}


    def __bool__(self):
        return bool(self._positions)
    
    
    def __str__(self):
        return(
            '-'.join([str(pos) for pos in self._positions.values()])
        )
            

    def add_position(
            self,
            path: int,
            initial: bool=True,
            next_coordinates: tuple[int, int]=None
    ) -> Position:
        
        self._validate_positive_integer(path, 'path')
        self._validate_boolean(initial, 'initial')
        self._validate_coordinates(next_coordinates, 'next_coordinates')
        
        for pos in self._positions.values():
            if pos._path == path:
                raise ValueError(
                    'Esta "Location" ya tiene asignada una "Position" '
                    'para ese "path".'
                )
            
            if not initial and not pos._initial:
                raise ValueError(
                    'Una "Location" sólo puede tener una "Position" no inicial.'
                )

        new_position = Position(
            self._coordinates, path, initial, next_coordinates)

        self._positions.update({path: new_position})

        return new_position
    
    
    def rm_position(self, path: int) -> Position:
        self._validate_positive_integer(path, 'path')
        
        return self._positions.pop(path)
        
    
    def add_next_coordinates_to_path(
            self, 
            path: int, 
            next_coordinates: tuple[int, int]
    ) -> None:
        self._validate_positive_integer(path, 'path')
        self._validate_coordinates(next_coordinates, 'next_coordinates')
        
        self._positions[path]._next_coordinates = next_coordinates
    

if __name__ == '__main__':
    p1 = Location(1, 1)
    
    p1.add_position(1)
    p1.add_position(3, initial=False)
    p1.add_position(4)
    p1.add_next_coordinates_to_path(4, (3, 5))
    print((p1))
    print(p1._positions[4]._next_coordinates)
    p1.rm_position(4)
    print(p1)