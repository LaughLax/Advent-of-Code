class TreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.root = self

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
        return len(self.children) + sum([child.count_direct_orbits() for child in self.children])

    def count_indirect_orbits(self):
        return sum([child.count_direct_orbits() for child in self.children]) + sum([child.count_indirect_orbits() for child in self.children])


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
        root = next(iter(self.nodes.values())).root

        # print(root.name)
        # print([c.name for c in root.children])
        return root.count_direct_orbits() + root.count_indirect_orbits()

    def part2(self):
        you = self.nodes['YOU']
        santa = self.nodes['SAN']

        searched = []
        this_round = [you]
        next_round = []
        round = 0

        found = False
        while not found:
            round += 1
            # print(f'\nRound {round}!')
            # print([str(node) for node in this_round])

            while len(this_round) > 0:
                node = this_round.pop()
                if node in searched:
                    continue
                searched.append(node)
                if node.parent is not None:
                    # print(node.parent)
                    if santa is node.parent:
                        found = True
                    elif node.parent not in searched:
                        next_round.append(node.parent)
                for child in node.children:
                    # print(child)
                    if santa is child:
                        found = True
                    elif child not in searched:
                        next_round.append(child)
                if found:
                    break

            this_round = next_round
            next_round = []

        return round - 2
