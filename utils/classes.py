import random

#Square Class. A maze is formed by nxm Squares
class Square:
    def __init__(self, x, y):
        
        #Coordinates of the square  
        self.x = x
        self.y = y
       
        #Initial walls of the Square
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
            self.top_wall = False
            other.bottom_wall = False
        
        if self.y < other.y:
            self.bottom_wall = False
            other.top_wall = False

#Defino la clase Maze de dimensiones NxM
class Maze:
    def __init__(self, n, m):

        #Defino las dimensiones del Maze
        self.n = n
        self.m = m

        #Armo una grilla con elementos square para wxh
        self.grid = [[Square(x, y) for y in range(m)] for x in range(n)]
              
        #Inicio visited y frontier como sets vacios
        self.visited = []
        self.frontier = []

        
    def update_frontier(self, square):
        # obtengo las coodernadas del square
        fx = square.x
        fy = square.y

        #Chequeo las 4 posibilidades de frontera, para eso reviso si está dentro de 
        #las dimensiones del laberinto, si no ha sido visitado y si no está ya dentro de 
        # frontera. Si es así, lo muevo a frontera.
        if (fx + 1 < self.n) and (self.grid[fx+1][fy] not in self.visited) and (
            self.grid[fx+1][fy] not in self.frontier):
            self.frontier.append(self.grid[fx+1][fy])

        if (fx - 1 >= 0) and (self.grid[fx-1][fy] not in self.visited) and (
            self.grid[fx-1][fy] not in self.frontier):
            self.frontier.append(self.grid[fx-1][fy])

        if (fy + 1 < self.m) and (self.grid[fx][fy+1] not in self.visited) and (
            self.grid[fx][fy+1] not in self.frontier):
            self.frontier.append(self.grid[fx][fy+1])

        if (fy - 1 >= 0) and (self.grid[fx][fy-1] not in self.visited) and (
            self.grid[fx][fy-1] not in self.frontier):
            self.frontier.append(self.grid[fx][fy-1])


    #Obtengo vecinos a un cuadrado dentro del maze que estén visitados
    def get_neighbours(self, square):
        
        fx = square.x
        fy = square.y
        neighbours = []
        
        if (fx + 1 < self.n) and (self.grid[fx+1][fy] in self.visited):
            neighbours.append(self.grid[fx+1][fy])

        if (fx -1 >= 0) and (self.grid[fx-1][fy] in self.visited):
            neighbours.append(self.grid[fx-1][fy])

        if (fy + 1 < self.m) and (self.grid[fx][fy+1] in self.visited):
            neighbours.append(self.grid[fx][fy+1])
        
        if (fy -1 >= 0) and (self.grid[fx][fy-1] in self.visited):
            neighbours.append(self.grid[fx][fy-1])

        return neighbours
   

    def generate_maze(self):    
        #Defino un square inicial al azar del interior del laberinto
        _x = random.choice(range(0,self.n))
        _y = random.choice(range(0, self.m))
        
        _square = self.grid[_x][_y]
        self.update_frontier(_square)

        while len(set(self.visited)) <= (self.n * self.m) and len(self.frontier) > 0:

            if _square not in self.visited:
                self.visited.append(_square)
                
            self.update_frontier(_square)
            
            frontier_square = random.choice(self.frontier)

            sub_visited = self.get_neighbours(frontier_square)
                
            visited_square = random.choice(sub_visited)
            
            frontier_square.remove_walls(visited_square)
            
            self.frontier.remove(frontier_square)
            
            _square = frontier_square