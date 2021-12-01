import math
from dataclasses import dataclass

from utils import challenge_data, bootstrap
import logging

bootstrap()
logger = logging.getLogger(__name__)

d3 = challenge_data(3)

@dataclass
class Stats:
    pos_x: int = 0
    pos_y: int = 0
    trees: int = 0

TREE = '#'

def map_traversal(map, stats, slope=None):
    slope = slope or (3,1)
    while stats.pos_y <= map_height(map):
        stats.pos_x += slope[0]
        stats.pos_y += slope[1]
        try:
            if get_map(map, stats.pos_x, stats.pos_y) == TREE:
                stats.trees += 1
        except Exception:
            pass
        yield stats

def map_height(map):
    return len(map)

def get_map(map, pos_x, pos_y):
    first_line_length = len(map[0])
    if pos_y >= len(map):
        raise Exception('Out of bounds')
    return map[pos_y][pos_x % first_line_length]

def parse_map(map):
    return [list(e) for e in map.split('\n')]

def exhaust_iter_until_last(i):
    try:
        while True:
            last = next(i)
    except StopIteration:
        pass
    return last


if __name__ == '__main__':
    i = map_traversal(parse_map(d3), Stats())
    last = exhaust_iter_until_last(i)
    print(last.trees)

    slopes = {}
    for slope in [(1,1), (3,1), (5,1), (7,1), (1, 2)]:
        i = map_traversal(parse_map(d3), Stats(), slope)
        last = exhaust_iter_until_last(i)
        slopes[str(slope)] = last.trees

    print(slopes)
    print(math.prod(slopes.values()))


