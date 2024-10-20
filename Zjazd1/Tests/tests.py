import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(Calculator.add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(Calculator.add(-1, -1), -2)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(Calculator.add(-1, 1), 0)

    def test_subtract_positive_numbers(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)
    
    def test_subtract_negative_from_positive(self):
        self.assertEqual(Calculator.subtract(5, -3), 8)
    
    def test_multiply_positive_numbers(self):
        self.assertTrue(Calculator.multiply(2, 3) == 6)
    
    def test_multiply_negative_numbers(self):
        self.assertTrue(Calculator.multiply(-2, 3) == -6)
    
    def test_divide_positive_numbers(self):
        self.assertEqual(Calculator.divide(6, 3), 2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(6, 0)
    
    def test_power(self):
        self.assertTrue(Calculator.power(2, 0) == 1)

if __name__ == '__main__':
    unittest.main()
