class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = [int(val) for val in f.read().strip().split(',')]

    def part1(self):
        turn = len(self.input)
        rounds = self.input.copy()

        most_recent = dict()
        for i, val in enumerate(rounds):
            if i == len(rounds) - 1:
                break
            most_recent[val] = i+1

        while turn < 2020:
            turn += 1

            if rounds[-1] in most_recent:
                next_num = turn - most_recent[rounds[-1]] - 1
            else:
                next_num = 0

            most_recent[rounds[-1]] = turn - 1
            rounds.append(next_num)

        return rounds[2019]

    def part2(self):
        turn = len(self.input)

        most_recent = dict()
        for i, val in enumerate(self.input):
            if i == len(self.input) - 1:
                break
            most_recent[val] = i+1
        last_val = self.input[-1]

        while turn < 30_000_000:
            turn += 1

            if last_val in most_recent:
                next_num = turn - most_recent[last_val] - 1
            else:
                next_num = 0

            most_recent[last_val] = turn - 1
            last_val = next_num

        return next_num
