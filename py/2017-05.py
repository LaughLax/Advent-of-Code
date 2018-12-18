class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = list(map(int, f.read().splitlines()))

    def part1(self):
        commands = self.input[:]

        i = 0
        steps = 0

        while 0 <= i < len(commands):
            jump = commands[i]
            commands[i] += 1
            i += jump
            steps += 1

        return steps

    def part2(self):
        commands = self.input[:]

        i = 0
        steps = 0

        while 0 <= i < len(commands):
            jump = commands[i]
            commands[i] += 1 if jump < 3 else -1
            i += jump
            steps += 1

        return steps
