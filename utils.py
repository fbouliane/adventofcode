import sys

from aocd import get_data


def challenge_data(day, year=2021):
    return get_data(day=day, year=year)

def bootstrap():
    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def inline(input):
    return "\n".join([i.strip() for i in input.split("\n")])
