from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Any, Dict
from dijkstar import Graph, find_path

from utils import challenge_data
d6 = challenge_data(6)


@dataclass()
class Node:
    name: str = ''
    orbits_around: Any = None
    is_orbited_by: List[Any] = field(default_factory=list)


def parse(instructions) -> Dict[str, Node]:
    node_by_name = defaultdict(lambda : Node())
    for instruction in instructions:
        f, to = instruction.split(')')
        node_by_name[f].name = f
        node_by_name[f].is_orbited_by.append(to)
        node_by_name[to].orbits_around = f
    return node_by_name


def calculate_node_orbit(node, node_by_name):
    direct, indirect = 0, 0
    if node.orbits_around:
        direct += 1

        recchild = node_by_name[node.orbits_around]
        while recchild:
            if recchild.orbits_around:
                recchild = node_by_name[recchild.orbits_around]
                indirect += 1
            else:
                recchild = None

    return direct, indirect


def calculate_orbit(nodes_by_name):
    direct = 0
    indirect = 0
    for k, node in nodes_by_name.items():
        calc =  calculate_node_orbit(node, nodes_by_name)
        direct += calc[0]
        indirect += calc[1]

    return direct, indirect


def part1(d):
    nodes = parse(d)
    direct,indirect = calculate_orbit(nodes)
    print(f'd={direct}, ind={indirect}')
    print(f'total={direct+indirect}')


def parse_edge(instructions) -> Graph:
    graph = Graph()
    for instruction in instructions:
        f, to = instruction.split(')')
        graph.add_edge(to, f, 1)
        graph.add_edge(f, to, 1)
    return graph


def to_dikjstra(f,to, graph):
    path =  find_path(graph, f , to)
    print(path)
    return path.total_cost - 2


def part2(d):
    edges = parse_edge(d)
    print(to_dikjstra('YOU', 'SAN', edges))


if __name__ == '__main__':
    print(part1(d6.split('\n')))
    print(part2(d6.split('\n')))
