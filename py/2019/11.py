import numpy as np
import matplotlib.pyplot as plt

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

        self.auto_inputs = None
        self.outputs = []

        self.cmd_count = 0
        self.halted = False

    def get_addr(self, addr):
        if addr >= len(self.state) - 1:
            return 0
        return self.state[addr]

    def set_addr(self, addr, val):
        while addr >= len(self.state) - 1:
            self.state.append(0)
        self.state[addr] = val

    def run_op(self):
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

    def run_until_output_or_halt(self):
        outs = len(self.outputs)
        while len(self.outputs) == outs and not self.halted:
            self.run_op()

    def reset_state(self):
        self.state = self.init_cond.copy()

        self.pos = 0
        self.input_pos = 0
        self.relative_base = 0

        self.auto_inputs = None
        self.outputs = []

        self.cmd_count = 0
        self.halted = False


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))

    def part1(self):
        pos = (0, 0)
        painted = {}
        dir = 0
        brain = IntCode('brain', self.init_cond)
        brain.auto_inputs = [0]
        while not brain.halted:
            brain.run_until_output_or_halt()
            if not brain.halted:
                paint = brain.outputs[-1]
                painted[pos] = paint
            brain.run_until_output_or_halt()
            if not brain.halted:
                turn = brain.outputs[-1]
                if turn == 0:
                    dir = ((dir + 4) - 1) % 4
                elif turn == 1:
                    dir = (dir + 1) % 4

                if dir == 0:
                    pos = (pos[0], pos[1] + 1)
                elif dir == 1:
                    pos = (pos[0] + 1, pos[1])
                elif dir == 2:
                    pos = (pos[0], pos[1] - 1)
                elif dir == 3:
                    pos = (pos[0] - 1, pos[1])

            if pos in painted:
                brain.auto_inputs.append(painted[pos])
            else:
                brain.auto_inputs.append(0)

        return len(painted)

    def part2(self):
        pos = (0, 0)
        painted = {}
        dir = 0
        brain = IntCode('brain', self.init_cond)
        brain.auto_inputs = [1]
        while not brain.halted:
            brain.run_until_output_or_halt()
            if not brain.halted:
                paint = brain.outputs[-1]
                painted[pos] = paint
            brain.run_until_output_or_halt()
            if not brain.halted:
                turn = brain.outputs[-1]
                if turn == 0:
                    dir = ((dir + 4) - 1) % 4
                elif turn == 1:
                    dir = (dir + 1) % 4

                if dir == 0:
                    pos = (pos[0], pos[1] + 1)
                elif dir == 1:
                    pos = (pos[0] + 1, pos[1])
                elif dir == 2:
                    pos = (pos[0], pos[1] - 1)
                elif dir == 3:
                    pos = (pos[0] - 1, pos[1])

            if pos in painted:
                brain.auto_inputs.append(painted[pos])
            else:
                brain.auto_inputs.append(0)

        min_x = 1e10
        max_x = -1e10
        min_y = 1e10
        max_y = -1e10
        for p in painted:
            min_x = p[0] if p[0] < min_x else min_x
            max_x = p[0] if p[0] > max_x else max_x
            min_y = p[1] if p[1] < min_y else min_y
            max_y = p[1] if p[1] > max_y else max_y

        arr = np.zeros((max_y - min_y + 1, max_x - min_x + 1))
        for p in painted:
            arr[p[1] - min_y][p[0] - min_x] = painted[p]

        plt.imshow(arr, origin='lower')
        # plt.show()

        return 0
