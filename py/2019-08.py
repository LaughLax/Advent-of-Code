import numpy as np
import matplotlib.pyplot as plt


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().strip()

        self.input_ints = list(map(int,[char for char in self.input]))

    def part1(self):
        size = 25 * 6
        layers = int(len(self.input) / size)

        min_0 = 1e20
        result = None
        for i in range(layers):
            lay = self.input[i*size:(i+1)*size]
            zeros = lay.count('0')
            if zeros < min_0:
                min_0 = zeros
                result = lay.count('1') * lay.count('2')

        return result

    def part2(self):
        size = 25 * 6
        layers = int(len(self.input) / size)

        im = np.zeros((6,25))
        for i in range(layers):
            i = layers - i - 1
            for j in range(size):
                pix = i*size+j
                im[j // 25][j % 25] = self.input_ints[pix] if self.input_ints[pix] < 2 else im[j // 25][j % 25]

        plt.imshow(im)
        # plt.show()  # Comment out for benchmarking purposes
