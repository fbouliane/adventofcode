from unittest import TestCase

from day2 import parse, validation_rule, count_passwords, validation_rule_2
from day3 import parse_map, Stats, map_traversal
from day4 import parse_passport, is_valid
from utils import inline


class Day4Test(TestCase):
    def test_1(self):
        i = inline("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""")
        it = parse_passport(i)
        p1 = next(it)
        self.assertEqual(True, is_valid(p1))
        self.assertEqual(False, is_valid(next(it)))
        self.assertEqual(True, is_valid(next(it)))

