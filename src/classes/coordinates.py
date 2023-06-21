import pygame as pg

class Coordinates(tuple):
    def __new__(cls, x: int, y: int):
        return tuple.__new__(cls, (x, y))

    def __init__(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError(
                'The elements of a Coordinates object must be integer.'
            )
        
        self._x = x
        self._y = y

        tuple.__init__((x, y))


    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(_, __):
        raise AttributeError('The Coordinates properties are immutables.')
    
    @x.deleter
    def x(_):
        raise AttributeError('The Coordinates properties cannot be erased.')
    

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(_, __):
        raise AttributeError('The Coordinates properties are immutables.')
    
    @y.deleter
    def y(_):
        raise AttributeError('The Coordinates properties cannot be erased.')
    
    
    @property
    def up(self):
        return Coordinates(self.x, self.y - 1)
    
    @up.setter
    def up(_, __):
        raise AttributeError('The Coordinates properties are immutables.')
    
    @up.deleter
    def up(_):
        raise AttributeError('The Coordinates properties cannot be erased.')
    

    @property
    def down(self):
        return Coordinates(self.x, self.y + 1)
    
    @down.setter
    def down(_, __):
        raise AttributeError('The Coordinates properties are immutables.')
    
    @down.deleter
    def down(_):
        raise AttributeError('The Coordinates properties cannot be erased.')
    
   
    @property
    def left(self):
        return Coordinates(self.x - 1, self.y)
    
    @left.setter
    def left(_, __):
        raise AttributeError('The Coordinates properties are immutables.')
    
    @left.deleter
    def left(_):
        raise AttributeError('The Coordinates properties cannot be erased.')
    

    @property
    def right(self):
        return Coordinates(self.x + 1, self.y)
    
    @right.setter
    def right(_, __):
        raise AttributeError('The Coordinates properties are immutables.')
    
    @right.deleter
    def right(_):
        raise AttributeError('The Coordinates properties cannot be erased.')


class Dimensions(Coordinates):
    def __init__(self, x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError(
                'The elements of a Dimensions object must be positive integer.'
            )
        
        super().__init__(x, y)
        
    
    def __add__(self, other: 'Dimensions'):
        return Dimensions(self.x + other[0], self.y + other[1])
    
    def __sub__(self, other: 'Dimensions'):
        return Dimensions(self.x - other[0], self.y - other[1])
        
    def __mul__(self, multiplier: float):
        return Dimensions(round(self.x * multiplier), round(self.y * multiplier))


class Position(Coordinates):
    def __new__(cls, x: int, y: int, rect: pg.Rect=None):
        return super().__new__(cls, x, y)

    def __init__(self, x: int, y: int, rect: pg.Rect=None):
        super().__init__(x, y)

        self._rect = rect
        
    @property
    def rect(self):
        return self._rect
    
    @rect.setter
    def rect(_, __):
        raise AttributeError('The Position properties are immutables.')
    
    @rect.deleter
    def rect(_):
        raise AttributeError('The Position properties cannot be erased.')

