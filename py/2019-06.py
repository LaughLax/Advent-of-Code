class TreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.root = self

        self.d_o = None
        self.i_o = None

    def add_child(self, child):
        child.parent = self
        child.set_root(self.root)
        self.children.append(child)

    def set_root(self, root):
        self.root = root
        for child in self.children:
            child.set_root(root)

    def get_root(self):
        if self.parent is not None:
            return self.parent.get_root()
        else:
            return self

    def count_direct_orbits(self):
        if self.d_o is None:
            self.d_o = len(self.children) + sum([child.count_direct_orbits() for child in self.children])
        return self.d_o

    def count_indirect_orbits(self):
        if self.i_o is None:
            self.i_o = sum([child.count_direct_orbits() for child in self.children]) + sum([child.count_indirect_orbits() for child in self.children])
        return self.i_o


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            input = f.read().splitlines()

        self.nodes = {}
        for line in input:
            n = line.split(')')
            if n[0] not in self.nodes:
                self.nodes[n[0]] = TreeNode(n[0])
            if n[1] not in self.nodes:
                self.nodes[n[1]] = TreeNode(n[1])
            self.nodes[n[0]].add_child(self.nodes[n[1]])

    def part1(self):
        # Reset orbit count cache, for fair benchmarking
        for node in self.nodes:
            self.nodes[node].d_o = None
            self.nodes[node].i_o = None

        root = next(iter(self.nodes.values())).root

        return root.count_direct_orbits() + root.count_indirect_orbits()

    def part2(self):
        you = self.nodes['YOU']
        santa = self.nodes['SAN']

        youpath = set()
        sanpath = set()
        temp = you
        while temp.parent is not None:
            youpath.add(temp)
            temp = temp.parent
        temp = santa
        while temp.parent is not None:
            sanpath.add(temp)
            temp = temp.parent

        return len(youpath.symmetric_difference(sanpath)) - 2
