from dataclasses import dataclass, field
from typing import List

from utils import challenge_data
d2 = challenge_data(2)

Halt= "halt"

program = []

@dataclass
class Context:
    ptr: int = 0
    program: List[int] = field(default_factory=list)
    should_stop: bool = False


def step(c: Context):
    op = c.program[c.ptr]
    if op == 1:
        c.program[c.program[c.ptr + 3]] = c.program[c.program[c.ptr + 1]] + c.program[c.program[c.ptr + 2]]
    elif op == 2:
        c.program[c.program[c.ptr + 3]] = c.program[c.program[c.ptr + 1]] * c.program[c.program[c.ptr + 2]]
    elif op == 99:
        c.should_stop = True


def run_until(c):
    while not c.should_stop:
        step(c)
        c.ptr += 4

def part1():
    program = [int(x) for x in d2.split(',')]
    print(program)
    program[1] = 12
    program[2] = 2
    c = Context(program=program, ptr=0)
    run_until(c)
    print(c.program[0])


def seed_noun_verbs():
    for i in range(0,99):
        for j in range(0,99):
            yield i, j


def part2():
    program = [int(x) for x in d2.split(',')]

    for i, j in seed_noun_verbs():
        p1 = program.copy()
        p1[1] = i
        p1[2] = j

        c = Context(program=p1, ptr=0)
        run_until(c)
        if c.program[0] == 19690720:
            print(i,j)
            return (100* i) + j


if __name__ == '__main__':
    # part1()
    print(part2())

