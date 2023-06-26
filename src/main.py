
from classes.game import MazeGame
from classes.coordinates import Dimensions


game = MazeGame(
    maze_dimensions=Dimensions(28, 20)
)

game.start_game()

