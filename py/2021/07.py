import numpy as np


def p2fuel(locs, test_loc):
    dist = np.abs(locs - test_loc)
    return np.sum((dist + 1) * dist / 2)


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = list(map(int, f.read().split(',')))

    def part1(self):
        loc = np.array(self.input)
        avg = int(np.mean(loc))
        best = np.sum(np.abs(loc - avg))
        direction = -1 if np.sum(np.abs(loc - avg + 1)) < best else 1
        test = avg + direction
        while True:
            fuel = np.sum(np.abs(loc-test))
            if fuel < best:
                best = fuel
                test += direction
            else:
                return best

    def part2(self):
        loc = np.array(self.input)
        avg = int(np.mean(loc))
        best = p2fuel(loc, avg)
        direction = -1 if p2fuel(loc, avg-1) < best else 1
        test = avg + direction
        while True:
            fuel = p2fuel(loc, test)
            if fuel < best:
                best = fuel
                test += direction
            else:
                return best
