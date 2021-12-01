from unittest import TestCase
from day1 import rec_fuel

class Day1(TestCase):
	def test_part2(self):
		self.assertEqual(2, rec_fuel(14))
		self.assertEqual(966, rec_fuel(1969))
		self.assertEqual(50346, rec_fuel(100756))
		
		