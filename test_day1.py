from unittest import TestCase

from day1 import count_increasing, yield_3
from utils import inline

example = """199
200
208
210
200
207
240
269
260
263"""

class Day2Test(TestCase):
    def test_1(self):
        input = [int(s.strip()) for s in example.split('\n')]
        result = count_increasing(input)
        self.assertEqual(7, result)

    def test_2(self):
        input = [int(s.strip()) for s in example.split('\n')]
        sums = [sum(s) for s in yield_3(input)]
        self.assertEqual(5, count_increasing(sums))



