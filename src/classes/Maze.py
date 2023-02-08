from Position import Position
import random as rdm


class Maze:
    def __init__(self, dim_x, dim_y) -> None:
        self._board = {(x, y): Position() 
                        for x in range(dim_x) for y in range(dim_y)}
        
        self._paths = []
        self._shape = (dim_x, dim_y)
        
    def trace_path(self):
        if len(self._paths) == 0:
            pos_x = 0
            pos_y = rdm.randint(0, self._shape[1] - 1)
        else:
            start_path = rdm.randint(0, len(self._paths) -1)
            start_order = rdm.randint(0, len(self._paths[start_path] -1))
            start_pos = self._paths[start_path][start_order]

            pos_x = start_pos[0]
            pos_y = start_pos[1]

        new_path = [(pos_x, pos_y)]

        bounded_path = False

        while not bounded_path:
            test_pos = (
                (pos_x, pos_y - 1) if pos_y > 0 else True, 
                (pos_x + 1, pos_y) if pos_x < len(self._shape[0] - 1) else True, 
                (pos_x, pos_y + 1) if pos_y < len(self._shape[1] - 1) else True, 
                (pos_x - 1, pos_y) if pos_x > 0 else True
            )

            free_pos = [pos for pos in test_pos if not self._board.get(pos)]

            if not free_pos:
                bounded_path = True
            
            else:

                next_pos = rdm.choice(free_pos)

                new_path.append(next_pos)

        return new_path if len(new_path) > 1 else False




m = Maze(6, 8)



#print(get_size(m))
#print(m.__dict__)