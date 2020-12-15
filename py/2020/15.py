class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = [int(val) for val in f.read().strip().split(',')]

    def run_part(self, stop_at):
        turn = len(self.input)

        recent = dict()
        for i, val in enumerate(self.input[:-1]):
            recent[val] = i + 1
        last_val = self.input[-1]

        next_num = None
        while turn < stop_at:
            if last_val in recent:
                next_num = turn - recent[last_val]
            else:
                next_num = 0

            recent[last_val] = turn
            last_val = next_num
            turn += 1

        return next_num

    def part1(self):
        return self.run_part(2020)

    def part2(self):
        return self.run_part(30_000_000)
