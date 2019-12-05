class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))
        self.state = self.init_cond.copy()

        self.ops = {
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
        self.param_mode = 0
        self.pos = 0
        self.auto_input = None
        self.outputs = []

    def run_op(self):
        full_op = self.state[self.pos]
        op = full_op % 100
        params = [self.state[self.pos+i+1] for i in range(self.ops[op])]

        if op == 1:
            p0 = params[0] if (full_op // 100) % 10 == 1 else self.state[params[0]]
            p1 = params[1] if (full_op // 1000) % 10 == 1 else self.state[params[1]]
            self.state[params[2]] = p0 + p1
        elif op == 2:
            p0 = params[0] if (full_op // 100) % 10 == 1 else self.state[params[0]]
            p1 = params[1] if (full_op // 1000) % 10 == 1 else self.state[params[1]]
            self.state[params[2]] = p0 * p1
        elif op == 3:
            # self.state[params[0]] = int(input('>'))
            self.state[params[0]] = self.auto_input
        elif op == 4:
            p0 = params[0] if (full_op // 100) % 10 == 1 else self.state[params[0]]
            # print(p0)
            self.outputs.append(p0)
        elif op == 5:
            p0 = params[0] if (full_op // 100) % 10 == 1 else self.state[params[0]]
            p1 = params[1] if (full_op // 1000) % 10 == 1 else self.state[params[1]]
            if p0 != 0:
                self.pos = p1 - 3
        elif op == 6:
            p0 = params[0] if (full_op // 100) % 10 == 1 else self.state[params[0]]
            p1 = params[1] if (full_op // 1000) % 10 == 1 else self.state[params[1]]
            if p0 == 0:
                self.pos = p1 - 3
        elif op == 7:
            p0 = params[0] if (full_op // 100) % 10 == 1 else self.state[params[0]]
            p1 = params[1] if (full_op // 1000) % 10 == 1 else self.state[params[1]]
            self.state[params[2]] = 1 if p0 < p1 else 0
        elif op == 8:
            p0 = params[0] if (full_op // 100) % 10 == 1 else self.state[params[0]]
            p1 = params[1] if (full_op // 1000) % 10 == 1 else self.state[params[1]]
            self.state[params[2]] = 1 if p0 == p1 else 0
        elif op == 99:
            return False

        self.pos += self.ops[op] + 1

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
