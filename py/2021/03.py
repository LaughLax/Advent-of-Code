import numpy as np


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
            self.num_size = len(self.input[0])
            self.bits = [[i == '1' for i in line] for line in self.input]

    def part1(self):
        ct = np.sum(self.bits, axis=0) >= len(self.input)/2
        gamma = eps = 0
        for i, val in enumerate(ct):
            gamma += val * (1 << (self.num_size-i-1))
            eps += (not val) * (1 << (self.num_size-i-1))
        return gamma * eps

    def part2(self):
        # Oxygen
        bits_oxy = self.bits.copy()
        for i in range(self.num_size):
            bits_copy = bits_oxy.copy()
            want = np.sum(np.array(bits_copy)[:, i]) >= len(bits_copy)/2
            for row in bits_oxy:
                if row[i] != want:
                    bits_copy.remove(row)
            if len(bits_copy) == 1:
                break
            bits_oxy = bits_copy
        oxygen = np.sum([val * (1 << (self.num_size-i-1)) for i, val in enumerate(bits_copy.pop())])

        # CO2
        bits_co2 = self.bits.copy()
        for i in range(self.num_size):
            bits_copy = bits_co2.copy()
            want = np.sum(np.array(bits_copy)[:, i]) < len(bits_copy)/2
            for row in bits_co2:
                if row[i] != want:
                    bits_copy.remove(row)
            if len(bits_copy) == 1:
                break
            bits_co2 = bits_copy
        co2 = np.sum([val * (1 << (self.num_size-i-1)) for i, val in enumerate(bits_copy.pop())])

        return oxygen * co2
