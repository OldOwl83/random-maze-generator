
from classes.game import MazeGame
from classes.coordinates import Dimensions


game = MazeGame(
    maze_dimensions=Dimensions(44, 30)
)

game.start_game()

