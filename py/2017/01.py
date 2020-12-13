class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = list(map(int, [char for char in f.read().strip()]))

    def part1(self):
        sum = 0
        for i, v in enumerate(self.input):
            if v == self.input[i-1]:
                sum = sum + v

        return sum

    def part2(self):
        sum = 0
        rot = int(len(self.input) / 2)
        for i, v in enumerate(self.input):
            if v == self.input[i-rot]:
                sum = sum + v

        return sum
