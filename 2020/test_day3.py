from unittest import TestCase

from day2 import parse, validation_rule, count_passwords, validation_rule_2
from day3 import parse_map, Stats, map_traversal
from utils import inline


class Day2Test(TestCase):
    def test_1(self):
        i = inline("""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""")
        map = parse_map(i)
        s = Stats()
        r = map_traversal(map, s)
        stats1 = next(r)
        self.assertEqual(3, stats1.pos_x)
        self.assertEqual(1, stats1.pos_y)
        self.assertEqual(0, stats1.trees)
        stats2 = next(r)
        self.assertEqual(6, stats2.pos_x)
        self.assertEqual(2, stats2.pos_y)
        self.assertEqual(1, stats2.trees)

    def test_2(self):
        i = inline("""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""")

        i = map_traversal(parse_map(i), Stats())
        last = self.exhaust_iter_until_last(i)
        self.assertEqual(7, last.trees)



