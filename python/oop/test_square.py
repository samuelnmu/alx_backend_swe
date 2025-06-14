import unittest
from square import square

class TestSquareFunction(unittest.TestCase):
    
    # Test positive integers
    def test_positive_integers(self):
        self.assertEqual(square(2), 4)    # Exact match
        self.assertEqual(square(5), 25)
    
    # Test negative integers
    def test_negative_integers(self):
        self.assertEqual(square(-3), 9)
    
    # Test zero
    def test_zero(self):
        self.assertEqual(square(0), 0)
    
    # Test floating-point numbers
    def test_floats(self):
        self.assertAlmostEqual(square(1.5), 2.25)  # Approximate match
        self.assertAlmostEqual(square(-2.2), 4.84)
    
    # Test invalid inputs
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            square("two")  # Strings
        with self.assertRaises(TypeError):
            square([2])    # Lists

if __name__ == '__main__':
    unittest.main()