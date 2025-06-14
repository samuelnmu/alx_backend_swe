import unittest
import cube
from math import isclose

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cube.cuboid_volume(2), 8)
        self.assertAlmostEqual(cube.cuboid_volume(1), 1)
        self.assertAlmostEqual(cube.cuboid_volume(0), 0)
        self.assertAlmostEqual(cube.cuboid_volume(5.5), 166.375)
    
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            cube.cuboid_volume("two")
        with self.assertRaises(TypeError):
            cube.cuboid_volume(2j)
        with self.assertRaises(ValueError):
            cube.cuboid_volume(-2.5)

if __name__ == '__main__':
    unittest.main()