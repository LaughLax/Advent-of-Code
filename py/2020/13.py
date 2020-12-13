import re


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        buses = self.input[1].split(',')
        self.times = []
        for i, bus in enumerate(buses):
            if bus != 'x':
                self.times.append((i, int(bus)))

    def part1(self):
        t0 = int(self.input[0])

        min_wait = 1_000_000_000
        min_bus = 0
        for bus in self.times:
            t = bus[1] - (t0 % bus[1]) if t0 % bus[1] > 0 else 0
            if t < min_wait:
                min_wait = t
                min_bus = bus[1]

        return min_wait*min_bus

    def part2(self):
        n = 0
        interval = self.times[0][1]
        all_t = frozenset(self.times[1:])
        found_t = set()
        while len(found_t) < len(all_t):
            n += interval
            for bus in all_t - found_t:
                if (n+bus[0]) % bus[1] == 0:
                    found_t.add(bus)
                    interval *= bus[1]

        return n
