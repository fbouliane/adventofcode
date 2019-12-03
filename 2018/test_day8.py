from unittest import TestCase
from day8 import *


class Day8Test(TestCase):
    def test_parses_basic_and_metadata(self):
        n = next_node([0,1,9], 0)
        self.assertEqual(n.start, 0)
        self.assertEqual(n.end, 2)
        self.assertEqual(n.child_count, 0)
        self.assertEqual(n.metadata_count, 1)
        self.assertEqual(n.metadata, [9])

    def test_parses_with_null_child(self):
        n = next_node([1,1,0,0,9], 0)
        self.assertEqual(n.start, 0)
        self.assertEqual(n.end, 4)
        self.assertEqual(n.child_count, 1)
        self.assertEqual(n.metadata_count, 1)
        self.assertEqual(n.metadata, [9])
        
    def test_parse_example(self):
        data = [2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2]
        # n = next_node(data, 0)
        print(p1(data))

    def test_parses_total(self):
        n = next_node([1,1,0,0,1], 0)
        self.assertEqual(n.value(), 0)