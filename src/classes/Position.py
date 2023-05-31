
class Position(tuple):
    def __new__(cls, x: int, y: int):
        return tuple.__new__(cls, (x, y))

    def __init__(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError(
                'The Position must be integers.'
            )
        
        if x < 0 or y < 0:
            raise ValueError(
                'The Position must be positive integers.'
            )
        
        self._x = x
        self._y = y
        self._path_nexts: dict[int, Position] = {}

        tuple.__init__((x, y))


    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(_, __):
        raise TypeError('The Position properties are immutables.')
    
    @x.deleter
    def x(_):
        raise TypeError('The Position properties cannot be erased.')
    

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(_, __):
        raise TypeError('The Position properties are immutables.')
    
    @y.deleter
    def y(_):
        raise TypeError('The Position properties cannot be erased.')
    
    @property
    def paths(self):
        return tuple(self._path_nexts.keys())
    
    @paths.setter
    def paths(_, __):
        raise TypeError('The Position properties are immutables.')
    
    @paths.deleter
    def paths(_):
        raise TypeError('The Position properties cannot be erased.')

    def __bool__(self):
        return bool(self._path_nexts)

    def add_path_step(self, path: int, next: 'Position'=None):
        if not isinstance(path, int):
            raise TypeError(
                'The "path" parameter type must be integer.'
            )
        
        if path < 0:
            raise ValueError(
                'The "path" parameter must be a positive integer.'
            )
        
        if not isinstance(next, Position):
            raise TypeError(
                'The "position" parameter must be a Position object.'
            )
        
        # TODO
        if False:
            raise ValueError(
                'Only one path step can be no-initial at the same Position.'
            )
        
        self._path_nexts.update({path: next})

    def rm_path(self, path: int):
        return self._path_nexts.pop(path)

    def clear_paths(self):
        self._path_nexts.clear()
        
    def get_path_nexts(self, path: int):
        return self._path_nexts[path]
