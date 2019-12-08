import functools
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from math import floor

from utils import challenge_data
d5 = challenge_data(5)

import logging


class Operations(Enum):
    ADD = 1
    MUL = 2
    INPUT = 3
    OUTPUT = 4
    JUMPIFTRUE = 5
    JUMPIFFALSE=6
    LESSTHAN=7
    EQUALS=8
    HALT=99


class ParameterModes(Enum):
    Position = 0
    Immediate = 1


@dataclass
class Context:
    ptr: int = 0
    program: List[int] = field(default_factory=list)
    should_stop: bool = False
    next: int = None
    inputs: List[int] = field(default_factory=list)
    outputs: List[int] = field(default_factory=list)
    input_index: int = 0


def reforval(ptr, mode, program):
    val = program[ptr]
    imode = int(mode)
    if imode == ParameterModes.Position.value:
        return program[val]
    elif imode == ParameterModes.Immediate.value:
        return val


def reforvaloffset(offset, ptr, modes, program, address=False):
    if address:
        modes = '111'
    return reforval(ptr + offset + 1, modes[offset], program)


def get_mode(instruction):
    modes = floor(instruction / 100)
    modes = str(modes).zfill(3)
    return modes[::-1]


def step(c: Context):
    op = c.program[c.ptr] % 100
    modes = get_mode(c.program[c.ptr])
    val = functools.partial(reforvaloffset, ptr=c.ptr, modes=modes, program=c.program)
    op = Operations(op)
    print(f'OP {op}')
    if op == Operations.ADD:
        c.program[val(2, address=True)] = val(0) + val(1)
    elif op == Operations.MUL:
        c.program[val(2, address=True)] = val(0) * val(1)
    elif op == Operations.INPUT:
        c.program[val(0, address=True)] = c.inputs[c.input_index]
        c.input_index += 1
        c.next = c.ptr + 2
    elif op == Operations.JUMPIFTRUE:
        if val(0) != 0:
            c.next = val(1)
        else:
            c.next = c.ptr + 3
    elif op == Operations.JUMPIFFALSE:
        if val(0) == 0:
            c.next = val(1)
        else:
            c.next = c.ptr + 3
    elif op == Operations.LESSTHAN:
        if val(0) < val(1):
            c.program[val(2, address=True)] = 1
        else:
            c.program[val(2, address=True)] = 0
    elif op == Operations.EQUALS:
        if val(0) == val(1):
            c.program[val(2, address=True)] = 1
        else:
            c.program[val(2, address=True)] = 0
    elif op == Operations.OUTPUT:
        output = val(0)
        c.next = c.ptr + 2
        c.outputs.append(output)
        print(f'output {output}')
    elif op == Operations.HALT:
        c.should_stop = True


def run_until_output_or_halt(c):
    while not c.should_stop:
        c.next = c.ptr + 4
        if Operations(c.program[c.ptr] % 100) == Operations.OUTPUT:
            step(c)
            c.ptr = c.next
            return c.outputs[-1]
        step(c)
        c.ptr = c.next


def run_until(c):
    while not c.should_stop:
        c.next = c.ptr + 4
        step(c)
        c.ptr = c.next


def part1(program):
    c = Context(program=list(program), ptr=0)
    c.inputs = [1]
    run_until(c)

def part2(program):
    c = Context(program=list(program), ptr=0)
    c.inputs = [5]
    run_until(c)



if __name__ == '__main__':
    program = list(map(int, d5.split(',')))
    print(program)
    print(part1(program))
    print('---')
    print(part2(program))




