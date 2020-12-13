import numpy as np


class Node:

    def __init__(self, val):
        self.val = val
        self.parents = []
        self.children = []

        self.num_paths = None

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

    def paths_down(self):
        if self.num_paths is not None:
            return self.num_paths

        if len(self.children) == 0:
            self.num_paths = 1
        else:
            self.num_paths = sum([c.paths_down() for c in self.children])

        return self.num_paths


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.input = sorted([int(i) for i in self.input])

    def part1(self):
        j = np.array(self.input)
        diffs = np.diff(j)
        ones = np.count_nonzero(diffs == 1)
        threes = np.count_nonzero(diffs == 3)
        return (ones + 1) * (threes + 1)

    def part2(self):
        nodes = dict()
        nodes[0] = Node(0)
        for val in self.input:
            nodes[val] = Node(val)
            for i in range(1,4):
                if val-i in nodes:
                    nodes[val-i].add_child(nodes[val])
        nodes[val+3] = Node(val+3)

        return nodes[0].paths_down()
