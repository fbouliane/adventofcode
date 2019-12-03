import itertools

from utils import challenge_data
from collections import defaultdict
d2 = challenge_data(2)


def count_letters(word):
    letter_count = defaultdict(int)
    for letter in word:
        letter_count[letter] += 1
    return letter_count


def return_doubles_and_truples(letter_count):
    doubles = 0
    triples = 0
    for k, v in letter_count.items():
        if v == 3:
            triples = 1
        if v == 2:
            doubles = 1

    return doubles, triples


def day2_p1():
    doubles = 0
    triples = 0
    for word in d2.split('\n'):
        letter_count = count_letters(word)
        double, triple = return_doubles_and_truples(letter_count)
        doubles += double
        triples += triple
    return doubles * triples


def day2_p2():
    results = []

    for w1, w2 in itertools.combinations(d2.split('\n'), 2):
        diff_count = 0
        for i in range(0, len(w1)):
            if w1[i] != w2[i]:
                diff_count += 1
            if diff_count > 1:
                continue
        if diff_count == 1:
            results.append((w1,w2))
    return results


print(day2_p2())








