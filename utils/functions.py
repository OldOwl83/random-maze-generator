from utils.constants import *
from PIL import Image
import random

def assing_walls(maze):
    """
    assing each visited square in the maze its correspondent value of walls
    for image processing. The beginning of the maze will always be on the top
    or left sides, the goal will always be on the right or bottom sides. 
    """
    walled_squares = []
    start_gate = random.choice(
            [(i,0) for i in range(0,maze.n)] + [(0,j) for j in range(0,maze.m)])
    end_gate = random.choice(
            [(i, maze.m-1) for i in range(0,maze.n)] + [(maze.n-1, j) for j in range(0,maze.m)])

    for sq in maze.visited:
        wall = 0
        if sq.top_wall: wall = wall + 1    
        if sq.left_wall: wall = wall + 2
        if sq.right_wall: wall = wall + 4
        if sq.bottom_wall: wall = wall + 8

        if (sq.x, sq.y) == start_gate or (sq.x, sq.y) == end_gate:
            wall = wall + 16
        
        walled_squares.append((sq.x, sq.y, wall))

    return walled_squares


def print_maze(walled_squares, sprite_size=30):
    """
    Constructs a full sized image of the maze using individual sprites for each square
    The image size is set to 30 because the sprites are 30x30 pixels. The final image
    size will be sprite_size x num_colums BY sprite_size x num_rows 
    """
    walls_images = [Image.open(WALL_PATH + f'{i}.png') for i in range(32)]

    num_columns = max(walled_squares)[0] + 1
    num_rows = max(walled_squares)[1] + 1

    canvas = Image.new('RGB', (sprite_size * num_columns, sprite_size * num_rows))

    # Paste the smaller images onto the larger canvas to create the maze
    for square in walled_squares:
        x = (square[0] % num_columns) * sprite_size
        y = (square[1] % num_rows) * sprite_size
        canvas.paste(walls_images[square[2]], (x, y))
        
    # Save the resulting image
    canvas.save(SAVE_PATH + f'maze{num_columns}x{num_rows}.png')
