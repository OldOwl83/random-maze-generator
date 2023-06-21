from unittest import TestCase as TC, main as run

import sys

import env_vars as env
sys.path.append(env.src_path)

import pygame as pg
from classes.maze import Maze
from classes.board import Board
from classes.coordinates import Coordinates, Dimensions


class MazeTests(TC):
    d1 = Dimensions(24, 20)
    s1 = Dimensions(800, 600)
    m1 = Maze(d1, s1)

    def test_parameters_validation(self):
        self.assertRaises(TypeError, Maze, (24, 20), self.s1)
        self.assertRaises(TypeError, Maze, self.d1, (24, 20))
        self.assertRaises(TypeError, Maze, self.d1, 'hola')

        
    def test_board_property_state(self):
        self.assertEqual(len(self.m1._board._board), 24 * 20)
        self.assertEqual(self.m1._board.is_full, True)    
        self.assertEqual(len(self.m1._board.get_open_positions()), 24 * 20)
        for y in range(20):
            for x in range(24):
                self.assertEqual(self.m1._board.get_free_neighbors(Coordinates(x, y)), ())
        

if __name__ == '__main__':
    run()

