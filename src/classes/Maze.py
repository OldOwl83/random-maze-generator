import random as rdm
from typing import Literal

import pygame as pg

from Position import Position
from Board import Board


# Type hints
dimensions = coordinates = tuple[int, int]

direction = Literal['up', 'down', 'left', 'right']


class Maze:
    def __init__(
        self, 
        dim: dimensions,
        # screen_rect: pg.Rect,
        # proportion: float=.8
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
        self._path_initials: 
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
        
        self._shape: dimensions = dim

        self._path_initials: list[coordinates] = []

        # self._rect = pg.Rect(
        #     (
        #         screen_rect.width * (1 - proportion) / 2,
        #         screen_rect.height * (1 - proportion) / 2
        #     ),
        #     (
        #         screen_rect.width * proportion, 
        #         screen_rect.height * proportion
        #     )
        # )

        self._board: Board(self._shape)

        self._fill_board()

        # self._marble = {
        #     'coord': self._path_initials[0][0],
        #     'center': self._board[self._path_initials[0][0]]._rect.center
        # }

    
    def __str__(self):
        unicode_subins = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084',
                          '\u2085', '\u2086', '\u2087', '\u2088', '\u2089']
        
        maze_string = '|\t\t'

        for pos in sorted(self._board._board):
            maze_string += '-'.join([
                f'{path}'
                for path in pos._path_nexts.keys()])
            
            maze_string += '|\n|\t\t' if pos[0] == self._shape[0] - 1 else '|\t\t'

        return maze_string
        
    def _trace_path(
            self,
            init_coord: coordinates,
            path: int
        ):
        '''
        Dadas las coordenadas de una posición inicial y el número de "path" que 
        se quiere generar, contruye una secuencia aleatoria de posiciones 
        adyacentes con las que quedan sin ocupar, finalizando en alguna cuyas 
        adyacentes estén todas ocupadas (situación de "encierro").
        Devuelve la secuencia generada (el "path") y escribe en self._board
        la información correspondiente a cada posición ocupada.
        '''
        bounded_path = False

        coord_x, coord_y = init_coord

        while not bounded_path:
            
            test_coord = (
                (coord_x, coord_y - 1) if coord_y > 0 else False, 
                (coord_x + 1, coord_y) 
                    if coord_x < self._shape[0] - 1 or path == 0 else False, 
                (coord_x, coord_y + 1) 
                    if coord_y < self._shape[1] - 1 else False, 
                (coord_x - 1, coord_y) if coord_x > 0 else False
            )

            free_coord = [coord for coord in test_coord 
                        if coord and not self._board.get_position(coord)]

            if free_coord:
                next_coord = rdm.choice(free_coord)
                self._board.get_position((coord_x, coord_y)).add_path_step(
                    path, self._board.get_position(next_coord)
                )
                coord_x, coord_y = next_coord

            else:
                bounded_path = True
        
        return next_coord
    

    def _generate_next_path(self):
        '''
        Escoge aleatoriamente la posición desde la que comenzará cada "path"
        (todos comienzan desde alguna posición aleatoria de algún "path" 
        tomado aleatoriamente; salvo el primero, que comienza de alguna 
        posición aleatoria dentro de la columna izquierda del tablero, y debe 
        terminar en alguna posición de la columna derecha); y llama a 
        self._trace_path para generar el "path". Con el "path" recibido
        alimenta el atributo self._path_initials.
        '''
        
        while existing_paths := len(self._path_initials) == 0:
            coord_x = 0
            coord_y = rdm.randint(0, self._shape[1] - 1)

            last_coord = self._trace_path((coord_x, coord_y), existing_paths)
            
            if last_coord[0] == self._shape[0] - 1:
                self._path_initials.append(last_coord)
            else:
                self._board.remove_path()
                
        else:
            while not new_path:
                start_path = rdm.randint(0, existing_paths - 1)
                start_order = rdm.randint(0, len(self._path_initials[start_path]) - 1)
                start_coord = self._path_initials[start_path][start_order]

                coord_x, coord_y = start_coord

                new_path = self._trace_path((coord_x, coord_y), existing_paths)

        self._path_initials.append(new_path)


    def _fill_board(self):
        '''
        Llama a self._generate_next_path las veces necesarias para ocupar
        la totalidad del tablero representado por self._board
        '''
        while not self._board.is_empty():
            self._generate_next_path()

    # def move_marble(self, direction: Direction):
    #     current_x, current_y = self._marble['coord']

    #     if direction == 'up':
    #         new_coord = current_x, current_y - 1 if current_y > 0 else current_y
    #     elif direction == 'down':
    #         new_coord = current_x, current_y + 1 \
    #             if current_y < self._shape[1] - 1 else current_y
    #     elif direction == 'left':
    #         new_coord = current_x - 1 if current_x > 0 else current_x, current_y
    #     elif direction == 'right':
    #         new_coord = current_x + 1 if current_x < self._shape[0] - 1 \
    #             else current_x, current_y
    #     else:
    #         raise ValueError(
    #             '"direction" sólo acepta "up", "down", "left" y'
    #             ' "right" como argumentos.'
    #         )
        
    #     if (
    #         (common_path := list(
    #             set(self._board[self._marble['coord']]._path_initials.keys()) 
    #             & 
    #             set(self._board[new_coord]._path_initials.keys())))
    #         and
    #         abs(self._board[self._marble['coord']]._path_initials[common_path[0]] - 
    #             self._board[new_coord]._path_initials[common_path[0]]) == 1
    #     ):
    #         self._marble['coord'] = new_coord
    #         self._marble['center'] = self._board[
    #             self._marble['coord']]._rect.center

    #     return self._marble['center']
