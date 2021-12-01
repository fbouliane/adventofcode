from utils import challenge_data, bootstrap
import logging

bootstrap()
logger = logging.getLogger(__name__)

d2 = challenge_data(2)

def parse(input):
    for policypassword in input.split('\n'):
        policy, password = policypassword.split(':')
        yield policy, password.strip()

def validation_rule(policy, password):
    _, subject = policy.split(' ')
    fromm, to = _.split('-')

    return int(fromm) <= list(password).count(subject) <= int(to)

def validation_rule_2(policy, password):
    _, subject = policy.split(' ')
    fromm, to = _.split('-')

    return bool(password[int(fromm)-1] == subject) ^ bool(password[int(to)-1] == subject)


def count_passwords(input):
    sum = 0
    for pp in parse(input):
        if validation_rule(*pp):
            sum+=1
    return sum


def count_passwords_v2(input):
    sum = 0
    for pp in parse(input):
        if validation_rule_2(*pp):
            sum+=1
    return sum


if __name__ == '__main__':
    print(count_passwords(d2))
    print(count_passwords_v2(d2))

