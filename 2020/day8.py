import copy
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List

from utils import challenge_data, bootstrap
import logging

bootstrap()
logger = logging.getLogger(__name__)

d8 = challenge_data(8)

class Operator(Enum):
    nop = "nop"
    acc = "acc"
    jmp = "jmp"


@dataclass
class Instruction():
    operator: Operator = None
    operand: Optional[int] = None
    line: Optional[int] = None


def parse_bootcode(input):
    for index, line in enumerate(input.split('\n')):
        i = Instruction()
        operator, operand = line.split(' ')
        i.operator = operator
        i.operand = int(operand)
        i.line = index
        yield i


def parse_all_instructions(input):
    instructions = {}
    for ops in parse_bootcode(input):
        instructions[ops.line] = ops
    return instructions

@dataclass
class ProcessorState:
    pos : int = 0
    accumulator: int = 0
    been_there : List[int] = field(default_factory=list)
    next_pos : Optional[int] = None


def next_instruction(s:ProcessorState, i: Instruction):
    if i.operator == Operator.acc.value:
        s.accumulator += i.operand
        s.next_pos = s.pos + 1
    elif i.operator == Operator.jmp.value:
        s.next_pos = s.pos + i.operand
    elif i.operator == Operator.nop.value:
        s.next_pos = s.pos + 1

class BootLoop(Exception):
    def __init__(self, s : ProcessorState):
        self.s = s

class Finished(Exception):
    def __init__(self, s : ProcessorState):
        self.s = s

def run(instructions):
    state = ProcessorState()
    while True:
        i = instructions[state.pos]
        next_instruction(state, i)
        if state.next_pos in state.been_there:
            raise BootLoop(state)
        elif state.next_pos == len(instructions):
            raise Finished(state)
        else:
            state.been_there.append(state.pos)
            state.pos = state.next_pos
            state.next_pos = None


def run_all(input):
    instructions = parse_all_instructions(input)
    for i in range(0, len(instructions)):
        if instructions[i].operator != Operator.acc.value:
            instructions2 = copy.deepcopy(instructions)
            instructions2[i].operator = {
                Operator.nop.value: Operator.jmp.value,
                Operator.jmp.value: Operator.nop.value
            }[instructions2[i].operator]

            try:
                run(instructions2)
            except BootLoop as e:
                logger.debug(f"Instructions {i} bootloop !")
            except Finished as e:
                logger.debug(f"Finished {i} !")
                print(e.s)
                break

if __name__ == '__main__':
    try:
        instructions = parse_all_instructions(d8)
        run(instructions)
    except:
        pass

    run_all(d8)
