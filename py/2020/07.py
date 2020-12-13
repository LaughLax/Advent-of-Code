import networkx as nx
import re


class Tree:

    def __init__(self, color):
        self.color = color
        self.parents = set()
        self.children = dict()

    def add_parent(self, tree, child_count):
        self.parents.add(tree)
        tree.children[self] = int(child_count)

    def __str__(self):
        return self.color

    def contains(self):
        t = 0
        for c in self.children:
            t += self.children[c] * (1 + c.contains())
        return t


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.bags = dict()
        self.parse_input()

    def parse_input(self):
        pattern = re.compile(r'(\d+) (\w+ \w+) bags?')
        for line in self.input:
            bag_type, _, remainder = line.partition(' bags ')
            children = pattern.findall(remainder)
            if bag_type not in self.bags:
                self.bags[bag_type] = Tree(bag_type)
            for c in children:
                if c[1] not in self.bags:
                    self.bags[c[1]] = Tree(c[1])
                self.bags[c[1]].add_parent(self.bags[bag_type], c[0])

    def part1(self):
        q = 'shiny gold'
        unexplored = set(self.bags[q].parents)
        parents = set()
        while len(unexplored) > 0:
            bag = unexplored.pop()
            parents.add(bag)
            for b in bag.parents:
                if b not in parents:
                    unexplored.add(b)
        return len(parents)

    def part2(self):
        return self.bags['shiny gold'].contains()
