import numpy as np


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = np.array(list(map(int, f.read().split(','))))

    def part1(self):
        fish = self.input.copy()
        for day in range(80):
            new = np.sum(fish == 0)
            fish = np.append(fish, [9]*new)
            fish += (7 * (fish == 0)) - 1
        return len(fish)

    def part2(self):
        fish = {}
        for i in range(9):
            fish[i] = np.sum(self.input == i, dtype=np.ulonglong)
        for _ in range(256):
            new = fish[0]
            for i in range(8):
                fish[i] = fish[i+1]
            fish[6] += new
            fish[8] = new
        return np.sum([fish[i] for i in range(9)])
