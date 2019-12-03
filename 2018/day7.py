from utils import challenge_data
from parse import parse

data = challenge_data(7)

def process(data):
    data=data.split('\n')
    dependencies = {}
    for line in data:
        requirement, element = parse('Step {} must be finished before step {} can begin.', line)
        if dependencies.get(element, None) == None:
            dependencies[element] = []
        dependencies[element] += requirement

        dependencies[requirement] = dependencies.get(requirement, [])

    return dependencies


def p1(dependencies):
    left = list(set([d[0] for d in dependencies]))
    done = []

    while True:
        all_left = sorted([d for d in left if set(dependencies[d]).issubset(done)])
        element = next(iter(all_left))
        yield element
        left.remove(element)
        done.append(element)

        if not left:
            break


def p2(dependencies, workers=2, offset=0):
    seconds = 0

    left = list(set([d[0] for d in dependencies]))
    done = []
    worker_current_task = {}
    end = False

    while True:
        for w in range(0, workers):
            all_left = sorted([d for d in left if set(dependencies[d]).issubset(done)])
            element = next(iter(all_left), None)
            if element and worker_current_task.get(w) is None:
                left.remove(element)
                worker_current_task[w] = [element, ord(element.lower()) - ord('a') + offset]

        y = [seconds]
        for w in range(0, workers):
            y.append(worker_current_task.get(w, ('.',))[0])
        y.append(''.join(done))
        yield y

        if end:
            break

        for w in range(0, workers):
            if worker_current_task.get(w):
                if worker_current_task[w][1] == 0:
                    done.append(worker_current_task[w][0])
                    del worker_current_task[w]
                else:
                    worker_current_task[w][1] -= 1

        if not left and not worker_current_task:
            end = True
        seconds += 1




# print(''.join(p1(process(data))))
# print('\nall done')


print(list(iter(p2(process(data), workers=5, offset=60)))[-1])
print('\nall done')