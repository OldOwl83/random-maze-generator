
from classes.game import MazeGame
from classes.coordinates import Dimensions

MazeGame(
    title='RandomMaze',
    icon="../resources/bolita24.png",
    screen_resolution=Dimensions(1000, 780),
    maze_dimensions=Dimensions(32, 26)
).start_game()




        # if ev.type == pg.MOUSEMOTION:
        #     if reset_button_rect.collidepoint(ev.pos):
        #         reset_button_color = 'yellow'
        #     else:
        #         reset_button_color = 'violet'

        # if ev.type == pg.MOUSEBUTTONDOWN:
        #     if reset_button_rect.collidepoint(ev.pos):
        #         maze = Maze((maze_width, maze_height), screen_rect, .8)
        #         finished = False


    # if maze._marble['coord'] == maze._paths[0][-1]:
    #     print_main_path(screen, maze)

    #     finished = True
