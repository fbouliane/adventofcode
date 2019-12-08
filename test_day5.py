from unittest import TestCase
from day5 import step, Context, run_until, get_mode, reforvaloffset, Operations


class Day5(TestCase):
    def test_step(self):
        c = Context(program=[1,4,5,6,1,2,0], ptr=0)
        step(c)
        self.assertEqual(3, c.program[6])

    def test_day2(self):
        c = Context(program=[1,0,0,0,99], ptr=0)
        run_until(c)
        self.assertEqual([2,0,0,0,99], c.program)

        c = Context(program=[2,3,0,3,99], ptr=0)
        run_until(c)
        self.assertEqual([2,3,0,6,99], c.program)

        c = Context(program=[2,4,4,5,99,0], ptr=0)
        run_until(c)
        self.assertEqual([2,4,4,5,99,9801], c.program)

        c = Context(program=[1,1,1,4,99,5,6,0,99], ptr=0)
        run_until(c)
        self.assertEqual([30,1,1,4,2,5,6,0,99], c.program)

    def test_output_instruction(self):
        c = Context(program=list(map(int, '4,0'.split(','))), ptr=0)
        step(c)
        self.assertEqual(4, c.outputs[0])

    def test_input_instruction(self):
        c2 = Context(program=list(map(int, '3,2,0'.split(','))), ptr=0)
        c2.inputs = [5]
        step(c2)
        self.assertEqual(5, c2.program[2])

    def test_store_load_instructions_changed_next_instructions(self):
        c = Context(program=list(map(int, '1,0,0,0'.split(','))), ptr=0)
        c.next = 4
        step(c)
        self.assertEqual(c.next, 4)

        c = Context(program=list(map(int, '4,0'.split(','))), ptr=0)
        c.next = 4
        step(c)
        self.assertEqual(c.next, 2)

    def test_get_mode(self):
        self.assertEqual('010', get_mode(1002))
        self.assertEqual('000', get_mode(2))
        self.assertEqual('001', get_mode(10002))

    def test_instruction_with_modes(self):
        c = Context(program=list(map(int, '1002,4,3,4,33'.split(','))), ptr=0)
        step(c)
        self.assertEqual([1002,4,3,4,99], c.program)

    def test_ret_or_val_offset(self):
        c = Context(program=list(map(int, '1002,4,3,4,33'.split(','))), ptr=0)

        self.assertEqual(33,reforvaloffset(ptr=c.ptr, offset=0, modes='010', program=c.program))
        self.assertEqual(3,reforvaloffset(ptr=c.ptr, offset=1, modes='010', program=c.program))
        self.assertEqual(4,reforvaloffset(ptr=c.ptr, offset=2, modes='111', program=c.program))

    def test_part2_jumps(self):
        c = Context(program=[Operations.JUMPIFTRUE.value, 0], ptr=0)
        step(c)
        self.assertEqual(3, c.next)

        c = Context(program=[Operations.JUMPIFTRUE.value, 1, 1], ptr=0)
        step(c)
        self.assertEqual(1, c.next)

        c = Context(program=[Operations.JUMPIFFALSE.value, 1], ptr=0)
        step(c)
        self.assertEqual(3, c.next)

        c = Context(program=[Operations.JUMPIFFALSE.value, 0, 1], ptr=0)
        step(c)
        self.assertEqual(0, c.next)

    def test_part2_lessthan(self):
        c = Context(program=[11100 + Operations.LESSTHAN.value, 1, 5, 4, 0], ptr=0)
        step(c)
        self.assertEqual(1, c.program[4])

        c = Context(program=[11100 + Operations.LESSTHAN.value, 5, 1, 4, 1], ptr=0)
        step(c)
        self.assertEqual(0, c.program[4])

    def test_part2_equals(self):
        c = Context(program=[11100 + Operations.EQUALS.value, 5, 5, 4, 0], ptr=0)
        step(c)
        self.assertEqual(1, c.program[4])

        c = Context(program=[11100 + Operations.EQUALS.value, 5, 4, 4, 1], ptr=0)
        step(c)
        self.assertEqual(0, c.program[4])

    def _program_with_input(self, program, input):
        c = Context(program=list(program), ptr=0)
        c.inputs = [input]
        run_until(c)
        return c.outputs

    def test_part2_example(self):
        p_position_equal = [3,9,8,9,10,9,4,9,99,-1,8]
        self.assertEqual([1], self._program_with_input(p_position_equal, 8))
        self.assertEqual([0], self._program_with_input(p_position_equal, 7))

        p_position_lt= [3,9,7,9,10,9,4,9,99,-1,8]
        self.assertEqual([1], self._program_with_input(p_position_lt, 6))
        self.assertEqual([0], self._program_with_input(p_position_lt, 9))

        p_imm_eq = [3,3,1108,-1,8,3,4,3,99]
        self.assertEqual([1], self._program_with_input(p_imm_eq, 8))
        self.assertEqual([0], self._program_with_input(p_imm_eq, 7))

        p_imm_lt = [3,3,1107,-1,8,3,4,3,99]
        self.assertEqual([1], self._program_with_input(p_imm_lt, 6))
        self.assertEqual([0], self._program_with_input(p_imm_lt, 9))

    def test_part2_example_jumps(self):
        jump_position = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.assertEqual([0], self._program_with_input(jump_position, 0))
        self.assertEqual([1], self._program_with_input(jump_position, 55))

        jump_immediate = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        self.assertEqual([0], self._program_with_input(jump_immediate, 0))
        self.assertEqual([1], self._program_with_input(jump_immediate, 55))

    def test_part2_larger(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                   1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                   999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.assertEqual([999], self._program_with_input(program, 7))
        self.assertEqual([1000], self._program_with_input(program, 8))
        self.assertEqual([1001], self._program_with_input(program, 9))


