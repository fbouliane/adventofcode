from utils import challenge_data
import itertools

d1 = challenge_data(1)


def part1():
    total = 0
    for elem in d1.split('\n'):
        if elem[0] == '+':
            total += int(elem[1:])
        elif elem[0] == '-':
            total -= int(elem[1:])
    return total


def part2():
    total = 0
    seen = []
    for elem in itertools.cycle(d1.split('\n')):
        if elem[0] == '+':
            total += int(elem[1:])
        elif elem[0] == '-':
            total -= int(elem[1:])
        if total in seen:
            break
        seen.append(total)

    return total

print(part2())
