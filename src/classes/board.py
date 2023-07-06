import pygame as pg

from classes.coordinates import Coordinates, Dimensions, Position
from datetime import datetime as dt

class Board():
    '''
    Esta clase representa un tablero cuadriculado de tamaño y dimensiones
    personalizables, compuesto de objectos Position asociados a coordenadas 
    particulares dentro de la grilla definida por el tablero. Adicionalmente,
    presenta las interfaces para obtener información sobre el estado de las 
    posiciones y manipular las relaciones de conexión o desconexión entre 
    posiciones vecinas, dentro del trazado de un laberinto. Finalmente, se
    incluye un método especial para dibujar el tablero en el contexto de una 
    aplicación pygame.
    '''
    def __init__(self, dimensions: Dimensions, size: Dimensions):
        if (
            not isinstance(dimensions, Dimensions) or 
            not isinstance(size, Dimensions)
        ):
            raise TypeError(
                'The Board parameters must be Dimensions object.'
            )
            
        '''
        Esta es la propiedad principal de la clase Board, y asocia cada posición
        del mismo a un objeto Coordinates, para facilitar su referenciamiento.
        '''   
        self._board = {
            Coordinates(x, y): Position(
                x, y,
                pg.Rect(
                    (size.left.x) / dimensions.x * x,
                    (size.up.y) / dimensions.y * y,
                    (size.left.x) / dimensions.x,
                    (size.up.y) / dimensions.y
                )
            )
            for y in range(dimensions.y) 
            for x in range(dimensions.x)
        }
        
        self._open_positions = set() # Se registran las posiciones abiertas a los efectos
                                        # de optimizar la función get_open_positions()
        self._size = size


    '''
    Esta propiedad valida si todas las posiciones del tablero están abiertas a
    algún vecino, lo que indica que están todas integradas al laberinto y, por
    tanto, éste está completamente trazado.
    ''' 
    @property
    def is_full(self):
        return all(self._board.values())
    
    @is_full.setter
    def is_full(_, __):
        raise TypeError('The Board properties are immutables.')
    
    @is_full.deleter
    def is_full(_):
        raise TypeError('The Board properties cannot be erased.')
    

    def __str__(self):
        '''
        Representación del tablero por consola, para facilitar el desarrollo y
        testeo de esta clase.
        '''
        draw_string = ''.join(['--------'] * self.get_dimensions()[0]) + '\n'

        for y in range(self.get_dimensions()[1]):
            for pos in self._board.values():
                if pos.y == y:
                    draw_string += '|' if pos.x == 0 else ''
                    draw_string += ('\t|' 
                                    if not pos.is_neighbor_open(pos.right) 
                                    else '\t ')

            draw_string += '\n'

            for pos in self._board.values():
                if pos.y == y:
                    draw_string += ('--------' 
                                    if not pos.is_neighbor_open(pos.down) 
                                    else '        ')
                
            draw_string += '\n'
                
        return draw_string
    
   
    def get_dimensions(self) -> Dimensions:
        #Devuelve la cantidad de posiciones en los ejes "x" e "y" del tablero
        return max(self._board.keys()).right.down
    
    def get_position(self, position: Coordinates) -> Position:
        # Devuelve el objeto Position asociada a la coordenada "position"
        return self._board[position]
    
    def get_position_rect(self, position: Coordinates) -> pg.Rect:
        # Devuelve el objeto pygame.Rect correspondiente a la posición asociada 
        # a la coordenada "position"
        return self._board[position].rect
    
    def get_all_positions(self) -> tuple[Position]:
        # Devuelve todos los objetos Position que componen al tablero
        return tuple(self._board.values())
    
    def get_open_positions(self) -> tuple[Position]:
        # Devuelve todos los objetos Position que están conectados a algún vecino
        return tuple(self._open_positions)

    def get_open_neighbors(self, position: Coordinates) -> tuple[Coordinates]:
        # Devuelve todos los vecinos que están conectados a "position"
        return self._board[position].get_open_neighbors()
        
    def get_closed_neighbors(self, position: Coordinates) -> tuple[Position]:
        # Devuelve todos los vecinos de "position" que están completamente 
        # desconectados
        return tuple(
            pos for pos in (
                position.up, position.down, position.left, position.right
            ) if not self._board.get(pos, True)
        )
    
    def connect_neighbor(
        self, position: Coordinates, neighbor: Coordinates    
    ) -> None:
        # Conecta los objetos Positions pasados por parámetros, y los agrega al
        # conjunto de "_open_positions" del tablero
        self._board.get(position).add_open_neighbor(neighbor)
        self._board.get(neighbor).add_open_neighbor(position)
        
        self._open_positions |= {position, neighbor}

    def get_shortest_path_positions(
        self, start: Coordinates, finish: Coordinates
    ) -> tuple[Position]:
        # Devuelve la secuencia de posiciones que conectan a "start" con 
        # "finish". La mayor utilidad de este método es trazar la solución del 
        # laberinto.
        test_board = {
            pos: list(pos.get_open_neighbors()) for pos in self._board.values()
        }
        test_steps = []
        previous_forks = []
        
        while start != finish:
            if len(test_board[start]) > 0:
                test_steps.append(start)
                
                if len(test_board[start]) > 1:
                    previous_forks.append(start)
                
                next = test_board[start].pop()
                test_board[next].remove(start)
                start = next
            
            else:                    
                start = previous_forks.pop()
                test_steps = test_steps[:test_steps.index(start)]
        
        test_steps.append(finish)
        
        return tuple(self._board[step] for step in test_steps)                   


    def get_surface(self) -> pg.Surface:
        # Devuelve un objeto Surface con el tablero dibujado
        surface = pg.Surface(self._size)
        surface.fill('beige')
        rect = pg.Rect((0, 0), self._size)
        line_width = int(rect.width * 0.004)

        # Imprime paredes lateral izquerda y superior
        pg.draw.lines(
            surface, 
            'darkred', 
            False, 
            [rect.bottomleft, rect.topleft, rect.topright],
            line_width
        )

        # Imprime paredes internas, lateral derecha e inferior
        for pos in self._board.values():
            if not pos.is_neighbor_open(pos.right):
                pg.draw.line(
                    surface, 
                    'darkred', 
                    pos.rect.topright, 
                    pos.rect.bottomright,
                    line_width
                )
            
            if not pos.is_neighbor_open(pos.down):
                pg.draw.line(
                    surface, 
                    'darkred', 
                    pos.rect.bottomleft, 
                    pos.rect.bottomright,
                    line_width
                )

        return surface
    