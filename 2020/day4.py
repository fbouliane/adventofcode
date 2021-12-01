import logging
from dataclasses import dataclass, field

from utils import challenge_data, bootstrap
import re

bootstrap()
logger = logging.getLogger(__name__)

d4 = challenge_data(4)

@dataclass
class Passport:
    pfields: dict = field(default_factory=dict)
    raw: str = ''

def parse_passport(input):
    for passport in input.split('\n\n'):
        p = Passport()
        p.raw = passport
        for field in passport.split():
            key, value = field.split(':')
            p.pfields[key] = value
        yield p

def is_valid(p: Passport):
    return {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(p.pfields.keys())

def is_valid_v2(p: Passport):
    if not {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(p.pfields.keys()):
        return False
    if not 1920 <= int(p.pfields['byr']) <= 2002:
        return False
    if not 2010 <= int(p.pfields['iyr']) <= 2020:
        return False
    if not 2020 <= int(p.pfields['eyr']) <= 2030:
        return False
    height_unit = p.pfields['hgt'][-2:]
    height_value= p.pfields['hgt'][:-2]
    if height_unit not in ['cm', 'in']:
        return False
    if height_unit == 'cm' and not 150 <= int(height_value) <= 193:
        return False
    if height_unit == 'in' and not 59 <= int(height_value) <= 76:
        return False
    if not re.match(r'^#[0-9a-f]{6}$', p.pfields['hcl']):
        return False
    if p.pfields['ecl'] not in ['amb','blu', 'brn', 'gry', 'grn','hzl','oth']:
        return False
    if len(p.pfields['pid']) != 9 or not p.pfields['pid'].isdecimal():
        return False
    return True

def count_valid(input):
    passports = list(parse_passport(input))
    valid = [p for p in passports if is_valid(p)]
    return len(valid)

def count_valid_v2(input):
    passports = list(parse_passport(input))
    valid = [p for p in passports if is_valid_v2(p)]
    return len(valid)


if __name__ == '__main__':
    print(count_valid(d4))
    print(count_valid_v2(d4))

