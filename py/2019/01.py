import math

class AdventOfCode:

    def __init__(self, filename):
        self.masses = []

        with open(filename) as f:
            self.input = f.read().splitlines()
            for line in self.input:
                self.masses.append(int(line))

    def part1(self):
        total_fuel = 0
        for m in self.masses:
            total_fuel += math.floor(m / 3) - 2

        return total_fuel

    def part2(self):
        total_fuel = 0
        for m in self.masses:
            inc_fuel = [math.floor(m / 3) - 2]
            while inc_fuel[-1] >= 0:
                new_inc_fuel = math.floor(inc_fuel[-1] / 3) - 2
                if new_inc_fuel > 0:
                    inc_fuel.append(new_inc_fuel)
                else:
                    break

            total_fuel += sum(inc_fuel)

        return total_fuel

