from utils import challenge_data, bootstrap
import logging

bootstrap()
logger = logging.getLogger(__name__)

d1 = challenge_data(1)


def count_increasing(list):
    increasing = 0
    old_elem = None
    for i, elem in enumerate(list):
        if not old_elem or elem <= old_elem:
            pass
        else:
            increasing +=1
        old_elem = elem
    return increasing

def yield_3(list):
    for i in range(2, len(list)):
        yield (list[i-2], list[i-1], list[i])


def part2(input):
    sums = [sum(s) for s in yield_3(input)]
    return count_increasing(sums)


if __name__ == '__main__':
    input = [int(s.strip()) for s in d1.split('\n')]
    print(count_increasing(input))

    input = [int(s.strip()) for s in d1.split('\n')]
    print(part2(input))


