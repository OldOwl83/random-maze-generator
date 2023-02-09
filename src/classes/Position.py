
class Position:
    def __init__(
            self, 
            coordinates: tuple[int, int], 
            path: int, 
            initial: bool,
            next_coordinates: tuple[int, int] | None=None
    ) -> None:
        if (
                (not isinstance(coordinates, tuple) or len(coordinates) != 2 or
                not isinstance(coordinates[0], int) or coordinates[0] < 0 or
                not isinstance(coordinates[1], int) or coordinates[1] < 0) and
                coordinates is not None
            ):
            raise TypeError(
                'El argumento pasado como "coordinates" debe ser una tupla '
                'de dos enteros positivos.'
            )

        if not isinstance(path, int) or path < 0:
            raise TypeError(
                'El argumento pasado como "path" debe ser un entero positivo.'
            )

        if not isinstance(initial, bool):
            raise TypeError(
                'El argumento pasado como "initial" debe ser un booleano.'
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

        self._coordinates = coordinates
        self._path = path
        self._initial = initial
        self._next_coordinates = next_coordinates

    def __str__(self):
        i_unicode = '\u1D62'

        return f'{self._path}{i_unicode if self._initial else ""}'
