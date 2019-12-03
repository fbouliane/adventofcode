from unittest import TestCase
from day2 import step, Context, run_until


class Day2(TestCase):
    def test_step(self):
        c = Context(program=[1,4,5,6,1,2,0], ptr=0)
        c2 = step(c)
        self.assertEqual(3, c2.program[6])

    def test_given(self):
        c = Context(program=[1,0,0,0,99], ptr=0)
        c = run_until(c)
        self.assertEqual([2,0,0,0,99], c.program)

        c = Context(program=[2,3,0,3,99], ptr=0)
        c = run_until(c)
        self.assertEqual([2,3,0,6,99], c.program)

        c = Context(program=[2,4,4,5,99,0], ptr=0)
        c = run_until(c)
        self.assertEqual([2,4,4,5,99,9801], c.program)

        c = Context(program=[1,1,1,4,99,5,6,0,99], ptr=0)
        c = run_until(c)
        self.assertEqual([30,1,1,4,2,5,6,0,99], c.program)
