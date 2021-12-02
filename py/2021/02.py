class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = [line.split(' ') for line in f.read().splitlines()]

    def part1(self):
        x, y = 0, 0
        for dir, amt in self.input:
            amt = int(amt)
            if dir == 'forward':
                x += amt
            elif dir == 'up':
                y -= amt
            elif dir == 'down':
                y += amt
        return x * y

    def part2(self):
        x, y, aim = 0, 0, 0
        for dir, amt in self.input:
            amt = int(amt)
            if dir == 'forward':
                x += amt
                y += amt*aim
            elif dir == 'up':
                aim -= amt
            elif dir == 'down':
                aim += amt
        return x*y
