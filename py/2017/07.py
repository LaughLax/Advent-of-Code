class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            lines = f.read().splitlines()

        self.nodes = {}
        for line in lines:
            node = TreeNode(line)
            self.nodes[node.id] = node

        self.top_node = None

    def part1(self):
        for node in self.nodes.values():
            for child_str in node.child_strings:
                node.add_child(self.nodes[child_str])

        while node.parent:
            node = node.parent

        self.top_node = node

        return node.id

    def part2(self):
        node_before = self.top_node
        while True:
            node_after = node_before.find_imbalance()
            if node_after == node_before:
                break
            node_before = node_after

        return node_after.parent.correct_child_weight() - sum(node_after.children_weights())


class TreeNode:

    def __init__(self, node_string):
        self.string = node_string

        split_str = node_string.split()
        self.id = split_str[0]
        self.weight = int(split_str[1][1:-1])

        self.total_weight = -1
        self.good_kid_weight = -1

        self.child_strings = set()
        if len(split_str) > 2:
            for i in range(len(split_str)-3):
                self.child_strings.add(split_str[i+3].strip(','))

        self.parent = None
        self.children = set()

    def add_child(self, child_node):
        self.children.add(child_node)
        child_node.parent = self

    def get_total_weight(self):
        if self.total_weight > -1:
            return self.total_weight

        self.total_weight = self.weight + sum(child.get_total_weight() for child in self.children)
        return self.total_weight

    def find_imbalance(self):
        if not self.children:
            return self

        if self.good_kid_weight == -1:
            child_list = list(self.children)
            self.good_kid_weight = child_list[0].get_total_weight() if child_list[0].get_total_weight() == child_list[1].get_total_weight() else child_list[2].get_total_weight()

        for child in self.children:
            if child.get_total_weight() != self.good_kid_weight:
                return child

        return self

    def correct_child_weight(self):
        if self.good_kid_weight > -1:
            return self.good_kid_weight

        child_list = list(self.children)
        self.good_kid_weight =  child_list[0].get_total_weight() if child_list[0].get_total_weight() == child_list[1].get_total_weight() else child_list[2].get_total_weight()
        return self.good_kid_weight

    def children_weights(self):
        if not self.children:
            return tuple([0])
        return [child.weight + sum(child.children_weights()) for child in self.children]

