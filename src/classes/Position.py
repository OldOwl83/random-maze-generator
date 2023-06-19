
class Position(tuple):
    def __new__(cls, x: int, y: int):
        return tuple.__new__(cls, (x, y))

    def __init__(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError(
                'The Position must be integers.'
            )
        
        # if x < 0 or y < 0:
        #     raise ValueError(
        #         'The Position must be positive integers.'
        #     )
        
        self._x = x
        self._y = y

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
    def up(self):
        return Position(self.x, self.y - 1)
    
    @up.setter
    def up(_, __):
        raise TypeError('The Position properties are immutables.')
    
    @up.deleter
    def up(_):
        raise TypeError('The Position properties cannot be erased.')
    

    @property
    def down(self):
        return Position(self.x, self.y + 1)
    
    @down.setter
    def down(_, __):
        raise TypeError('The Position properties are immutables.')
    
    @down.deleter
    def down(_):
        raise TypeError('The Position properties cannot be erased.')
    
   
    @property
    def left(self):
        return Position(self.x - 1, self.y)
    
    @left.setter
    def left(_, __):
        raise TypeError('The Position properties are immutables.')
    
    @left.deleter
    def left(_):
        raise TypeError('The Position properties cannot be erased.')
    

    @property
    def right(self):
        return Position(self.x + 1, self.y)
    
    @right.setter
    def right(_, __):
        raise TypeError('The Position properties are immutables.')
    
    @right.deleter
    def right(_):
        raise TypeError('The Position properties cannot be erased.')