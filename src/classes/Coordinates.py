from Board import Board


class Coordinates(tuple):
    def __new__(cls, x: int, y: int, max_dim: tuple[int, int]=None):
        return tuple.__new__(cls, (x, y))

    def __init__(self, x: int, y: int, max_dimen: tuple[int, int]=None):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError(
                'The coordinates must be integers.'
            )
        
        if max_dimen is not None and (
            not (isinstance(max_dimen, tuple) or isinstance(max_dimen, tuple)) 
            or (len(max_dimen) != 2 or not isinstance(max_dimen[0], int) 
                or not isinstance(max_dimen[1], int)
        )):
            raise TypeError(
                'The maximum dimensions must be a tuple of two integers.'
            )
        
        if x < 0 or y < 0 or (
            max_dimen and (x >= max_dimen[0] or y >= max_dimen[1])):
            raise ValueError(
                'The coordinates must be positive integers and not surpass '
                'his maximum dimensions.'
            )
        
        self._x = x
        self._y = y
        self._max_dim = max_dimen

        tuple.__init__((x, y))


    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(_, __):
        raise TypeError('The Coordinates properties are immutables.')
    
    @x.deleter
    def x(_):
        raise TypeError('The Coordinates properties cannot be erased.')
    

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(_, __):
        raise TypeError('The Coordinates properties are immutables.')
    
    @y.deleter
    def y(_):
        raise TypeError('The Coordinates properties cannot be erased.')
    

    @property
    def max_dim(self):
        return self._max_dim
    
    @max_dim.setter
    def max_dim(_, __):
        raise TypeError('The Coordinates properties are immutables.')
    
    @max_dim.deleter
    def max_dim(_):
        raise TypeError('The Coordinates properties cannot be erased.')
    

    def up(self, displacement: int):
        return Coordinates(self.x, self.y + displacement, self._max_dim)
    
    def down(self, displacement: int):
        return Coordinates(self.x, self.y - displacement, self._max_dim)
    
    def left(self, displacement: int):
        return Coordinates(self.x - displacement, self.y, self._max_dim)
    
    def right(self, displacement: int):
        return Coordinates(self.x + displacement, self.y, self._max_dim)