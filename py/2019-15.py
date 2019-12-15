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


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))
        self.machine = IntCode('repair', self.init_cond)
        self.dir_map_for_bot = {
            0: 1,
            1: 4,
            2: 2,
            3: 3
        }
        self.dir_map_for_me = {
            0: (0, -1),
            1: (1, 0),
            2: (0, 1),
            3: (-1, 0)
        }

        self.grid = None

    def print_grid(self, grid):
        min_x = 100000
        min_y = 100000
        max_x = -100000
        max_y = -100000
        for key in grid:
            min_x = key[0] if key[0] < min_x else min_x
            min_y = key[1] if key[1] < min_y else min_y
            max_x = key[0] if key[0] > max_x else max_x
            max_y = key[1] if key[1] > max_y else max_y

        print(min_x)
        print(min_y)
        print(max_x)
        print(max_y)

        chars = []
        for y in range(min_y, max_y + 1):
            this_row = []
            for x in range(min_x, max_x + 1):
                if x == 0 and y == 0:
                    this_row.append('S')
                elif (x, y) not in grid:
                    this_row.append(' ')
                elif grid[(x, y)] == 0:
                    this_row.append('#')
                elif grid[(x, y)] == 1:
                    this_row.append('.')
                elif grid[(x, y)] == 2:
                    this_row.append('o')
                else:
                    print('WHAT IS GOING ON')
            chars.append(this_row)
            print(''.join(this_row))

    def part1(self):
        grid = {(0, 0): 1}
        dir = 0
        my_dir = self.dir_map_for_me[dir]
        x = 0
        y = 0
        found_oxygen = False
        self.machine.run_until_io_or_halt()

        def consider_turning(dir):
            for dir_check in range(4):
                my_dir_check = self.dir_map_for_me[dir_check]
                if (x + my_dir_check[0], y + my_dir_check[1]) not in grid:
                    return dir_check
            return dir
        turns = 0
        while True:
            self.machine.add_input(self.dir_map_for_bot[dir])
            self.machine.run_until_input_or_halt()
            res = self.machine.outputs[-1]
            if res == 0:
                grid[(x + my_dir[0], y + my_dir[1])] = 0
                dir = (dir + 1) % 4
                my_dir = self.dir_map_for_me[dir]
            elif res == 1:
                x += my_dir[0]
                y += my_dir[1]
                grid[(x, y)] = 1
                dir = (dir - 1) % 4
                my_dir = self.dir_map_for_me[dir]
            elif res == 2:
                x += my_dir[0]
                y += my_dir[1]
                grid[(x, y)] = 2
                found_oxygen = True
                print((x, y))

            turns += 1
            if x == 0 and y == 0 and turns >= 10:
                break
        self.print_grid(grid)
        self.grid = grid

    def part2(self):
        non_oxy = set()
        oxy_to_spread = set()
        for key in self.grid:
            if self.grid[key] == 1:
                non_oxy.add(key)
            elif self.grid[key] == 2:
                oxy_to_spread.add(key)

        minutes = 0
        while len(non_oxy) > 0:
            for key in oxy_to_spread.copy():
                for x in [-1, 1]:
                    check = (key[0] + x, key[1])
                    if check in non_oxy:
                        non_oxy.remove(check)
                        oxy_to_spread.add(check)
                for y in [-1, 1]:
                    check = (key[0], key[1] + y)
                    if check in non_oxy:
                        non_oxy.remove(check)
                        oxy_to_spread.add(check)
                oxy_to_spread.remove(key)

            minutes += 1

        return minutes


