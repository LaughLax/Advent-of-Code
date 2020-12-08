class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.code = [line.split(' ') for line in self.input]
        self.code = [(i[0], int(i[1])) for i in self.code]

    def part1(self):
        ptr = 0
        acc = 0
        seen = set()
        while ptr not in seen:
            seen.add(ptr)
            if self.code[ptr][0] == 'acc':
                acc += self.code[ptr][1]
                ptr += 1
            elif self.code[ptr][0] == 'jmp':
                ptr += self.code[ptr][1]
            elif self.code[ptr][0] == 'nop':
                ptr += 1
        return acc

    def part2(self):
        ptr = 0
        acc = 0
        seen = set()
        while ptr not in seen:
            if self.code[ptr][0] == 'acc':
                acc += self.code[ptr][1]
                ptr += 1
            elif self.code[ptr][0] == 'jmp':
                seen.add(ptr)
                if ptr >= 619:
                    ptr += 1
                else:
                    ptr += self.code[ptr][1]
            elif self.code[ptr][0] == 'nop':
                seen.add(ptr)
                if ptr + self.code[ptr][1] >= 620:
                    ptr += self.code[ptr][1]
                else:
                    ptr += 1

        for line in seen:
            preserve = self.code[line]
            if preserve[0] == 'nop':
                self.code[line] = ('jmp', preserve[1])
            else:
                self.code[line] = ('nop', preserve[1])

            new_seen = set()
            ptr = 0
            acc = 0
            while ptr not in new_seen:
                if ptr == 625:
                    return acc
                new_seen.add(ptr)
                if self.code[ptr][0] == 'acc':
                    acc += self.code[ptr][1]
                    ptr += 1
                elif self.code[ptr][0] == 'jmp':
                    ptr += self.code[ptr][1]
                elif self.code[ptr][0] == 'nop':
                    ptr += 1

            self.code[line] = preserve
