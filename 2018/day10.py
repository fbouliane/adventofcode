from time import sleep

from parse import parse

from utils import challenge_data
from matplotlib import pyplot
import numpy


class Position:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f"p=<{self.x},{self.y}> v=<{self.vx},{self.vy}>"


def parse_positions(data):

    for line in data.split('\n'):
        x, y, vx, vy = parse("position=<{},{}> velocity=<{},{}>", line)
        yield Position(int(x), int(y), int(vx), int(vy))


def move(positions, multiplier=1.0):
    for pos in positions:
        pos.x += pos.vx * multiplier
        pos.y += pos.vy * multiplier


def p1(positions):
    seconds = 0
    new_positions = positions

    move(new_positions, 10117)
    seconds = 10117

    while True:
        graph(new_positions, seconds)

        move(new_positions, 1)
        seconds = seconds + 1
        sleep(5)


def graph(positions, seconds):
    x_points = numpy.asarray([pos.x for pos in positions])
    y_points = numpy.asarray([-pos.y for pos in positions])

    pyplot.scatter(x_points, y_points)
    pyplot.title(f"{seconds} second")
    pyplot.savefig('day10.png', dpi=600)
    # pyplot.show()




print(p1(list(parse_positions(challenge_data(10)))))
