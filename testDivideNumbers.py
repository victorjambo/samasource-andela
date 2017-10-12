import unittest
from divideNumbers import *

class TestDivideNumbers(unittest.TestCase):
	def test_output_is_equal(self):
		self.assertEqual(divide(4,2),2)
	def test_division_of_positive(self):
		self.assertEqual(divide(-4,2),-2)
	def test_division_of_negatives(self):
		self.assertEqual(divide(-4,-2),2)
	def test_input_is_not_a_list(self):
		self.assertRaises(TypeError, divide, [2,4])
	def test_input_is_not_a_dictionary(self):
		self.assertRaises(TypeError, divide, {"one":2, "two":4})
	def test_division_by_zero(self):
		try:
			divide(4,0)
		except ZeroDivisionError:
			self.fail("ZeroDivisionError")
if __name__ == "__main__":
	unittest.main(exit = False)