from unittest import TestCase
from day7 import *


example_text = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''


class Day7Test(TestCase):
    def test_p1_same_result(self):

        parsed = process(example_text)

        self.assertEqual('CABDFE', ''.join(p1(parsed)))

    def test_p2_same_result(self):
        parsed = process(example_text)

        p2_iter = iter(p2(parsed))
        self.assertEqual([0, 'C', '.', ''], next(p2_iter))
        self.assertEqual([1, 'C', '.', ''], next(p2_iter))
        self.assertEqual([2, 'C', '.', ''], next(p2_iter))
        self.assertEqual([3, 'A', 'F', 'C'], next(p2_iter))
        self.assertEqual([4, 'B', 'F', 'CA'], next(p2_iter))
        self.assertEqual([5, 'B', 'F', 'CA'], next(p2_iter))
        self.assertEqual([6, 'D', 'F', 'CAB'], next(p2_iter))
        self.assertEqual([7, 'D', 'F', 'CAB'], next(p2_iter))
        self.assertEqual([8, 'D', 'F', 'CAB'], next(p2_iter))
        self.assertEqual([9, 'D', '.', 'CABF'], next(p2_iter))
        self.assertEqual([10, 'E', '.', 'CABFD'], next(p2_iter))
        self.assertEqual([11, 'E', '.', 'CABFD'], next(p2_iter))
        self.assertEqual([12, 'E', '.', 'CABFD'], next(p2_iter))
        self.assertEqual([13, 'E', '.', 'CABFD'], next(p2_iter))
        self.assertEqual([14, 'E', '.', 'CABFD'], next(p2_iter))
        self.assertEqual([15, '.', '.', 'CABFDE'], next(p2_iter))

        with self.assertRaises(StopIteration):
            next(p2_iter)


