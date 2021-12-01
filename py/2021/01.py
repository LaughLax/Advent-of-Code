import numpy as np


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
        d3 = []
        for i in range(len(self.input)-2):
            d3.append(self.input[i] + self.input[i+1] + self.input[i+2])

        incr = 0
        for i in range(len(d3)-1):
            if d3[i+1] > d3[i]:
                incr += 1

        return incr
