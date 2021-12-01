from unittest import TestCase

from day6 import parse_anyone, parse_everone


class Day6Test(TestCase):
    def test_1(self):
        input = 'abc'
        self.assertEqual(3, parse_anyone(input))

        input = 'a\nb\nc'
        self.assertEqual(3, parse_anyone(input))

        input = 'ab\nac'
        self.assertEqual(3, parse_anyone(input))

        input = 'a\na\na\na'
        self.assertEqual(1, parse_anyone(input))

        input = 'b'
        self.assertEqual(1, parse_anyone(input))

    def test_total(self):
        input = """abc
        
        a
        b
        c
        
        ab
        ac
        
        a
        a
        a
        a
        
        b"""
        self.assertEqual(11, parse_anyone("".join([i.strip(' ') for i in input])))



class Day6TestPart2(TestCase):
    def test_simple(self):
        input = 'abc'
        self.assertEqual(3, parse_everone(input))

        input = 'a\na\na'
        self.assertEqual(1, parse_everone(input))

        input = 'a\nb\nc'
        self.assertEqual(0, parse_everone(input))

        input = 'ab\nac'
        self.assertEqual(1, parse_everone(input))

        input = 'a\na\na\na'
        self.assertEqual(1, parse_everone(input))

        input = 'b'
        self.assertEqual(1, parse_everone(input))
