class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            self.init_cond = list(map(int, self.input.split(',')))
        self.state = self.init_cond.copy()

    def run_op(self, position):
        op = self.state[position]
        addr_1 = self.state[position + 1]
        addr_2 = self.state[position + 2]
        target_addr = self.state[position + 3]

        if op == 1:
            self.state[target_addr] = self.state[addr_1] + self.state[addr_2]
        elif op == 2:
            self.state[target_addr] = self.state[addr_1] * self.state[addr_2]
        elif op == 99:
            return False

        return True

    def part1(self):
        self.state = self.init_cond.copy()
        self.state[1] = 12
        self.state[2] = 2

        run = True
        pos = 0
        while run:
            run = self.run_op(pos)
            pos += 4

        return self.state[0]

    def part2(self):
        for i in range(100):
            for j in range(100):
                self.state = self.init_cond.copy()
                self.state[1] = i
                self.state[2] = j

                run = True
                pos = 0
                while run:
                    run = self.run_op(pos)
                    pos += 4

                if self.state[0] == 19690720:
                    return i*100 + j

        return False
