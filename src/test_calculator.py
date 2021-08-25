"""
Testing src/calculator.py

"""

import unittest
import src.calculator

class CalculatorTest(unittest.TestCase):
    """Tests performed on the Calculator class"""
    
    def setUp(self):
        """Set up our test"""
        self.calc = src.calculator.Calculator()
    
    def test_add_adds_all_numbers(self):
        self.assertEqual(self.calc.add(9), 9)
        self.assertEqual(self.calc.add(972, 13, 1312), 2297)
        self.assertEqual(self.calc.add(100, 2, 99, 1), 202)
        self.assertEqual(self.calc.add(11, 87, 29, 18, 19, 242, 7), 413)
        
    def test_multiply_multiplies_all_numbers(self):
        self.assertEqual(self.calc.multiply(9), 9)
        self.assertEqual(self.calc.multiply(972, 13, 1312), 16578432)
        self.assertEqual(self.calc.multiply(100, 2, 99, 1), 19800)
        self.assertEqual(self.calc.multiply(11, 87, 29, 18, 19, 242, 7), 16078645044)
    
    def test_divide_divides_all_numbers(self):
        self.assertEqual(self.calc.divide(9), 0.1111111111111111)
        self.assertEqual(self.calc.divide(972, 13, 1312), 6.031933538708607e-08)
        self.assertEqual(self.calc.divide(100, 2, 99, 1), 5.0505050505050505e-05)
        self.assertEqual(self.calc.divide(11, 87, 29, 18, 19, 242, 7), 6.2194295431204e-11)

    def test_that_result_is_set_to_total_after_an_operation(self):
        self.assertEqual(self.calc.result(), 0)
        self.calc.divide(9)
        self.assertEqual(self.calc.result(), 0.1111111111111111)
        self.calc.add(972, 13, 1312)
        self.assertEqual(self.calc.result(), 2297)
        self.calc.multiply(11, 87, 29, 18, 19, 242, 7)
        self.assertEqual(self.calc.result(), 16078645044)
