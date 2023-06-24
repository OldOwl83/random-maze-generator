
from classes.game import MazeGame
from classes.coordinates import Dimensions

MazeGame(
    screen_resolution=Dimensions(1000, 760),
    maze_dimensions=Dimensions(32, 26)
).start_game()

