import random as rdm


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
        
    
    def __init__(self, dim_x: int, dim_y: int) -> None:
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
        self._validate_positive_integer(dim_x, 'dim_x')
        self._validate_positive_integer(dim_y, 'dim_y')

        self._board = {(x, y): {}
                        for y in range(dim_y) for x in range(dim_x)}
        
        self._paths = []
        
        self._shape = (dim_x, dim_y)

    
    def __str__(self):
        unicode_subins = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084',
                          '\u2085', '\u2086', '\u2087', '\u2088', '\u2089']
        
        maze_string = '|\t\t'

        for pos, paths in self._board.items():
            maze_string += '-'.join([
                (f'{path}'
                f'{"".join([unicode_subins[int(dig)] for dig in str(order)])}')
                for path, order in paths.items()])
            
            maze_string += '|\n|\t\t' if pos[0] == self._shape[0] - 1 else '|\t\t'

        return maze_string
        
    def _trace_path(
            self, pos_x: int, pos_y: int, path: int) -> list[tuple[int, int]]:
        '''
        Dadas las coordenadas de una posición inicial y el número de "path" que 
        se quiere generar, contruye una secuencia aleatoria de posiciones 
        adyacentes con las que quedan sin ocupar, finalizando en alguna cuyas 
        adyacentes estén todas ocupadas (situación de "encierro").
        Devuelve la secuencia generada (el "path") y escribe en self._board
        la información correspondiente a cada posición ocupada.
        '''
        self._validate_positive_integer(pos_x, 'pos_x')
        self._validate_positive_integer(pos_y, 'pos_y')
        self._validate_positive_integer(path, 'path')

        new_path = []

        bounded_path = False

        while not bounded_path:
            new_path.append((pos_x, pos_y))
            self._board[(pos_x, pos_y)].update({path: len(new_path)})
            
            test_pos = (
                (pos_x, pos_y - 1) if pos_y > 0 else False, 
                (pos_x + 1, pos_y) if pos_x < self._shape[0] - 1 else False, 
                (pos_x, pos_y + 1) if pos_y < self._shape[1] - 1 else False, 
                (pos_x - 1, pos_y) if pos_x > 0 else False
            )

            free_pos = [pos for pos in test_pos 
                        if pos and not self._board.get(pos)]

            if free_pos:
                pos_x, pos_y = rdm.choice(free_pos)

            else:
                bounded_path = True

                if len(new_path) <=1:
                    self._board[(pos_x, pos_y)].pop(path)
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
            while not new_path or new_path[-1][0] != self._shape[0] - 1:
                for pos in new_path:
                    self._board[pos].clear()

                pos_x = 0
                pos_y = rdm.randint(0, self._shape[1] - 1)

                new_path = self._trace_path(pos_x, pos_y, existing_paths)
                
        else:
            while not new_path:
                start_path = rdm.randint(0, existing_paths - 1)
                start_order = rdm.randint(0, len(self._paths[start_path]) - 1)
                start_pos = self._paths[start_path][start_order]

                pos_x, pos_y = start_pos

                new_path = self._trace_path(pos_x, pos_y, existing_paths)

        self._paths.append(new_path)


    def _fill_board(self):
        '''
        Llama a self._generate_next_path las veces necesarias para ocupar
        la totalidad del tablero representado por self._board
        '''
        while (
            len(null_paths := [pos for pos, paths in self._board.items() 
                                if not paths]) 
                > 0 #> 0.1 * self._shape[0] * self._shape[1]
        ):
            self._generate_next_path()

if __name__ == '__main__':
    l1 = Maze(10, 10)

    l1._fill_board()

    print(l1)