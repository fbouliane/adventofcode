from collections import Counter
from dataclasses import dataclass
from itertools import tee

from utils import challenge_data
d4 = challenge_data(4)


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def strictly_increasing(number):
    old = number[0]
    for n in number[1:]:
        if n < old:
            return False
        old = n
    return True

def has_same_number_twice(number):
    for a, b in pairwise(number):
        if a == b:
            return True
    return False

def has_same_number_only_twice(number):
    c = Counter(number)
    return 2 in c.values()

def validate_number_p1(number):
    return strictly_increasing(number) and has_same_number_twice(number)

def validate_number_p2(number):
    return strictly_increasing(number) and has_same_number_only_twice(number)

def part1(lower , upper):
    passwords = range(lower, upper)
    validated = [password for password in passwords if validate_number_p1(str(password))]
    return len(validated)

def part2(lower , upper):
    passwords = range(lower, upper)
    validated = [password for password in passwords if validate_number_p2(str(password))]
    return len(validated)

if __name__ == '__main__':
    lower, upper = d4.split('-')
    # print(part1(int(lower), int(upper)))
    print(part2(int(lower), int(upper)))
