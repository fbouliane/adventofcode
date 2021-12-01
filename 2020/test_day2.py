from unittest import TestCase

from day2 import parse, validation_rule, count_passwords, validation_rule_2
from utils import inline


class Day2Test(TestCase):
    def test_1(self):
        input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
        results = list(parse(input))
        print(results)

    def test_policy(self):
        self.assertEqual(True, validation_rule('1-3 a', 'abcde'))
        self.assertEqual(False, validation_rule('1-3 b', 'cdefg'))
        self.assertEqual(True, validation_rule('2-9 c', 'ccccccccc'))

    def test_d2(self):
        input = inline("""1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc""")
        print(input)
        self.assertEqual(2, count_passwords(input))

    def test_d2_p2(self):
        input = inline("""1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc""")
        for pp in parse(input):
            if validation_rule_2(*pp):
                print(f'password {pp} valid')

