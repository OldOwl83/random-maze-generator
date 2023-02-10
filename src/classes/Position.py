
class Position:
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
            coordinates: tuple[int, int], 
            path: int, 
            initial: bool,
            next_coordinates: tuple[int, int] | None=None
    ) -> None:
        self._validate_coordinates(coordinates)
        self._validate_positive_integer(path, 'path')
        self._validate_boolean(initial, 'initial')
        self._validate_coordinates(next_coordinates, 'next_coordinates')
        
        self._coordinates = coordinates
        self._path = path
        self._initial = initial
        self._next_coordinates = next_coordinates

    def __str__(self):
        i_unicode = '\u1D62'

        return f'{self._path}{i_unicode if self._initial else ""}'
