
class Position:
    def __init__(
            self, 
            coordinates: tuple[int, int], 
            path: int, 
            initial: bool,
            next_coordinates: tuple[int, int] | None=None
    ) -> None:
        
        # TODO: encapsular propiedades y agregarles el underscore inicial.
        self.coordinates = coordinates
        self.path = path
        self.initial = initial
        self.next_coordinates = next_coordinates