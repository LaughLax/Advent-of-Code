import re


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        t0 = int(self.input[0])
        buses = self.input[1].split(',')
        times = []
        for bus in buses:
            if bus != 'x':
                times.append(int(bus))

        min_wait = 1_000_000_000
        min_bus = 0
        for bus in times:
            t = bus - (t0 % bus) if t0 % bus > 0 else 0
            if t < min_wait:
                min_wait = t
                min_bus = bus

        return min_wait*min_bus

    def part2(self):
        buses = self.input[1].split(',')
        times = []
        n = 0
        for i, bus in enumerate(buses):
            if bus != 'x':
                times.append((i, int(bus)))

        k = 0
        n = 0
        interval = 1
        found_k = dict()
        all_t = frozenset(times[1:])
        while len(found_k.keys()) < len(all_t):
            k += interval
            n = times[0][1] * k
            for bus in times[1:]:
                if bus in found_k:
                    continue
                if (n+bus[0]) % bus[1] == 0:
                    found_k[bus] = k
                    interval *= bus[1]

        return n
