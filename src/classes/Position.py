class Position:
    def __init__(self) -> None:
        self._paths = []

    @property
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, *args):
        raise PermissionError('No se puede alterar este atributo ' + 
            'directamente. Utilice los métodos "add_path" y "rm_path" ' + 
            'en su lugar.')

    def add_path(self, path: int, order: int) -> None:
        if not isinstance(path, int) or not isinstance(order, int):
            raise TypeError('Los parámetros "path" y "order" deben ser ' + 
                'números enteros')

        self._paths.append(
            {
                'path': path,
                'order': order
            }
        )
