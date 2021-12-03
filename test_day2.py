from unittest import TestCase

from day1 import count_increasing, yield_3
from day2 import part1, part2
from utils import inline

example = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

class Day2Test(TestCase):
    def test_1(self):
        input = [s.strip() for s in example.split('\n')]
        x, y = part1(input)
        self.assertEqual(15, x)
        self.assertEqual(10, y)


    def test_2(self):
        input = [s.strip() for s in example.split('\n')]
        x, y, aim = part2(input)
        self.assertEqual(15, x)
        self.assertEqual(60, y)




