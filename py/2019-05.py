class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))
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
            99: 0,
        }
        self.param_mode = 0
        self.pos = 0
        self.auto_input = None
        self.outputs = []

    def run_op(self):
        full_op = self.state[self.pos]
        op = full_op % 100
        params = [self.state[self.pos+i+1] for i in range(self.op_param_count[op])]
        for i in range(self.op_param_modal[op]):
            params[i] = params[i] if (full_op // int(10**(i+2))) % 10 == 1 else self.state[params[i]]

        if op == 1:
            self.state[params[2]] = params[0] + params[1]
        elif op == 2:
            self.state[params[2]] = params[0] * params[1]
        elif op == 3:
            self.state[params[0]] = self.auto_input
        elif op == 4:
            self.outputs.append(params[0])
        elif op == 5:
            if params[0] != 0:
                self.pos = params[1] - 3
        elif op == 6:
            if params[0] == 0:
                self.pos = params[1] - 3
        elif op == 7:
            self.state[params[2]] = 1 if params[0] < params[1] else 0
        elif op == 8:
            self.state[params[2]] = 1 if params[0] == params[1] else 0
        elif op == 99:
            return False

        self.pos += self.op_param_count[op] + 1

        return True

    def part1(self):
        self.state = self.init_cond.copy()
        self.auto_input = 1

        run = True
        while run:
            run = self.run_op()

        return self.outputs[-1]

    def part2(self):
        self.state = self.init_cond.copy()
        self.pos = 0
        self.auto_input = 5

        run = True
        while run:
            run = self.run_op()

        return self.outputs[-1]
