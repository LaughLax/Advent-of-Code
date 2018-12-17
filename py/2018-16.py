class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        self.input_1, self.input_2 = self.input.split('\n\n\n\n')

        self.samples = tuple(map(OpSample, self.input_1.split('\n\n')))

        self.commands = [list(map(int, line.split())) for line in self.input_2.splitlines()]

        self.proc = Processor()
        
        self.ops = [
            self.proc.addr,
            self.proc.addi,
            self.proc.mulr,
            self.proc.muli,
            self.proc.banr,
            self.proc.bani,
            self.proc.borr,
            self.proc.bori,
            self.proc.setr,
            self.proc.seti,
            self.proc.gtir,
            self.proc.gtri,
            self.proc.gtrr,
            self.proc.eqir,
            self.proc.eqri,
            self.proc.eqrr,
            ]

    def part1(self):
        three_or_more = 0
        for sample in self.samples:

            count = 0
            for op in self.ops:
                self.proc.r = sample.reg_before[:]
                op(sample.op_vals)
                if self.proc.r == sample.reg_after:
                    count += 1
                    
            if count >= 3:
                three_or_more += 1

        return three_or_more
    
    def part2(self):
        opcodes = [[op for op in self.ops] for i in range(16)]
        
        for sample in self.samples:
            if len(opcodes[sample.opcode]) > 1:
                for op in opcodes[sample.opcode][:]:
                    self.proc.r = sample.reg_before[:]
                    op(sample.op_vals)
                    if self.proc.r != sample.reg_after:
                        opcodes[sample.opcode].remove(op)

        reduced = True          
        while reduced:
            reduced = False
            for i0 in range(len(opcodes)):
                if len(opcodes[i0]) == 1:
                    op = opcodes[i0][0]
                    for i1 in range(len(opcodes)):
                        if i0 == i1:
                            continue
                        if op in opcodes[i1]:
                            opcodes[i1].remove(op)
                            reduced = True

        self.proc.r = [0, 0, 0, 0]
        for comm in self.commands:
            opcodes[comm[0]][0](comm[1:])
        
        return self.proc.r[0]


class Processor:

    def __init__(self):
        self.r = [0]*4
        pass
    
    def addr(self, i):
        self.r[i[2]] = self.r[i[0]] + self.r[i[1]]

    def addi(self, i):
        self.r[i[2]] = self.r[i[0]] + i[1]

    def mulr(self, i):
        self.r[i[2]] = self.r[i[0]] * self.r[i[1]]

    def muli(self, i):
        self.r[i[2]] = self.r[i[0]] * i[1]

    def banr(self, i):
        self.r[i[2]] = self.r[i[0]] & self.r[i[1]]

    def bani(self, i):
        self.r[i[2]] = self.r[i[0]] & i[1]

    def borr(self, i):
        self.r[i[2]] = self.r[i[0]] | self.r[i[1]]

    def bori(self, i):
        self.r[i[2]] = self.r[i[0]] | i[1]

    def setr(self, i):
        self.r[i[2]] = self.r[i[0]]

    def seti(self, i):
        self.r[i[2]] = i[0]

    def gtir(self, i):
        self.r[i[2]] = 1 if i[0] > self.r[i[1]] else 0

    def gtri(self, i):
        self.r[i[2]] = 1 if self.r[i[0]] > i[1] else 0

    def gtrr(self, i):
        self.r[i[2]] = 1 if self.r[i[0]] > self.r[i[1]] else 0

    def eqir(self, i):
        self.r[i[2]] = 1 if i[0] == self.r[i[1]] else 0

    def eqri(self, i):
        self.r[i[2]] = 1 if self.r[i[0]] == i[1] else 0

    def eqrr(self, i):
        self.r[i[2]] = 1 if self.r[i[0]] == self.r[i[1]] else 0


class OpSample:

    def __init__(self, input_str):
        lines = input_str.splitlines()
        line2 = lines[1].split()

        self.reg_before = [int(lines[0][9]), int(lines[0][12]), int(lines[0][15]), int(lines[0][18])]
        self.opcode = int(line2[0])
        self.op_vals = (int(line2[1]), int(line2[2]), int(line2[3]))
        self.reg_after = [int(lines[2][9]), int(lines[2][12]), int(lines[2][15]), int(lines[2][18])]



                                                          
