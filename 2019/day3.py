from dataclasses import dataclass

from utils import challenge_data
d3 = challenge_data(3)


@dataclass
class Position:
    x : int = 0
    y : int = 0

@dataclass
class Conflict:
    pos : Position
    dist_a : int
    dist_b : int


def manhattan(pos: Position):
    return abs(pos.x) + abs(pos.y)


def some_step(instruction, position: Position):
    direction = instruction[0].upper()
    distance = int(instruction[1:])
    x = position.x
    y = position.y
    while distance > 0:
        if direction == 'U':
            y=y+1
        elif direction == 'D':
            y=y-1
        elif direction == 'L':
            x=x-1
        elif direction == 'R':
            x=x+1
        distance = distance - 1
        yield x, y


def coord_by_step(instructions, initial_position: Position):
    position_history=[(initial_position.x, initial_position.y)]
    position = initial_position
    for instruction in instructions:
        for step in some_step(instruction, position):
            position_history.append(step)
            position.x = step[0]
            position.y = step[1]
    return position_history


def find_conflicts(a, b):
    conflicts = list(set(a) & set(b))
    for conflict in conflicts:
        yield Conflict(Position(conflict), a.index(conflict)+1, b.index(conflict)+1)

    # for pos_a in a:
    #     for pos_b in b:
    #         if pos_a == pos_b:
    #             yield pos_a


def part1(instructions_a, instructions_b):
    history_a = coord_by_step(instructions_a, Position(0,0))
    history_b = coord_by_step(instructions_b, Position(0,0))

    conflicts = list(find_conflicts(history_a[1:], history_b[1:]))

    conflict_cost = {}
    for conflict in conflicts[1:]:
        cost = manhattan(Position(conflict.pos.x, conflict.pos.y))
        conflict_cost[cost] = Position(conflict.pos.x, conflict.pos.y)

    cheaper = min(conflict_cost.keys())
    return cheaper


def part2(instructions_a, instructions_b):
    history_a = coord_by_step(instructions_a, Position(0,0))
    history_b = coord_by_step(instructions_b, Position(0,0))

    conflicts = list(find_conflicts(history_a[1:], history_b[1:]))

    conflict_cost = {}
    for conflict in conflicts[1:]:
        cost = conflict.dist_a + conflict.dist_b
        conflict_cost[cost] = Position(conflict.pos.x, conflict.pos.y)

    cheaper = min(conflict_cost.keys())
    return cheaper

if __name__ == '__main__':
    patha, pathb = d3.split('\n')
    # print(part1(patha.split(','), pathb.split(',')))
    print(part2(patha.split(','), pathb.split(',')))

