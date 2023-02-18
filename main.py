from utils.constants import WIDTH, HEIGHT
from utils.classes import Maze
from utils.functions import *


maze = Maze(WIDTH,HEIGHT)
maze.generate_maze()

print_maze(assing_walls(maze))