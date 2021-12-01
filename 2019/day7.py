import functools
import itertools

from day5 import Context, run_until, run_until_output_or_halt
from utils import challenge_data
d7 = challenge_data(7)


class HaltException(Exception):
    pass


class FeedbackModeAmp:
    def __init__(self, phase, program):
        self.phase = phase
        self.program = program

        self.c = Context(program=list(program), ptr=0)
        self.c.inputs = [phase]

    def input(self, input):
        self.c.inputs.append(input)

    def wait_for_output(self) -> int:
        result = run_until_output_or_halt(self.c)
        if not result:
            raise HaltException()
        return result

'''
inject
wait_for_output
(pause)
inject
wait_for_output
if halt:
'''


def amplifier(input, phase, program):
    c = Context(program=list(program), ptr=0)
    c.inputs = [phase, input]
    run_until(c)
    return c.outputs[0]


def total_output(program, phases):
    quickamp = functools.partial(amplifier, program=program)
    input = 0
    output = 0
    for i in range(0, 5):
        output = quickamp(input, phases[i])
        input = output
    return output


def part1(p):
    thruster_signals = {}
    combinations = itertools.permutations([4,3,2,1,0])
    for phase in combinations:
        output = total_output(list(p), phase)
        thruster_signals[output] = phase
    return max(thruster_signals.keys())


def run_with_one_phase(phases, program):
    amplifiers = [FeedbackModeAmp(phases[i], list(program)) for i in range(0, 5)]
    something_halted = False
    input = 0
    output = 0
    while not something_halted:
        for i in range(0, 5):
            try:
                amplifiers[i].input(input)
                output = amplifiers[i].wait_for_output()
                input = output
            except HaltException:
                something_halted = True
                break
    return output


def part2(p):
    thruster_signals = {}
    combinations = itertools.permutations([5,6,7,8,9])
    for phase in combinations:
        output = run_with_one_phase(phase, list(p))
        thruster_signals[output] = phase
    return max(thruster_signals.keys())


if __name__ == '__main__':
    program = list(map(int, d7.split(',')))
    print(part1(program))

    print(part2(program))
