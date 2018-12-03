from collections import defaultdict

from parse import parse

from utils import challenge_data

map = defaultdict(int)
id_map = dict()

for claim in challenge_data(3).split('\n'):
    r = parse('#{:d} @ {:d},{:d}: {:d}x{:d}', claim)
    claim_id, left, top, width, height = r

    for x in range(left, left+width):
        for y in range(top, top+height):
            map[(x, y)] += 1


def p1():
    square_inch=0
    for k, v in map.items():
        if v>=2:
            square_inch += 1


for claim in challenge_data(3).split('\n'):
    r = parse('#{:d} @ {:d},{:d}: {:d}x{:d}', claim)
    claim_id, left, top, width, height = r

    altered=False
    for x in range(left, left+width):
        for y in range(top, top+height):
            if map[(x, y)] != 1:
                altered = True

    if not altered:
        print(claim_id)