from unittest import TestCase

from day7 import amplifier, total_output
from day8 import split_layers, count_layer, flatten_layer


class Day7Test(TestCase):
    def test_1(self):
        input = '123456789012'
        layers = split_layers(list(input), 3, 2)
        self.assertEqual(list('123456'), layers[0])
        self.assertEqual(list('789012'), layers[1])

    def test_count_layer(self):
        layer = '122333'
        self.assertEqual(1, count_layer(layer, '1'))
        self.assertEqual(2, count_layer(layer, '2'))
        self.assertEqual(3, count_layer(layer, '3'))

    def test_flatten(self):
        l1 = '0222'
        l2 = '1122'
        l3 = '2212'
        l4 = '0000'

        image = flatten_layer([l1, l2, l3, l4], 2, 2)

        self.assertEqual(list('0110'), image)
