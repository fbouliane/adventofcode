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


def p1(positions):
    seconds = 0
    new_positions = positions

    while True:
        graph(new_positions)

        for pos in new_positions:
            pos.x = pos.x + pos.vx
            pos.y = pos.y + pos.vy
        seconds = seconds + 1

        sleep(0.2)


def graph(positions):
    x_points = numpy.asarray([pos.x for pos in positions])
    y_points = numpy.asarray([pos.y for pos in positions])

    pyplot.scatter(x_points, y_points)
    pyplot.show()


print(p1(list(parse_positions(challenge_data(10)))))
