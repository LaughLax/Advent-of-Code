import numpy as np
import matplotlib.pyplot as plt
from time import sleep


class IntCode:

    def __init__(self, obj_id, init_state):
        self.id = obj_id
        self.init_cond = init_state
        self.state = self.init_cond.copy()

        self.op_param_count = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            9: 1,
            99: 0,
        }
        self.op_param_modal = {
            1: 2,
            2: 2,
            3: 0,
            4: 1,
            5: 2,
            6: 2,
            7: 2,
            8: 2,
            9: 1,
            99: 0,
        }

        self.pos = 0
        self.input_pos = 0
        self.relative_base = 0

        self.auto_inputs = []
        self.outputs = []

        self.cmd_count = 0
        self.halted = False
        self.awaiting_input = False
        self.input_op = None

    def get_addr(self, addr):
        if addr >= len(self.state):
            return 0
        return self.state[addr]

    def set_addr(self, addr, val):
        while addr >= len(self.state) - 1:
            self.state.append(0)
        self.state[addr] = val

    def run_op(self):
        if self.awaiting_input:
            return False

        full_op = self.state[self.pos]
        op = full_op % 100
        params = self.state[self.pos+1:self.pos+self.op_param_count[op]+1]
        for i in range(self.op_param_count[op]):
            mode = (full_op // [100, 1000, 10000][i]) % 10
            if i < self.op_param_modal[op]:
                if mode == 0:
                    params[i] = self.get_addr(params[i])
                elif mode == 2:
                    params[i] = self.get_addr(self.relative_base + params[i])
            elif mode == 2:
                params[i] = self.relative_base + params[i]

        self.cmd_count += 1

        if op == 1:
            self.set_addr(params[2], params[0] + params[1])
        elif op == 2:
            self.set_addr(params[2], params[0] * params[1])
        elif op == 3:
            if self.input_pos > len(self.auto_inputs) - 1:
                self.awaiting_input = True
                self.input_op = params[0]
                return False
            self.set_addr(params[0], self.auto_inputs[self.input_pos])
            self.input_pos += 1
        elif op == 4:
            self.outputs.append(params[0])
        elif op == 5:
            if params[0] != 0:
                self.pos = params[1] - 3
        elif op == 6:
            if params[0] == 0:
                self.pos = params[1] - 3
        elif op == 7:
            self.set_addr(params[2], 1 if params[0] < params[1] else 0)
        elif op == 8:
            self.set_addr(params[2], 1 if params[0] == params[1] else 0)
        elif op == 9:
            self.relative_base += params[0]
        elif op == 99:
            self.halted = True
            return False

        self.pos += self.op_param_count[op] + 1

        return True

    def add_input(self, input):
        self.auto_inputs.append(input)
        if self.awaiting_input:
            self.set_addr(self.input_op, self.auto_inputs[self.input_pos])
            self.input_pos += 1
            self.pos += 2
            self.awaiting_input = False
            self.input_op = None

    def run_until_input_or_halt(self):
        while not self.awaiting_input and not self.halted:
            self.run_op()

    def run_until_output_or_halt(self):
        outs = len(self.outputs)
        while len(self.outputs) == outs and not self.halted:
            self.run_op()

    def run_until_io_or_halt(self):
        outs = len(self.outputs)
        while len(self.outputs) == outs and not self.awaiting_input and not self.halted:
            self.run_op()

    def run_until_halt(self):
        while not self.halted:
            self.run_op()

    def reset_state(self):
        self.state = self.init_cond.copy()

        self.pos = 0
        self.input_pos = 0
        self.relative_base = 0

        self.auto_inputs = []
        self.outputs = []

        self.cmd_count = 0
        self.halted = False
        self.awaiting_input = False
        self.input_op = None


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))
        self.machine = IntCode('vacuum', self.init_cond)

        self.grid = None

    def part1(self):
        self.machine.reset_state()
        self.machine.run_until_halt()
        my_str = ''
        lines = []
        line = []
        for o in self.machine.outputs:
            my_str += chr(o)
            if chr(o) != '\n':
                line.append(chr(o))
            else:
                if len(line) > 0:
                    lines.append(line)
                    line = []

        # print(my_str)
        # print(lines)

        inters = []
        for y, line in enumerate(lines):
            # print(f'y: {y}')
            if y == 0 or y == len(lines) - 1:
                continue
            for x, ch in enumerate(line):
                # print(f'x: {x}')
                if x == 0 or x == len(line) - 1:
                    continue

                if lines[y][x] == '#' and \
                    lines[y-1][x] == '#' and \
                    lines[y+1][x] == '#' and \
                    lines[y][x-1] == '#' and \
                    lines[y][x+1] == '#':
                    inters.append((x, y))
                    # print((x, y))
                    lines[y][x] = 'O'

        # for line in lines:
        #     print(''.join(line))

        sum = 0
        for inter in inters:
            sum += inter[0] * inter[1]

        return sum

    def part2(self):
        self.machine.reset_state()
        self.machine.state[0] = 2

        mov_func = [ord(c) for c in 'A,B,A,C,A,C,B,C,C,B\n']
        mov_a = [ord(c) for c in 'L,4,L,4,L,10,R,4\n']
        mov_b = [ord(c) for c in 'R,4,L,4,L,4,R,8,R,10\n']
        mov_c = [ord(c) for c in 'R,4,L,10,R,10\n']

        self.machine.auto_inputs.extend(mov_func)
        self.machine.auto_inputs.extend(mov_a)
        self.machine.auto_inputs.extend(mov_b)
        self.machine.auto_inputs.extend(mov_c)
        self.machine.auto_inputs.extend([ord('n'), ord('\n')])

        self.machine.run_until_halt()
        # print(''.join(map(chr, self.machine.outputs)))

        return self.machine.outputs[-1]


