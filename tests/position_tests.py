from unittest import TestCase as TC, main as run

import sys

sys.path.append('/home/maurodonna/Documentos/Programación/Proyectos/random-maze-generator/src/classes')

from Position import Position


class PositionTests(TC):

    def setUp(self):
        self.p1 = Position()

        self.p1.add_path(2, 1)
        self.p1.add_path(3, 4)
        self.p1.add_path(3, 3)
    
    def test_add_paths(self):
        self.assertEqual(len(self.p1._paths), 2)

    def test_add_path_fails(self):
        self.assertRaises(ValueError, self.p1.add_path, 'hola', 3)
        self.assertRaises(ValueError, self.p1.add_path, 4, -3)
        self.assertRaises(ValueError, self.p1.add_path, 4, 3)


if __name__ == '__main__':
    run()

