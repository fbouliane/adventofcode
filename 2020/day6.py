from utils import challenge_data, bootstrap
import logging

bootstrap()
logger = logging.getLogger(__name__)

d6 = challenge_data(6)


def parse_anyone(input):
    sums = []
    for group in input.split('\n\n'):
        answers = set("".join(group.split()))
        sums.append(len(answers))
    return sum(sums)

def parse_everone(input):
    sums = []
    for group in input.split('\n\n'):
        people_answers = []
        for people in group.split('\n'):
            responses = "".join(people.split())
            people_answers.append(responses)
        group_answers = set.intersection(*map(set,people_answers))
        sums.append(len(group_answers))
    return sum(sums)

if __name__ == '__main__':
    print(parse_anyone(d6))
    print(parse_everone(d6))

