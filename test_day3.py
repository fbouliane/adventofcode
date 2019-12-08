from unittest import TestCase

from day3 import manhattan, Position, some_step, coord_by_step, find_conflicts, part1, part2


class Day3(TestCase):
    def test_manhattan(self):
        self.assertEqual(6, manhattan(Position(3,3)))
        self.assertEqual(6, manhattan(Position(3,-3)))

    def test_tracing(self):
        direction = 'R3'
        position = Position(0,0)

        i = iter(some_step(direction, position))
        self.assertEqual((1,0), next(i))
        self.assertEqual((2,0), next(i))
        self.assertEqual((3,0), next(i))

    def test_coord_by_step(self):
        instructions = ['R1', 'D1']

        steps = coord_by_step(instructions, Position(0,0))
        self.assertEqual([(0,0),(1,0),(1,-1)], steps)

    def test_find_conflicts(self):
        path1 = [(0,0),(2,2),(5,5)]
        path2 = [(0,0),(3,3),(5,5)]

        conflicts = list(find_conflicts(path1, path2))
        self.assertEqual((0,0), conflicts[0])
        self.assertEqual((5,5), conflicts[1])

    def test_part1(self):
        result = part1(['R1', 'R1', 'R1'], ['D1', 'R1', 'R1', 'U1'])

        self.assertEqual(2, result)

    def test_examples(self):
        result = part1('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
                       'U62,R66,U55,R34,D71,R55,D58,R83'.split(','))
        self.assertEqual(159, result)

        result2 = part1('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
                       'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))
        self.assertEqual(135, result2)

    def test_part2(self):
        result = part2('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
                       'U62,R66,U55,R34,D71,R55,D58,R83'.split(','))
        self.assertEqual(610, result)

        result2 = part2('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
                        'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))
        self.assertEqual(410,result2)

