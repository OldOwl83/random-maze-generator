def dim(V):
    a = 0
    if len(V) > 0:
        for v in V:
            a = a + len(v)
        return a
    else: return 0

#Obtengo vecinos a un cuadrado dentro del maze que estén visitados
def get_neighbours(square, width, height):
    
    fx = square.x
    fy = square.y
    neighbours = []
    if (fx + 1 < self.width) and (grid[fx+1][fy] in self.visited):
        neighbours.append(grid[fx+1][fy])
    
    if (fx -1 > 0) and (grid[fx-1][fy] in self.visited):
        neighbours.append(grid[fx-1][fy])

    if (fy + 1 < self.height) and (grid[fx][fy+1] in self.visited):
        neighbours.append(grid[fx][fy+1])

    if (fy -1 > 0) and (grid[fx][fy-1] in self.visited):
        neighbours.append(grid[fx][fy+1])