
from classes.game import MazeGame
from classes.coordinates import Dimensions


game = MazeGame(
    maze_dimensions=Dimensions(50, 36)
)

game.start_game()

