from Maze import Maze
from Coordinates import Coordinates
from Position import Position


class Board(dict):
    def __init__(self, dimensions: tuple[int, int]):
        super().__init__(
            {Coordinates(x, y): Position()
             for y in range(dimensions[1]) 
             for x in range(dimensions[0])}
        )