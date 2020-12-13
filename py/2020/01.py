class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

            self.input = sorted(list(map(int, self.input)))

    def part1(self):
        for i in range(len(self.input)):
            num_i = self.input[i]
            for j in range(i, len(self.input)):
                num_j = self.input[j]

                if num_i + num_j == 2020:
                    return num_i * num_j

                elif num_i + num_j > 2020:
                    break

    def part2(self):
        for i in range(len(self.input)):
            num_i = self.input[i]
            for j in range(i+1, len(self.input)):
                num_j = self.input[j]
                if num_i + num_j > 2020:
                    break
                for k in range(j+1, len(self.input)):
                    num_k = self.input[k]

                    if num_i + num_j + num_k == 2020:
                        return num_i * num_j * num_k
                    elif num_i + num_j + num_k > 2020:
                        break
