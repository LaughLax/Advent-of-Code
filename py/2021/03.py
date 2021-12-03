import numpy as np
import pandas as pd


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
        df = pd.DataFrame(self.bits, columns=range(self.num_size))

        # Oxygen
        oxy = df.copy()
        for i in range(self.num_size):
            want = oxy[i].sum() >= len(oxy) / 2
            oxy = oxy[oxy[i] == want]
            if len(oxy) == 1:
                break
        oxygen = np.sum(oxy[i].iloc[0] * (1 << (self.num_size - i - 1)) for i in range(self.num_size))

        # CO2
        co = df.copy()
        for i in range(self.num_size):
            want = co[i].sum() < len(co) / 2
            co = co[co[i] == want]
            if len(co) == 1:
                break
        co2 = np.sum(co[i].iloc[0] * (1 << (self.num_size - i - 1)) for i in range(self.num_size))

        return oxygen * co2
