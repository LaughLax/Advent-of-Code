import networkx as nx
import re


class Tree:

    def __init__(self, description, color):
        self.desc = description
        self.color = color
        self.parents = set()
        self.children = dict()

    def add_parent(self, tree, child_count):
        self.parents.add(tree)
        tree.children[self] = int(child_count)

    def __str__(self):
        return f'{self.desc} {self.color}'

    def contains(self):
        t = 0
        for c in self.children:
            t += self.children[c] * (1 + c.contains())
        return t


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        bags = dict()
        pattern = re.compile('(\d+)\s+(\w+)\s+(\w+)\s+bags?')
        for line in self.input:
            bag_type, _, remainder = line.partition(' bags ')
            children = pattern.findall(remainder)
            if bag_type not in bags:
                desc, color = bag_type.split(' ')
                bags[bag_type] = Tree(desc, color)
            for c in children:
                name = f'{c[1]} {c[2]}'
                if name not in bags:
                    bags[name] = Tree(c[1], c[2])
                bags[name].add_parent(bags[bag_type], c[0])

        q = 'shiny gold'
        parents = set(bags[q].parents)
        unexplored = set(parents)
        explored = set()
        while len(unexplored) > 0:
            bag = unexplored.pop()
            parents.add(bag)
            explored.add(bag)
            for b in bag.parents:
                if b not in explored:
                    unexplored.add(b)
        return len(parents)

    def part2(self):
        bags = dict()
        pattern = re.compile('(\d+)\s+(\w+)\s+(\w+)\s+bags?')
        for line in self.input:
            bag_type, _, remainder = line.partition(' bags ')
            children = pattern.findall(remainder)
            if bag_type not in bags:
                desc, color = bag_type.split(' ')
                bags[bag_type] = Tree(desc, color)
            for c in children:
                name = f'{c[1]} {c[2]}'
                if name not in bags:
                    bags[name] = Tree(c[1], c[2])
                bags[name].add_parent(bags[bag_type], c[0])
        return bags['shiny gold'].contains()
