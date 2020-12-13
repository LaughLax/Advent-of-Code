import operator

op_dict = {
    '==': operator.eq,
    '!=': operator.ne,
    '>':  operator.gt,
    '>=': operator.ge,
    '<':  operator.lt,
    '<=': operator.le,
}


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.ops = list(map(InputLine, self.input))

        self.registers = {}

        self.peak_value = 0

    def part1(self):
        for line in self.ops:
            reg = self.registers.setdefault(line.reg, 0)
            if line.op(self.registers.setdefault(line.check_reg, 0), line.check_val):
                self.registers[line.reg] = reg + line.add

        return max(self.registers.values())

    def part2(self):
        if len(self.registers) > 0:
            self.registers = {}
        for line in self.ops:
            reg = self.registers.setdefault(line.reg, 0)
            if line.op(self.registers.setdefault(line.check_reg, 0), line.check_val):
                self.registers[line.reg] = reg + line.add
                if reg + line.add > self.peak_value:
                    self.peak_value = reg + line.add

        return self.peak_value


class InputLine:

    def __init__(self, line):
        self.line = line.split()
        self.reg = self.line[0]
        self.add = int(self.line[2]) if self.line[1] == 'inc' else -int(self.line[2])
        self.check_reg = self.line[4]
        self.op = op_dict.get(self.line[5])
        self.check_val = int(self.line[6])
