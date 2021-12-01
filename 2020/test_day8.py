from unittest import TestCase

from day8 import run
from utils import inline


class Day6Test(TestCase):
    def test_1(self):
        input = inline("""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""")

        run(input)
