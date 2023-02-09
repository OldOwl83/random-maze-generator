import random
from functions import dim, get_neighbours


#Defino un cuadrado. Un maze esta compuesto por NxM cuadrados
class Square:
    def __init__(self, x, y):
        
        #Inicio las coordenadas 
        self.x = x
        self.y = y

        #El cuadrado inicia no visitado
        self.visited = False
        
        #Defino las paredes del cuadrado
        self.top_wall = True
        self.bottom_wall = True
        self.right_wall = True
        self.left_wall = True

    #Comparo las coordenadas x e y de dos elementos square y elimino la pared que los une
    #Si la coordenada x es mayor, es porque ese objeto se encuentra a la derecha, asi que 
    #hay que borrar su pared izquierda y vice-versa
    def remove_walls(self, other):
        
        if self.x > other.x:
            self.left_wall = False
            other.right_wall = False
        
        if self.x < other.x:
            self.right_wall = False
            other.left_wall = False

        if self.y > other.y:
            self.bottom_wall = False
            other.top_wall = False
        
        if self.y < other.y:
            self.top_wall = False
            other.bottom_wall = False



#Defino la clase Maze de dimensiones NxM
class Maze:
    def __init__(self, width, height):

        #Defino las dimensiones del Maze
        self.width = width
        self.height = height

        #Armo una grilla con elementos square para wxh
        self.grid = [[Square(x, y) for y in range(height)] for x in range(width)]

        self.existing = self.grid
        self.visited = set()
        self.frontier = set()
        """ self.existing_squares = set([self.grid[x][0] for x in range(width)] + 
        [self.grid[x][height-1] for x in range(width)] + 
        [self.grid[0][y] for y in range(height)] + 
        [self.grid[width-1][y] for y in range(height)])

        self.visited_squares = set([self.grid[0][0]])
        self.frontier_squares = set([self.grid[0][0]]) """


    def update_frontier(self, square):
        # obtengo las coodernadas del square
        fx = square.x
        fy = square.y

        #Chequeo las 4 posibilidades de frontera, para eso reviso si está dentro de 
        #las dimensiones del laberinto y si no ha sido visitado. Si es así, lo muevo a frontera
        #y lo saco de existing.
        if (fx + 1 < self.width) and (self.grid[fx+1][fy] not in self.visited):
            self.frontier.append([self.grid[fx+1][fy]])
            self.existing[fx+1].remove(self.grid[fx+1][fy])
        
        if (fx -1 > 0) and (self.grid[fx-1][fy] not in self.visited):
            self.frontier.append([self.grid[fx-1][fy]])
            self.existing[fx-1].remove(self.grid[fx-1][fy])

        if (fy + 1 < self.height) and (self.grid[fx][fy+1] not in self.visited):
            self.frontier.append([self.grid[fx][fy+1]])
            self.existing[fx].remove(self.grid[fx][fy+1])

        if (fy -1 > 0) and (self.grid[fx][fy-1] not in self.visited):
            self.frontier.append([self.grid[fx][fy-1]])
            self.existing[fx].remove(self.grid[fx][fy-1])


    def generate_maze(self):
        
        #Defino un square inicial al azar del interior del laberinto
        n = random.choice(range(1,width))
        m = random.choice(range(1, height))
        square = grid[n][m]
        
        #lo muevo al espacio de visitados
        self.visited.append([square])
        self.existing[n].remove(square)
        
        while dim(self.visited) < self.width * self.height:
            update_frontier(square)
            new_square = random.sample(self.frontier,1)
            sub_visited = get_neighbours(square, width, height)
            visited_square = random.sample(sub_visited, 1)
            new_square.remove_walls(visited_square)

            self.visited.append([new_square])
            self.frontier.remove(new_square)
        #mientras haya 
        """ while len(self.frontier_squares) > 0:
            current = random.sample(self.frontier_squares, 1)[0]
            neighbors = []

            if current.x > 0 and self.grid[current.x-1][current.y] not in self.visited_squares:
                neighbors.append(self.grid[current.x-1][current.y])

            if current.x < self.width-1 and self.grid[current.x+1][current.y] not in self.visited_squares:
                neighbors.append(self.grid[current.x+1][current.y])

            if current.y > 0 and self.grid[current.x][current.y-1] not in self.visited_squares:
                neighbors.append(self.grid[current.x][current.y-1])

            if current.y < self.height-1 and self.grid[current.x][current.y+1] not in self.visited_squares:
                neighbors.append(self.grid[current.x][current.y+1])

            if len(neighbors) > 0:
                neighbor = random.choice(neighbors)
                current.remove_wall(neighbor)
                self.visited_squares.add(neighbor)
                self.frontier_squares.add(neighbor) """