class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
            self.input = list(map(int, self.input))

    def part1(self):
        incr = 0
        for i in range(len(self.input)-1):
            if self.input[i+1] > self.input[i]:
                incr += 1

        return incr

    def part2(self):
        incr = 0
        for i in range(len(self.input)-3):
            if self.input[i+3] > self.input[i]:
                incr += 1

        return incr
