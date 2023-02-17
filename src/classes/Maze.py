import random as rdm
import pygame as pg

from classes.Position import Position


class Maze:
    @staticmethod
    def _validate_positive_integer(integer, arg_name: str='(s/n)'):
        if not isinstance(integer, int) or integer < 0:
            raise TypeError(
                f'El argumento pasado como "{arg_name}" debe ser un '
                'entero positivo.'
            )
        
    @staticmethod
    def _validate_boolean(boolean, arg_name: str='(s/n)'):
        if not isinstance(boolean, bool):
            raise TypeError(
                f'El argumento pasado como "{arg_name}" debe ser un '
                'valor booleano.'
            )
        
    
    def __init__(
        self, 
        dim: tuple[int, int],
        screen_rect: pg.Rect,
        proportion: float=.8
    ) -> None:
        '''
        self._board: 
            Diccionario que asocia a cada posición del tablero (
            identificada por las coordenadas x e y) otro diccionario cuyas "keys"
            son los "paths" que pasan por ella y los "values" el orden en 
            la secuencia del "path" que corresponde a esa posición (cada posición
            sólo puede tener un orden distinto de 1).
            La utilidad de este atributo consiste en poder evaluar fácilmente
            para cada posición si las adyacentes están ocupadas o no. La 
            información contenida para cada posición, a su vez, sirve para 
            imprimir el tablero (tanto en consola como en el canvas), y para
            evaluar la posibilidad de desplazarse entre una posición y otra.
        self._paths: 
            Lista que almacena cada una de las secuencias (en listas) de 
            posiciones por la que pasa cada "path". Si bien la información
            almacenada en este atributo es indirectamente redundante respecto
            del anterior, facilita el registro de cuántos "paths" fueron 
            trazados a cada momento; y la selección aleatoria de las posiciones
            desde las que deben comenzar cada "path".
        self._shape:
            Contiene las dimensiones del tablero representado por self._board,
            ya que para obtenerlas directamente desde este atributo haría falta 
            iterarlo.
        '''
        self._validate_positive_integer(dim[0], 'dim_x')
        self._validate_positive_integer(dim[1], 'dim_y')

        self._shape = (dim[0], dim[1])

        self._paths = []

        self._rect = pg.Rect(
            (
                screen_rect.width * (1 - proportion) / 2,
                screen_rect.height * (1 - proportion) / 2
            ),
            (
                screen_rect.width * proportion, 
                screen_rect.height * proportion
            )
        )

        self._board = {(x, y): Position((x, y), dim, self._rect)
                        for y in range(dim[1]) for x in range(dim[0])}

        self._fill_board()

        self._marble = {
            'coord': self._paths[0][0],
            'center': self._board[self._paths[0][0]]._rect.center
        }

    
    def __str__(self):
        unicode_subins = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084',
                          '\u2085', '\u2086', '\u2087', '\u2088', '\u2089']
        
        maze_string = '|\t\t'

        for coord, pos in self._board.items():
            maze_string += '-'.join([
                (f'{path}'
                f'{"".join([unicode_subins[int(dig)] for dig in str(order)])}')
                for path, order in pos._paths.items()])
            
            maze_string += '|\n|\t\t' if coord[0] == self._shape[0] - 1 else '|\t\t'

        return maze_string
        
    def _trace_path(
            self,
            init_coord: tuple[int, int],
            path: int
        ) -> list[tuple[int, int]]:
        '''
        Dadas las coordenadas de una posición inicial y el número de "path" que 
        se quiere generar, contruye una secuencia aleatoria de posiciones 
        adyacentes con las que quedan sin ocupar, finalizando en alguna cuyas 
        adyacentes estén todas ocupadas (situación de "encierro").
        Devuelve la secuencia generada (el "path") y escribe en self._board
        la información correspondiente a cada posición ocupada.
        '''
        self._validate_positive_integer(init_coord[0], 'coord_x')
        self._validate_positive_integer(init_coord[1], 'coord_y')
        self._validate_positive_integer(path, 'path')

        new_path = []

        bounded_path = False

        coord_x, coord_y = init_coord

        while not bounded_path:
            new_path.append((coord_x, coord_y))
            self._board[(coord_x, coord_y)].add_path(path, len(new_path))
            
            test_coord = (
                (coord_x, coord_y - 1) if coord_y > 0 else False, 
                (coord_x + 1, coord_y) 
                    if coord_x < self._shape[0] - 1 or path == 0 else False, 
                (coord_x, coord_y + 1) 
                    if coord_y < self._shape[1] - 1 else False, 
                (coord_x - 1, coord_y) if coord_x > 0 else False
            )

            free_coord = [coord for coord in test_coord 
                        if coord and not self._board.get(coord)]

            if free_coord:
                coord_x, coord_y = rdm.choice(free_coord)

            if not free_coord or coord_x == self._shape[0]:
                bounded_path = True

                if len(new_path) <=1:
                    self._board[(coord_x, coord_y)].rm_path(path)
                    new_path = False
               
        return new_path
    

    def _generate_next_path(self):
        '''
        Escoge aleatoriamente la posición desde la que comenzará cada "path"
        (todos comienzan desde alguna posición aleatoria de algún "path" 
        tomado aleatoriamente; salvo el primero, que comienza de alguna 
        posición aleatoria dentro de la columna izquierda del tablero, y debe 
        terminar en alguna posición de la columna derecha); y llama a 
        self._trace_path para generar el "path". Con el "path" recibido
        alimenta el atributo self._paths.
        '''
        new_path = []
        
        if (existing_paths := len(self._paths)) == 0:
            # TODO: Habilitar la posibilidad de que el tramo 1 se cierre 
            # sin encerrarse
            while (
                not new_path or 
                new_path[-1][0] != self._shape[0] - 1 or
                not (len([coord_y for _, coord_y in new_path 
                    if coord_y < self._shape[1] * .2]) > 0 and
                len([coord_y for _, coord_y in new_path 
                    if coord_y > self._shape[1] * .8]) > 0)
            ):
                for coord in new_path:
                    self._board[coord].clear_paths()

                coord_x = 0
                coord_y = rdm.randint(0, self._shape[1] - 1)

                new_path = self._trace_path((coord_x, coord_y), existing_paths)
                
        else:
            while not new_path:
                start_path = rdm.randint(0, existing_paths - 1)
                start_order = rdm.randint(0, len(self._paths[start_path]) - 1)
                start_coord = self._paths[start_path][start_order]

                coord_x, coord_y = start_coord

                new_path = self._trace_path((coord_x, coord_y), existing_paths)

        self._paths.append(new_path)


    def _fill_board(self):
        '''
        Llama a self._generate_next_path las veces necesarias para ocupar
        la totalidad del tablero representado por self._board
        '''
        while (
            len(null_paths := [coord for coord, pos in self._board.items() 
                                if not pos]) 
                > 0 #> 0.1 * self._shape[0] * self._shape[1]
        ):
            self._generate_next_path()

    def move_marble(self, direction: str):
        current_x, current_y = self._marble['coord']

        if direction == 'up':
            new_coord = current_x, current_y - 1 if current_y > 0 else current_y
        elif direction == 'down':
            new_coord = current_x, current_y + 1 \
                if current_y < self._shape[1] - 1 else current_y
        elif direction == 'left':
            new_coord = current_x - 1 if current_x > 0 else current_x, current_y
        elif direction == 'right':
            new_coord = current_x + 1 if current_x < self._shape[0] - 1 \
                else current_x, current_y
        else:
            raise ValueError(
                '"direction" sólo acepta "up", "down", "left" y'
                ' "right" como argumentos.'
            )
        
        if (
            (common_path := list(
                set(self._board[self._marble['coord']]._paths.keys()) 
                & 
                set(self._board[new_coord]._paths.keys())))
            and
            abs(self._board[self._marble['coord']]._paths[common_path[0]] - 
                self._board[new_coord]._paths[common_path[0]]) == 1
        ):
            self._marble['coord'] = new_coord
            self._marble['center'] = self._board[
                self._marble['coord']]._rect.center

        return self._marble['center']
