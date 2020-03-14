import unittest

from randomgenerator.randomgenerator import RandomGenerator


class TestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_rangeSeeded_int(self):
		self.assertEqual(426, RandomGenerator.rangeSeeded(12345, 0, 1000))

	def test_rangeSeeded_float(self):
		self.assertEqual(41.66198725453412, RandomGenerator.rangeSeeded(12345, 0.0, 100.0))

	def test_rangeListSeeded(self):
		self.assertEqual([
			0.9317846908693116,
			0.27024484102434043,
			0.43622841061419115,
			0.3730638408978796,
			0.874174337334456
		], RandomGenerator.rangeListSeeded(12345, 5, 0.0, 1.0))

	def test_chooseNSeeded(self):
		data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEqual([6, 0, 4, 5], RandomGenerator.chooseNSeeded(data, 12345, 4))
