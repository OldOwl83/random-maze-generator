from unittest import TestCase as TC, main as run

import sys

sys.path.append('/home/maurodonna/Documentos/Programación/Proyectos/random-maze-generator/src/classes')

from Board import Board
from Coordinates import Coordinates


class CoordinatesTests(TC):
    max_dim = (10, 10)
    c1 = Coordinates(3, 4, max_dim)
    c2 = Coordinates(3, 4, max_dim)
    c3 = Coordinates(2, 2)

    def test_coordinates_validation(self):
        self.assertRaises(TypeError, Coordinates, 2, 'hola')
        self.assertRaises(ValueError, Coordinates, -1, 0)
        self.assertRaises(ValueError, Coordinates, 12, 9, self.max_dim)
        self.assertRaises(TypeError, Coordinates, 12, 9, 'hola')
        self.assertRaises(TypeError, Coordinates, 12, 9, (4, 'hola'))
        self.assertRaises(TypeError, Coordinates, 12, 9, ('hola', 5))

    def test_coordinates_equality(self):
        self.assertEqual(self.c1, tuple((3, 4)))
        self.assertEqual(self.c1, self.c2)

        d1 = {
            self.c1: 'hola',
            self.c2: 'chau'
        }
        
        self.assertEqual(len(d1), 1)
        self.assertEqual(d1.get((3, 4)), 'chau')

    def test_properties_operations(self):
        self.assertEqual(self.c1.x, 3)
        self.assertEqual(self.c1.y, 4)
        self.assertEqual(self.c1.max_dim, (10, 10))

        def x_assignement():
            self.c1.x = 2

        def y_assignement():
            self.c1.y = 2

        def max_dim_assignement():
            self.c1.max_dim = (12, 12)

        self.assertRaises(TypeError, x_assignement)
        self.assertRaises(TypeError, y_assignement)
        self.assertRaises(TypeError, max_dim_assignement)

    def test_displacements(self):
        self.assertEqual(self.c1.up(4), Coordinates(3, 8))
        self.assertEqual(self.c1.down(2), Coordinates(3, 2))
        self.assertEqual(self.c1.left(2), Coordinates(1, 4))
        self.assertEqual(self.c1.right(3), Coordinates(6, 4))

        self.assertRaises(ValueError, self.c1.left, 4)
        self.assertRaises(ValueError, self.c1.down, 5)
        self.assertRaises(ValueError, self.c1.up, 6)
        self.assertRaises(ValueError, self.c1.right, 7)


if __name__ == '__main__':
    run()

