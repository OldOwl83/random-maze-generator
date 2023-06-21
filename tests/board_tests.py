from unittest import TestCase as TC, main as run

import sys

sys.path.append('/home/maurodonna/Documentos/Programación/Proyectos/random-maze-generator/src')

import pygame as pg
from classes.board import Board
from classes.coordinates import Coordinates, Dimensions


class CoordinatesTests(TC):
    d1 = Dimensions(24, 20)
    s1 = Dimensions(800, 600)

    b1 = Board(d1, s1)

    def test_parameters_validation(self):
        self.assertRaises(TypeError, Board, (24, 20), self.s1)
        self.assertRaises(TypeError, Board, self.d1, (24, 20))
        self.assertRaises(TypeError, Board, self.d1, 'hola')

        
    def test_board_property_state(self):
        self.assertEqual(len(self.b1._board), 24 * 20)
        self.assertEqual(self.b1.is_full, False)
        self.assertEqual(max(self.b1._board.keys())._rect.bottomright, (798, 598))
        

    def test_methods(self):
        self.assertEqual(self.b1.get_dimensions(), self.d1)
        self.assertEqual(len(self.b1.get_all_positions()), 24 * 20)
        self.assertEqual(self.b1.get_open_positions(), ())
        self.assertEqual(self.b1.get_free_neighbors(Coordinates(4, 4)), ((4, 3), (4, 5), (3, 4), (5, 4)))
        self.b1.connect_neighbor(Coordinates(4, 4), Coordinates(4, 5))
        self.assertEqual(self.b1.get_free_neighbors(Coordinates(4, 4)), ((4, 3), (3, 4), (5, 4)))
        self.assertEqual(self.b1.get_surface().get_rect(), pg.Rect(0, 0, 800, 600))

if __name__ == '__main__':
    run()

