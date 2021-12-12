import networkx as nx


class Tree1:

    def __init__(self, graph, current_node, parent=None):
        self.G = graph
        self.node = current_node
        self.parent = parent
        self.children = []
        if parent is not None:
            parent.children.append(self)

        p = self
        self.path_so_far = []
        while True:
            self.path_so_far.append(p.node)
            if p.parent is None:
                break
            p = p.parent

    def explore(self):
        if self.node == 'end':
            return
        for n in self.G.neighbors(self.node):
            if n in self.path_so_far and n.lower() == n:
                continue
            Tree1(self.G, n, self).explore()

    def num_children(self):
        if len(self.children) == 0 and self.node == 'end':
            return 1
        else:
            return sum(c.num_children() for c in self.children)

    def paths(self):
        if len(self.children) == 0:
            n = self
            path = []
            while True:
                path.append(n.node)
                if n.parent is None:
                    break
                n = n.parent
            return [path[::-1]]
        else:
            paths = []
            for c in self.children:
                paths.extend(c.paths())
            return paths


class Tree2:

    def __init__(self, graph, current_node, parent=None):
        self.G = graph
        self.node = current_node
        self.parent = parent
        self.children = []
        if parent is not None:
            parent.children.append(self)

        p = self
        self.path_so_far = []
        while True:
            self.path_so_far.append(p.node)
            if p.parent is None:
                break
            p = p.parent

    def explore(self, doubled=False):
        if self.node == 'end':
            return
        for n in self.G.neighbors(self.node):
            if n == 'start':
                continue
            if n in self.path_so_far and n.lower() == n:
                if self.path_so_far.count(n) > 1:
                    continue
                elif doubled:
                    continue
                else:
                    Tree2(self.G, n, self).explore(True)
            else:
                Tree2(self.G, n, self).explore(doubled)

    def num_children(self):
        if len(self.children) == 0 and self.node == 'end':
            return 1
        else:
            return sum(c.num_children() for c in self.children)

    def paths(self):
        if len(self.children) == 0:
            if self.node != 'end':
                return []
            n = self
            path = []
            while True:
                path.append(n.node)
                if n.parent is None:
                    break
                n = n.parent
            return [path[::-1]]
        else:
            paths = []
            for c in self.children:
                paths.extend(c.paths())
            return paths


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
        self.G = nx.Graph()
        for line in self.input:
            f, t = line.split('-')
            self.G.add_edge(f, t)

    def part1(self):
        tree = Tree1(self.G, 'start')
        tree.explore()
        return tree.num_children()

    def part2(self):
        tree = Tree2(self.G, 'start')
        tree.explore()
        return tree.num_children()
