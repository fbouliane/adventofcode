from unittest import TestCase

from day3 import part1, filter_gcd_lcd, part2
from utils import inline

example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

class Day3Test(TestCase):
    def test_1(self):
        input = [[int(i) for i in list(s)] for s in example.split('\n')]
        gamma, epsilon = part1(input)
        self.assertEqual(22, gamma)
        self.assertEqual(9, epsilon)

    def test2_filter_pass(self):
        input = [s for s in example.split('\n')]
        common, filtered = filter_gcd_lcd(input, 0)
        self.assertEqual(7, len(filtered))
        self.assertEqual(1, common)

        common, filtered = filter_gcd_lcd(filtered, 1)
        self.assertEqual(4, len(filtered))
        self.assertEqual(0, common)

        common, filtered = filter_gcd_lcd(filtered, 2)
        self.assertEqual(3, len(filtered))
        self.assertEqual(1, common)

        common, filtered = filter_gcd_lcd(filtered, 3)
        self.assertEqual(2, len(filtered))
        self.assertEqual(1, common)

        common, filtered = filter_gcd_lcd(filtered, 4)
        self.assertEqual(1, len(filtered))
        self.assertEqual(1, common)

    def test_2(self):
        input = [s for s in example.split('\n')]
        o2,co2 =  part2(input)
        self.assertEqual(23, o2)
        self.assertEqual(10, co2)




