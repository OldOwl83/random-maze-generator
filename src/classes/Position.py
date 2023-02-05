class Position:
    def __init__(self) -> None:
        self._paths = []

    def get_paths(self):
        return self._paths
    
    def set_paths(self, *args):
        raise PermissionError(
            'No se puede alterar este atributo directamente. Utilice los '
            'métodos "add_path" y "rm_path" en su lugar.'
        )
    
    paths = property(get_paths, set_paths)

    def add_path(self, path: int, order: int) -> None:
        if (
            not isinstance(path, int) or not isinstance(order, int) or 
            path <= 0 or order <= 0
        ):
            raise TypeError(
                'Los parámetros "path" y "order" deben ser números naturales.'
            )
        
        for p in self._paths:
            if path == p['path']:
                raise ValueError(
                    'Esta "Position" ya tiene asignado un "order" '
                    'para ese "path".'
                )
            
            if order != 1 and p['order'] != 1:
                raise ValueError(
                    'Una "Position" sólo puede tener un "order" distinto de 1.'
                )

        self._paths.append(
            {
                'path': path,
                'order': order
            }
        )
    
    def rm_path(self, path):
        rm_flag = False

        for p in self._paths:
            if p['path'] == path:
                self._paths.remove(p)
                rm_flag = True

        if not rm_flag:
            raise ValueError(
                f'Esta "Position" no está vinculada con el "path" {path}.'
            )

if __name__ == '__main__':
    p1 = Position()
    p1.add_path(1, 23)
    p1.add_path(3, 1)
    p1.rm_path(4)
    print(p1.paths)
