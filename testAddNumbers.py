import unittest
from addNumbers import *

class TestAddNumbers(unittest.TestCase):
	def test_input_is_list(self):
		self.assertRaises(TypeError, add_numbers, [2,4])
	def test_output_is_number(self):
		self.assertIsInstance(add_numbers(5,6), int)
	def test_output_is_equal(self):
		self.assertEqual(add_numbers(2,3),5)

if __name__ == "__main__":
	unittest.main(exit = False)