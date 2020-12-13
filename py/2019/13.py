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


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))
        self.machine = IntCode('arcade', self.init_cond)

    def part1(self):
        self.machine.reset_state()
        self.machine.run_until_halt()
        stuff = np.array(self.machine.outputs)
        stuff = stuff.reshape((int(len(stuff)/3), 3))
        count = 0
        for x in stuff[:, 2]:
            if x == 2:
                count += 1

        return count

    def part2(self):
        self.machine.reset_state()
        self.machine.state[0] = 2

        bricks = set()
        score = 0
        ball_x = 0
        paddle_x = 0

        while True:
            self.machine.run_until_input_or_halt()

            while len(self.machine.outputs) > 0:
                x, y, z = self.machine.outputs[0:3]
                self.machine.outputs = self.machine.outputs[3:]

                if x < 0:
                    score = z
                elif z == 2:
                    bricks.add((x, y))
                elif z == 3:
                    paddle_x = x
                elif z == 4:
                    ball_x = x

                if (x, y) in bricks and z != 2:
                    bricks.remove((x, y))

            if len(bricks) > 0:
                if ball_x < paddle_x:
                    self.machine.add_input(-1)
                elif ball_x > paddle_x:
                    self.machine.add_input(1)
                else:
                    self.machine.add_input(0)
            else:
                return score
