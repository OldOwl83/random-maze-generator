class Position:
    def __init__(self) -> None:
        self._paths = []


    # Control del atributo paths
    def get_paths(self):
        return self._paths
    
    def set_paths(self, value):
        raise PermissionError(
            'No se puede alterar este atributo directamente. Utilice los '
            'métodos "add_path" y "rm_path" en su lugar.'
        )

    def del_paths(self):
        self._paths = []
    
    paths = property(get_paths, set_paths, del_paths)


    def __bool__(self):
        return bool(self.paths)
    

    def __str__(self):
        unicode_subins = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084',
                          '\u2085', '\u2086', '\u2087', '\u2088', '\u2089']
        
        return(
            '-'.join([
            (f'{p["path"]}'
             f'{"".join([unicode_subins[int(d)] for d in str(p["order"])])}')
            for p in self.paths])
        )
            

    def add_path(self, path: int, order: int) -> None:
        if (
            not isinstance(path, int) or not isinstance(order, int) or 
            path < 0 or order < 0
        ):
            raise TypeError(
                'Los parámetros "path" y "order" deben ser números naturales o 0.'
            )
        
        for p in self.paths:
            if path == p['path']:
                raise ValueError(
                    'Esta "Position" ya tiene asignado un "order" '
                    'para ese "path".'
                )
            
            if order != 0 and p['order'] != 0:
                raise ValueError(
                    'Una "Position" sólo puede tener un "order" distinto de 0.'
                )

        self.paths.append(
            {
                'path': path,
                'order': order
            }
        )
    
    def rm_path(self, path):
        rm_flag = False

        for p in self.paths:
            if p['path'] == path:
                self.paths.remove(p)
                rm_flag = True

        if not rm_flag:
            raise ValueError(
                f'Esta "Position" no está vinculada con el "path" {path}.'
            )

if __name__ == '__main__':
    p1 = Position()
    
    p1.add_path(1, 23)
    p1.add_path(3, 0)
    
    print((p1.paths))