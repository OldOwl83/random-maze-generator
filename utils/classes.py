import random


class Square:
    """
    A Square object is defined by its coordinate and the existance of walls.
    """
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
       
        #Initial state of walls for the Square
        self.top_wall = True
        self.bottom_wall = True
        self.right_wall = True
        self.left_wall = True


    def remove_walls(self, other):
        """
        remove_walls compares the relative position of the Squares and determines which 
        walls should be removed to create a path between them.
        """
        
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


class Maze:
    """
    A Maze object of dimension nxm composed by a grid of Squares
    """
    def __init__(self, n, m):

        self.n = n
        self.m = m

        self.grid = [[Square(x, y) for y in range(m)] for x in range(n)]
              
        #Initiate visited and frontier sets 
        self.visited = []
        self.frontier = []

        
    def update_frontier(self, square):
        """
        update_frontier obtains the adjacent squares that are within the maze to any
        given square and updates the frontier set.
        """

        fx = square.x
        fy = square.y

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


    def get_neighbours(self, square):
        """
        get_neighbours returns a set of the adjacent visited squares that are 
        within the maze to any given square. 
        """
        
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
        """
        generate_maze modifies the maze object itself and the 'walls' atributes of 
        each square object within it 
        """
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
        
        self.visited.append(_square)
