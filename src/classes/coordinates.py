import pygame as pg

class Coordinates(tuple):
    '''
    Esta clase define un tipo especial de tupla compuesta de dos enteros, 
    cuyas instancias representan coordenadas particulares e inmutables de un 
    plano bidimensional. Sus posiciones en los ejes cartesianos son accesibles 
    como propiedades del objeto ("x" e "y"), tanto como a través de los índices
    de la tupla (0 y 1). Adicionalmente, Coordinates define propiedades que 
    devuelven las coordenadas vecinas dentro del plano ("up", "down", "left" 
    y "right").
    @params:
        x: posición de la coordenada en el eje x.
        y: posición de la coordenada en el eje y.
    '''
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
    '''
    Esta clase extiende la clase Coordinates para representar las dimensiones 
    de un plano bidimensional. Dimensions no admite que sus propiedades "x" e 
    "y" contengan valores negativos. Adicionalmente, admite las operaciones 
    aritméticas básicas (+, -, *, /) contra un escalar u otro objeto 
    Coordinates, siempre y cuando el resultado no contradiga las restricciones
    de un objeto Dimensions (los resultados con decimales son redondeados).
    @params:
        x: anchura del plano.
        y: altura del plano.
    '''
    def __init__(self, x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError(
                'The elements of a Dimensions object must be positive integer.'
            )
        
        super().__init__(x, y)
        
    
    def __add__(self, other: float|Coordinates):
        if isinstance(other, Coordinates):
            return Dimensions(
                round(self.x + other.x), round(self.y + other.y)
            )
    
        elif isinstance(other, float) or isinstance(other, int):
            return Dimensions(
                round(self.x + other), round(self.y + other)
            )
        
        else:
            raise TypeError(
                'The other must be a number or a Coordinates object.'
            )
        
    
    def __sub__(self, other: float|Coordinates):
        if isinstance(other, Coordinates):
            return Dimensions(
                round(self.x - other.x), round(self.y - other.y)
            )
    
        elif isinstance(other, float) or isinstance(other, int):
            return Dimensions(
                round(self.x - other), round(self.y - other)
            )
        
        else:
            raise TypeError(
                'The other must be a number or a Coordinates object.'
            )
        
    def __mul__(self, multiplier: float|Coordinates|tuple[float, float]):
        if isinstance(multiplier, Coordinates) or isinstance(multiplier, tuple):
            return Dimensions(
                round(self.x * multiplier[0]), round(self.y * multiplier[1])
            )
    
        elif isinstance(multiplier, float) or isinstance(multiplier, int):
            return Dimensions(
                round(self.x * multiplier), round(self.y * multiplier)
            )
        
        else:
            raise TypeError(
                'The multiplier must be a number or a Coordinates object.'
            )
        
    def __truediv__(self, divider: float|Coordinates):
        if isinstance(divider, Coordinates):
            return Dimensions(
                round(self.x / divider.x), round(self.y / divider.y)
            )
    
        elif isinstance(divider, float) or isinstance(divider, int):
            return Dimensions(
                round(self.x / divider), round(self.y / divider)
            )
        
        else:
            raise TypeError(
                'The divider must be a number or a Coordinates object.'
            )


class Position(Coordinates):
    '''
    Esta clase extiende a la clase Coordinates para asociar a una coordenada 
    particular e inmutable de un plano bidimensional un objeto Rect del módulo
    pygame y una lista de coordenadas vecinas con las que se considera 
    conectada. El objeto Rect es accesible como una propiedad. Adicionalmente, 
    se define una serie de métodos que permiten manipular públicamente la lista
    de vecinos conectados. La llamada "bool(any_position_object)" devolverá 
    "False" sólo cuando "any_position_object" no tenga ningún vecino asociado.
    @params:
        x: posición de la coordenada en el eje x.
        y: posición de la coordenada en el eje y.
        rect: objecto pygame.Rect que representa la ubicación y la dimensión
            gráficas de la coordenada. Es opcional.
    '''
    def __new__(cls, x: int, y: int, rect: pg.Rect=None):
        return super().__new__(cls, x, y)

    def __init__(self, x: int, y: int, rect: pg.Rect=None):
        super().__init__(x, y)

        self._rect = rect
        self._open_neighbors = []


    @property
    def rect(self):
        return self._rect
    
    @rect.setter
    def rect(_, __):
        raise AttributeError('The Position properties are immutables.')
    
    @rect.deleter
    def rect(_):
        raise AttributeError('The Position properties cannot be erased.')


    def __bool__(self):
        return bool(self._open_neighbors)
    

    def get_open_neighbors(self):
        return tuple(self._open_neighbors)
    
    def add_open_neighbor(self, neighbor: Coordinates):
        if (
            self.up == neighbor or self.down == neighbor or 
            self.left == neighbor or self.right == neighbor
        ):
            self._open_neighbors.append(neighbor)
        else:
            raise ValueError(
                f'Coordinates {neighbor} is not neighbor of {self}.'
            )

    def remove_open_neighbor(self, neighbor: Coordinates):
        self._open_neighbors.remove(neighbor)

    def is_neighbor_open(self, neighbor: Coordinates):
        if (
            self.up == neighbor or self.down == neighbor or 
            self.left == neighbor or self.right == neighbor
        ):
            return neighbor in self._open_neighbors
        else:
            raise ValueError(
                f'Coordinates {neighbor} is not neighbor of {self}.'
            )

