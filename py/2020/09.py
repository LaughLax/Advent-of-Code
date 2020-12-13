import numpy as np


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.input = [int(line) for line in self.input]

    def sum_exists(self, arr, target):
        for i in range(len(arr)):
            num_i = arr[i]
            for j in range(i+1, len(arr)):
                num_j = arr[j]

                if num_i + num_j == target:
                    return num_i * num_j

                elif num_i + num_j > target:
                    continue
        pass

    def part1(self):
        for i, val in enumerate(self.input):
            if i < 25:
                continue

            if not self.sum_exists(list(self.input[i-25:i]), val):
                return val

    def part2(self):
        val = 85848519
        acc = np.cumsum(self.input)
        for length in range(2, len(acc)):
            for i in range(len(acc)-length):
                if acc[i+length] - acc[i] == val:
                    return np.min(self.input[i:i+length]) + np.max(self.input[i:i+length])
