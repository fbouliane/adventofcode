from utils import challenge_data, bootstrap
import logging

bootstrap()
logger = logging.getLogger(__name__)

d3 = challenge_data(3)


def most_common(col):
    return int(sum([int(i) for i in col]) >= (len(col) / 2))


def part1(input):
    size_x, size_y = len(input[0]), len(input)
    gamma = [0] * size_x
    epsilon = gamma.copy()
    for col_i in range(0, size_x):
        gamma[col_i] = most_common([input[j][col_i] for j in range(0, size_y)])
        epsilon[col_i] = int(gamma[col_i] == 0)
    return int(''.join([str(i) for i in gamma]), 2), int(''.join([str(i) for i in epsilon]), 2)


def filter_gcd_lcd(input, shift=0, gcd=True):
    common = most_common([i[shift] for i in input])
    if gcd:
        filter = [i for i in input if int(i[shift]) == common]
    else:
        filter = [i for i in input if int(i[shift]) != common]
    return common, filter


def part2(input):
    size_x, size_y = len(input[0]), len(input)
    list = input.copy()
    for mask_index in range(0, size_x):
        common, list = filter_gcd_lcd(list, mask_index)
        if len(list) == 1:
            o2 = int(list[0], 2)

    list = input.copy()
    for mask_index in range(0, size_x):
        common, list = filter_gcd_lcd(list, mask_index, False)
        if len(list) == 1:
            co2 = int(list[0], 2)

    return o2, co2


if __name__ == '__main__':
    input = [[int(i) for i in list(s)] for s in d3.split('\n')]
    gamma, epsilon = part1(input)
    print(gamma * epsilon)

    input = [s for s in d3.split('\n')]
    o2, co2 = part2(input)
    print(o2 * co2)
