"""Doctests Python
Author: Arturo Aviles

Instructions: Run in the bash:

	python test.py
"""

import unittest

import basic_math


class MathTests(unittest.TestCase):
	def test_sum2(self):
		assert basic_math.sum2(2, 2) == 4  # 1st way to test

	def test_multiply(self):
		self.assertEqual(basic_math.multiply(2, 2), 4)  # 2nd way to test


class MathTests2(unittest.TestCase):
	def setUp(self):
		self.sum = basic_math.sum2(3, 3)  # 3rd way to test

	def test2_sum2(self):
		self.assertEqual(self.sum, 6)


class MathExceptionTest(unittest.TestCase):
	def test_bad_sum(self):
		with self.assertRaises(TypeError):
			basic_math.sum2("2", 2)


"""More Info:

assertIn(x, y) - Make sure x is a member of y (this is like the in keyword)
assertIsInstance(x, y) - Make sure x is an instance of the y class
assertGreaterEqual(x, y) - Make sure x is greater than or equal to y
assertLessEqual(x, y) - Make sure x is less than or equal to y
"""

if __name__ == "__main__":
	unittest.main()