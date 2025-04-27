from unittest import TestCase as TC, main as run

import sys

import env_vars as env
sys.path.append(env.src_path)

from classes.coordinates import Coordinates, Dimensions, Position


class CoordinatesTests(TC):
    c1 = Coordinates(3, 4)
    c2 = Coordinates(3, 4)
    c3 = Coordinates(2, 2)
    p1 = Position(2, 2)

    def test_coordinates_validation(self):
        self.assertRaises(TypeError, Coordinates, 2, 'hola')
        self.assertRaises(TypeError, Coordinates, 2.0, 2)
        self.assertRaises(ValueError, Dimensions, -1, 0)
        self.assertRaises(TypeError, Position, 3, 3, 3)
        
    def test_coordinates_equality(self):
        self.assertEqual(self.c1, (3, 4))
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
        
        def x_assignement():
            self.c1.x = 2

        def y_assignement():
            self.c1.y = 2

        def left_assignement():
            self.c1.left = (12, 12)

        self.assertRaises(AttributeError, x_assignement)
        self.assertRaises(AttributeError, y_assignement)
        self.assertRaises(AttributeError, left_assignement)

    def test_displacements(self):
        self.assertEqual(self.c1.up, Coordinates(3, 3))
        self.assertEqual(self.c1.down, Coordinates(3, 5))
        self.assertEqual(self.c1.left, Coordinates(2, 4))
        self.assertEqual(self.c1.right, Coordinates(4, 4))
        self.assertEqual(self.c1, (3, 4))
        
    def test_dimensions_operations(self):
        d1 = Dimensions(2, 2)
        d2 = Dimensions(3, 3)
        
        self.assertEqual(d1 + d2, (5, 5))
        self.assertEqual(d2 - d1, (1, 1))
        self.assertRaises(ValueError, lambda: d1 - d2)
        
        self.assertEqual(d1 * 2, (4, 4))
        self.assertEqual(d1 * 0.5, (1, 1))
        self.assertEqual(d1 * 0.6, (1, 1))
        self.assertEqual(d1 * (2, 4), (4, 8))
        self.assertRaises(ValueError, lambda: d2 * -2)
        
        self.assertEqual(d2 / 3, (1, 1))
        self.assertEqual(d2 / 2, (2, 2))
        self.assertEqual(d2 / 2.1, (1, 1))
        self.assertEqual(d1 / d2 , (1, 1))
        self.assertRaises(ValueError, lambda: d2 / -2)
        
    def test_position_methods(self):
        self.assertFalse(self.p1)
        
        self.p1.add_open_neighbor((2, 3))
        self.assertEqual(self.p1.get_open_neighbors(), ((2, 3),))
        self.assertTrue(self.p1)
        self.assertTrue(self.p1.is_neighbor_open((2, 3)))
        
        self.p1.remove_open_neighbor((2, 3))
        self.assertFalse(self.p1)
        
        

if __name__ == '__main__':
    run()

