import pygame as pg

class Position:
    def __init__(
        self, 
        pos_coord: tuple[int, int], 
        maze_dim: tuple[int, int],
        maze_rect: pg.Rect
    ):
        self._paths = {}
        self._rect = pg.Rect(
            (
                pos_coord[0] * maze_rect.width / maze_dim[0] + maze_rect.left, 
                pos_coord[1] * maze_rect.height / maze_dim[1] + maze_rect.top
            ),
            (maze_rect.width / maze_dim[0], maze_rect.height / maze_dim[1])
        )

    def __bool__(self):
        return bool(self._paths)

    def add_path(self, path, order):
        self._paths.update({path: order})

    def rm_path(self, path):
        return self._paths.pop(path)

    def clear_paths(self):
        self._paths.clear()
