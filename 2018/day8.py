from utils import challenge_data

class Node(object):
    def __init__(self, start, child_count, metadata_count):
        self.child_count = child_count
        self.metadata_count = metadata_count
        self.childs = []
        self.metadata = []
        self.start = start
        self.end = 0

    def value(self):
        if not self.childs:
            return sum(self.metadata)
        else:
            total = 0
            for metadata in self.metadata:
                if metadata == 0:
                    continue
                try:
                    total += self.childs[metadata-1].value()
                except IndexError:
                    pass
            return total

    def __repr__(self):
        return f"{self.child_count} {self.metadata_count}"

import sys
sys.setrecursionlimit(200000)


def next_node(data, index):
    n = Node(index, int(data[index]), int(data[index + 1]))
    current_offset = index + 1
    for child in range(0, n.child_count):
        current_offset += 1
        c = next_node(data, current_offset)
        n.childs.append(c)
        current_offset = c.end

    for metadata in range(0, n.metadata_count):
        current_offset += 1
        n.metadata.append(int(data[current_offset]))

    n.end = current_offset
    return n


def p1(data):
    c = next_node(data, 0)

    def add_metadata(el):
        total = sum(el.metadata)
        for c in el.childs:
            total += add_metadata(c)
        return total

    return add_metadata(c)


def p2(data):
    node = next_node(data, 0)

    return node.value()

print(p1(challenge_data(8).split(' ')))

print(p2(challenge_data(8).split(' ')))



