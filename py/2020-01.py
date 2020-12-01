class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

            self.input = list(map(int, self.input))

    def part1(self):
        for i in range(len(self.input)):
            for j in range(i, len(self.input)):
                if self.input[i] + self.input[j] == 2020:
                    print(self.input[i])
                    print(self.input[j])
                    return self.input[i] * self.input[j]

    def part2(self):
        for i in range(len(self.input)):
            for j in range(i+1, len(self.input)):
                for k in range(j+1, len(self.input)):
                    if self.input[i] + self.input[j] + self.input[k] == 2020:
                        print(self.input[i])
                        print(self.input[j])
                        print(self.input[k])
                        return self.input[i] * self.input[j] * self.input[k]
