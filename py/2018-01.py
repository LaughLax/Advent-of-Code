class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.shifts = list(map(int, f.read().splitlines()))

    def part1(self):
        return sum(self.shifts)

    def part2(self):
        freq = 0
        seen = set()

        while True:
            for shift in self.shifts:
                freq = freq + shift

                if freq in seen:
                    return freq
                else:
                    seen.add(freq)
