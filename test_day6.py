from unittest import TestCase

from day6 import parse, calculate_orbit, calculate_node_orbit, parse_edge, to_dikjstra


class Day6Test(TestCase):
    def test_parse(self):
        instructions = ['A)B', 'B)C']
        result = parse(instructions)

        self.assertEqual('A', result['A'].name)
        self.assertEqual(None, result['A'].orbits_around)
        self.assertEqual(['B'], result['A'].is_orbited_by)

        self.assertEqual('B', result['B'].name)
        self.assertEqual('A', result['B'].orbits_around)

    def test_calculate_orbits(self):
        instructions = ['A)B', 'B)C']
        d = parse(instructions)
        d, ind = calculate_orbit(d)

        self.assertEqual(d, 2)
        self.assertEqual(ind, 1)

    def test_shown_specific_node(self):
        instructions = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', "K)L"]
        d = parse(instructions)
        d, ind = calculate_node_orbit(d['L'], d)
        self.assertEqual(1, d)
        self.assertEqual(6, ind)
        self.assertEqual(d + ind, 7)

    def test_shown(self):
        instructions = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', "K)L"]
        d = parse(instructions)
        d, ind = calculate_orbit(d)

        self.assertEqual(d + ind, 42)

    def test_dikjstra(self):
        instructions = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', "K)L", 'K)YOU', 'I)SAN']
        edges = parse_edge(instructions)
        print(edges)
        self.assertEqual(4, to_dikjstra('YOU', 'SAN', edges))





