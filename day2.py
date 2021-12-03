from utils import challenge_data, bootstrap
import logging

bootstrap()
logger = logging.getLogger(__name__)

d2 = challenge_data(2)

def part1(input):
    x = 0
    y = 0
    for step in input:
        direction, qty = step.split(' ')
        qty = int(qty)
        if 'forward' == direction:
            x+=qty
        elif 'down' == direction:
            y+=qty
        elif 'up' == direction:
            y-=qty
    return (x, y)

def part2(input):
    x = 0
    y = 0
    aim = 0
    for step in input:
        direction, qty = step.split(' ')
        qty = int(qty)
        if 'forward' == direction:
            x += qty
            y += aim * qty
        elif 'down' == direction:
            aim+=qty
        elif 'up' == direction:
            aim-=qty
    return (x, y, aim)



if __name__ == '__main__':
    input = [s.strip() for s in d2.split('\n')]
    print(part1(input))

    x, y, _ = part2(input)
    print(x*y)
