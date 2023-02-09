from Position import Position


class Location:
    def __init__(
            self, 
            pos_x: int, 
            pos_y: int
    ) -> None:
        
        self._coordinates = (pos_x, pos_y)
        self._positions = {}

    # Control del atributo coordinates
    def get_coordinates(self):
        return self._coordinates
    
    def set_coordinates(self, value):
        raise PermissionError(
            'Las "coordinates" de una "Location" sólo pueden pasarse '
            'como argumentos a su constructor.'
        )
    
    def del_coordinates(self):
        raise PermissionError(
            'Una "Location" no puede carecer del atributo "coordinates".'
            'Elimine el objeto mismo en su lugar.'
        )
    
    coordinates = property(get_coordinates, set_coordinates, del_coordinates)


    # Control del atributo positions
    def get_positions(self):
        return self._positions
    
    def set_positions(self, value):
        raise PermissionError(
            'No se puede alterar este atributo directamente. Utilice los '
            'métodos "add_path" y "rm_path" en su lugar.'
        )

    def del_positions(self):
        self._positions = []
    
    positions = property(get_positions, set_positions, del_positions)


    def __bool__(self):
        return bool(self.positions)
    
    # TODO: corregir para el nuevo modelo
    def __str__(self):
        unicode_subins = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084',
                          '\u2085', '\u2086', '\u2087', '\u2088', '\u2089']
        
        return(
            '-'.join([
            (f'{pos.path}'
             f'{"".join([unicode_subins[int(dig)] for dig in str(ord)])}')
            for ord, pos in enumerate(self.positions.values(), 1)])
        )
            

    def add_position(
            self,
            path: int,
            initial: bool=True,
            next_coordinates: tuple[int, int]=None
    ) -> None:
        
        if not isinstance(path, int) or path < 0:
            raise TypeError(
                'El argumento para "path" debe ser un número natural o 0.'
            )
        
        if not isinstance(initial, bool):
            raise TypeError(
                'El argumento para "initial" debe ser un valor booleano.'
            )
        
        # TODO: Validar coordenadas
        # if not isinstance(next_coordinates, tuple[int, int]):
        #     raise TypeError(
        #         'El argumento para "next_coordinates" debe ser una tupla con '
        #         'dos enteros.'
        #     )
        
        for pos in self.positions.values():
            if pos.path == path:
                raise ValueError(
                    'Esta "Location" ya tiene asignada una "Position" '
                    'para ese "path".'
                )
            
            if not initial and not pos.initial:
                raise ValueError(
                    'Una "Location" sólo puede tener una "Position" no inicial.'
                )

        new_position = Position(self.coordinates, path, initial, next_coordinates)

        self.positions.update({path: new_position})

        return new_position
    
    
    def rm_position(self, path: int):
        if not isinstance(path, int) or path < 0:
            raise TypeError(
                'El argumento para "path" debe ser un número natural o 0.'
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
        
        # TODO: Validar coordenadas
        # if not isinstance(next_coordinates, tuple[int, int]):
        #     raise TypeError(
        #         'El argumento para "next_coordinates" debe ser una tupla con '
        #         'dos enteros.'
        #     )
        
        self.positions[path].next_coordinates = next_coordinates
    

if __name__ == '__main__':
    p1 = Location(1, 1)
    
    p1.add_position(1)
    p1.add_position(3)
    
    print((p1))