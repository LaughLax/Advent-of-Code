import numpy as np


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = np.array(list(map(int, f.read().split(','))))

        # Keys = days left in sim
        # Values = # of fish at end of sim
        # Sim as defined for this dict starts with 1 fish (0 days til spawn)
        self.fish_prop_map = dict()

    def part1(self):
        fish = dict()
        for i in range(9):
            fish[i] = np.sum(self.input == i)
        for _ in range(80):
            new = fish[0]
            for i in range(8):
                fish[i] = fish[i+1]
            fish[6] += new
            fish[8] = new
        return np.sum([fish[i] for i in range(9)])

    def part2(self):
        # I borrowed this really cool approach from github.com/alfiejfs
        self.fish_prop_map.clear()
        fish = dict()
        for i in range(7):
            fish[i] = np.sum(self.input == i)
        total = np.ulonglong(0)
        for i in range(7):
            total += fish[i]*self.fish_props(256-i)
        return total

    def fish_props(self, duration):
        if duration in self.fish_prop_map:
            return self.fish_prop_map[duration]

        if duration <= 0:
            self.fish_prop_map[duration] = np.ulonglong(1)
            return self.fish_prop_map[duration]

        if duration not in self.fish_prop_map:
            self.fish_prop_map[duration] = (self.fish_props(duration-7)
                                            + self.fish_props(duration-9))

            return self.fish_prop_map[duration]
