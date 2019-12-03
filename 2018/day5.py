from collections import defaultdict

from utils import challenge_data

original_data = list(challenge_data(5))


def p1(data):
    stack = [data[0]]
    for b in data[1:]:
        try:
            a = stack.pop()
        except IndexError:
            stack.append(b)
            continue
        if a.lower() == b.lower() and a != b:
            continue# discard both
        stack.append(a)
        stack.append(b)
    return stack


p1_result = p1(original_data)
print(''.join(p1_result))
print(len(p1_result))


def p2():
    stats = []
    data = challenge_data(5)
    unique_elements = set(data.lower())
    for el in unique_elements:
        new_data = data.replace(el, '').replace(el.upper(), '')
        result = p1(list(new_data))

        stats.append((el, len(result)))

    return sorted(stats, key=lambda x: x[1])[0]


print(p2())






