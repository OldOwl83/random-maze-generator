from Position import Position


class Location:
    def __init__(
            self, 
            pos_x: int, 
            pos_y: int
    ) -> None:
        if (
            not isinstance(pos_x, int) or pos_x < 0 or
            not isinstance(pos_y, int) or pos_y < 0
        ):
            raise TypeError(
                'Los argumentos pasados como "pos_x" y "pos_y" '
                'deben ser enteros positivos.'
            )
        
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
    ) -> None:
        
        if not isinstance(path, int) or path < 0:
            raise TypeError(
                'El argumento pasado como "path" debe ser un entero positivo.'
            )
        
        if not isinstance(initial, bool):
            raise TypeError(
                'El argumento para "initial" debe ser un valor booleano.'
            )
        
        if (
                (not isinstance(next_coordinates, tuple) or 
                len(next_coordinates) != 2 or
                not isinstance(next_coordinates[0], int) or
                next_coordinates[0] < 0 or
                not isinstance(next_coordinates[1], int) or 
                next_coordinates[1] < 0) and next_coordinates is not None
            ):
            raise TypeError(
                'El argumento pasado como "next_coordinates" debe ser una tupla '
                'de dos enteros positivos.'
            )
        
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
    
    
    def rm_position(self, path: int):
        if not isinstance(path, int) or path < 0:
            raise TypeError(
                'El argumento para "path" debe ser un entero positivo.'
            )
        
        return self.positions.pop(path)
        
    
    def add_next_coordinates_to_path(
            self, 
            path: int, 
            next_coordinates: tuple[int, int]
    ):
        
        if not isinstance(path, int) or path < 0:
            raise TypeError(
                'El argumento para "path" debe ser un número natural o 0.'
            )
        
        if (
                (not isinstance(next_coordinates, tuple) or 
                len(next_coordinates) != 2 or
                not isinstance(next_coordinates[0], int) or
                next_coordinates[0] < 0 or
                not isinstance(next_coordinates[1], int) or 
                next_coordinates[1] < 0) and next_coordinates is not None
            ):
            raise TypeError(
                'El argumento pasado como "next_coordinates" debe ser una tupla '
                'de dos enteros positivos.'
            )
        
        self._positions[path]._next_coordinates = next_coordinates
    

if __name__ == '__main__':
    p1 = Location(1, 1)
    
    p1.add_position(1)
    p1.add_position(3, initial=False)
    
    print((p1))