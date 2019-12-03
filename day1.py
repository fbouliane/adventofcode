from utils import challenge_data
from math import floor
d1 = challenge_data(1)


def fuel(mass):
    return floor(mass / 3)-2

def part1(inp):
    return sum([fuel(int(x)) for x in inp])

def rec_fuel(mass):
    mass_sum = []
    m_current = mass
    while True:
        if fuel(m_current) >= 0:
            m_current = fuel(m_current)
            mass_sum.append(m_current)
        else:
            return sum(mass_sum)

def part2(inp):
    return sum([rec_fuel(int(x)) for x in inp])

#modules_mass = d1.split('\n')
#print(part1(modules_mass))
if __name__ == "__main__":
    modules_mass = d1.split('\n')
    print(part1(modules_mass))
    print(part2(modules_mass))

