import numpy as np


class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().strip()
        self.stuff = list(map(int, self.input))
        self.signal_array = np.array(self.stuff, dtype=np.int16)

        # self.pattern2 = np.empty_like(self.signal_array)

    def fft_all(self, in_array):
        out_array = np.empty_like(in_array)
        for i in range(len(in_array)):
            out_array[i] = self.fft_pos(in_array, i)

        return np.array(out_array)

    def fft_pos(self, in_array, position):
        base = [0, 1, 0, -1]
        base_2 = []
        for i in base:
            base_2.extend([i] * (position + 1))

        pattern1 = []
        for i in range(np.ceil(len(in_array)/len(base_2)).astype(np.int64) + 1):
            pattern1.extend(base_2)
        pattern1 = pattern1[position+1:len(in_array) + 1]

        # inner_cum = 0
        # for i in range(len(in_array)):
        #     base_ind = ((i + 1) // (position + 1)) % 4
        #     inner_cum += in_array[i] * base[base_ind]

        # pattern2 = np.empty_like(in_array)
        # for i in range(len(in_array)):
        #     ind = ((i + 1) // (position + 1)) % 4
        #     pattern2[i] = base[ind]

        # inner_prod = in_array.dot(pattern1)
        inner_prod = in_array[position:].dot(pattern1)

        return np.abs(inner_prod) % 10

    def part1(self):
        arr = self.signal_array
        for i in range(100):
            # print(i)
            arr = self.fft_all(arr)

        return arr[:8]

    def modified_fft(self, in_array):
        out_array = np.cumsum(in_array)

        out_array = np.abs(out_array) % 10

        return out_array

    def part2(self):
        offset = self.stuff[:7]
        offset = offset[0] * 1_000_000 + \
                 offset[1] * 100_000 + \
                 offset[2] * 10_000 + \
                 offset[3] * 1_000 + \
                 offset[4] * 100 + \
                 offset[5] * 10 + \
                 offset[6]
        in_len = len(self.stuff)
        num_reps = int(np.ceil((in_len * 10_000 - offset) / in_len))
        new_offset = offset - in_len * (10_000 - num_reps)
        arr = np.flip(np.array(self.stuff * num_reps, dtype=np.int64).flatten()[new_offset:])
        for i in range(100):
            arr = self.modified_fft(arr)

        return np.flip(arr)[:8]
        # higher than 02990190

