from utils.constants import *
from PIL import Image

def assing_walls(maze):
    """
    assing each visited square in the maze its correspondent value of walls
    """
    walled_squares = []

    for sq in maze.visited:
        wall = 0
        if sq.top_wall: wall = wall + 1    
        if sq.left_wall: wall = wall + 2
        if sq.right_wall: wall = wall + 4
        if sq.bottom_wall: wall = wall + 8
        walled_squares.append((sq.x, sq.y, wall))

    walled_squares.sort()

    return walled_squares


def print_maze(walled_squares):
    walls_images = [Image.open(WALL_PATH + f'{i}.png') for i in range(16)]

    #dimensions of the final image
    num_columns = max(walled_squares)[0] + 1
    num_rows = max(walled_squares)[1] + 1
    image_size = 30 #The wall sprites are 30x30

    canvas = Image.new('RGB', (image_size * num_columns, image_size * num_rows))

    # Paste the smaller image onto the larger canvas to create the final image
    for square in walled_squares:
        x = (square[0] % num_columns) * image_size
        y = (square[1] % num_columns) * image_size
        canvas.paste(walls_images[square[2]], (x, y))
        
    # Save the resulting image to your local drive
    canvas.save(SAVE_PATH + f'maze{num_columns}x{num_rows}.png')
    canvas.show()
