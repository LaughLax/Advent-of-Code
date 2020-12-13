class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.proc = Processor()

        commands = []
        for line in self.input:
            if line.startswith('#ip'):
                self.proc.instr_reg = int(line[4])
            else:
                commands.append(Command(self.proc, line))

    def part1(self):
        pass
    
    def part2(self):
        pass


class Processor:

    def __init__(self):
        self.r = [0]*6
        self.instr_reg = -1

        self.ops = {
            'addr': self.proc.addr,
            'addi': self.proc.addi,
            'mulr': self.proc.mulr,
            'muli': self.proc.muli,
            'banr': self.proc.banr,
            'bani': self.proc.bani,
            'borr': self.proc.borr,
            'bori': self.proc.bori,
            'setr': self.proc.setr,
            'seti': self.proc.seti,
            'gtir': self.proc.gtir,
            'gtri': self.proc.gtri,
            'gtrr': self.proc.gtrr,
            'eqir': self.proc.eqir,
            'eqri': self.proc.eqri,
            'eqrr': self.proc.eqrr,
            }
    
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


class Command:

    def __init__(self, processor, input_str):

        split = input_str.split()

        oper = processor.ops[split[0]]
        nums = list(map(int, split[1:]))



                                                          
