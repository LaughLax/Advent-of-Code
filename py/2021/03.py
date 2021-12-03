import numpy as np


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
            # self.input = [int(i, base=2) for i in self.input]

    def part1(self):
        bits = [[int(i) for i in line] for line in self.input]
        bits = np.array(bits)
        ct = np.sum(bits, axis=0)
        gamma_bits = [str(int(c >= len(self.input)/2)) for c in ct]
        eps_bits = [str(1-int(c)) for c in gamma_bits]
        gamma = int(''.join(gamma_bits), base=2)
        eps = int(''.join(eps_bits), base=2)
        return gamma * eps

    def part2(self):
        bits = [[int(i) for i in line] for line in self.input]

        # Oxygen
        bits_oxy = bits.copy()
        for i in range(12):
            bits_copy = bits_oxy.copy()
            want = int(np.sum(bits_copy, axis=0)[i] >= len(bits_copy)/2)
            for row in bits_oxy:
                if row[i] != want:
                    bits_copy.remove(row)
                if len(bits_copy) == 1:
                    break
            if len(bits_copy) == 1:
                break
            bits_oxy = bits_copy
        oxygen = int(''.join([str(c) for c in bits_copy.pop()]), base=2)

        # CO2
        bits_co2 = bits.copy()
        for i in range(12):
            bits_copy = bits_co2.copy()
            want = int(np.sum(bits_copy, axis=0)[i] < len(bits_copy)/2)
            for row in bits_co2:
                if row[i] != want:
                    bits_copy.remove(row)
                if len(bits_copy) == 1:
                    break
            if len(bits_copy) == 1:
                break
            bits_co2 = bits_copy
        co2 = int(''.join([str(c) for c in bits_copy.pop()]), base=2)

        return oxygen * co2
