from Coordinates import Coordinates

class Position:
    def __init__(self):
        self._paths: dict[int, int] = {}
        
    def __bool__(self):
        return bool(self._paths)

    def add_path(self, path: int, order: int):
        if (
            not isinstance(path, int) or not isinstance(order, int) or 
            path < 0 or order < 0
        ):
            raise ValueError(
                'The "path" and "order" arguments must be positive integers.'
            )
        
        if (
            path not in self._paths.keys() and 
            order != 1 and 
            any(map(lambda val: val != 1, self._paths.values()))
        ):
            raise ValueError(
                'Only one path step can be other than 1 at the same Position.'
            )
        else:
            self._paths.update({path: order})

    def rm_path(self, path: int):
        return self._paths.pop(path)

    def clear_paths(self):
        self._paths.clear()
