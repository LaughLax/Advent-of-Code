class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = [list(map(int, line.split())) for line in f.read().splitlines()]

    def part1(self):
        return sum([max(line) - min(line) for line in self.input])

    @staticmethod
    def get_row_division(row):
        for i, val_1 in enumerate(row):
            for val_2 in row[i+1:]:
                div = max(val_1, val_2) / min(val_1, val_2)
                if int(div) == div:
                    return int(div)

    def part2(self):
        return sum([self.get_row_division(line) for line in self.input])
