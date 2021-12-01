from collections import Counter
from dataclasses import dataclass
from enum import Enum
from PIL import Image

from utils import challenge_data
d8 = challenge_data(8)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class Color(Enum):
    black = 0
    white = 1
    transparent = 2


def split_layers(input, image_width, image_height):
    layers = []
    for layer in chunks(input, image_width * image_height):
        layers.append(layer)
    return layers


def count_layer(layer, pixel):
    c = Counter(list(layer))
    return c.get(pixel)


def part1(image):
    width = 25
    height = 6
    layers = split_layers(image, width, height)
    layer_zeros = {}
    for i, layer in enumerate(layers):
        layer_zeros[count_layer(layer, '0')] = i
    min_value = min(layer_zeros.keys())
    min_layer = layers[layer_zeros[min_value]]
    ones, twos = count_layer(min_layer, '1'), count_layer(min_layer, '2')
    print(f'1={ones},2={twos}, t = {ones*twos}')
    return ones * twos


def flatten_layer(layers, width, height):
    image = [2 for i in range(0, width * height)]
    for i in range(0, width * height):
        for layer in layers:
            if int(layer[i]) != Color.transparent.value:
                image[i] = layer[i]
                break
    return image


def format_image(image, width, height):
    for h in range(0, height):
        for w in range(0, width):
            print(image[w + (h*w)], end='')
        print('')


def to_png(image, width, height):
    im= Image.new('RGB', (width, height))
    color = {
        Color.black.value: (255,255,255),
        Color.white.value: (0,0,0)
    }
    im.putdata([color[int(p)] for p in image])
    im.save('day8.png')


def part2(image):
    width = 25
    height = 6
    layers = split_layers(image, width, height)
    image = flatten_layer(layers, width, height)
    format_image(image, width, height)
    to_png(image, width, height)


if __name__ == '__main__':
    print(part1(d8))
    part2(d8)

