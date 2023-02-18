def assing_walls(maze):

    squares = []

    for sq in maze.visited:
        wall = 0
        if sq.top_wall: wall = wall + 1    
        if sq.left_wall: wall = wall + 2
        if sq.right_wall: wall = wall + 4
        if sq.bottom_wall: wall = wall + 8
        squares.append((sq.x, sq.y, wall))

    squares.sort()

    return squares
