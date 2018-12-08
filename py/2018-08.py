class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = list(map(int, f.read().split()))

        self.tree_top_node = TreeNode(self.input, 0)

    def part1(self):
        return self.tree_top_node.metadata_sum()

    def part2(self):
        return self.tree_top_node.value()


class TreeNode:

    def __init__(self, input_list, pos):
        num_children = input_list[pos]
        num_metadata = input_list[pos+1]
        pos += 2

        self.children = []
        for i in range(num_children):
            self.children.append(TreeNode(input_list, pos))
            pos += self.children[i].length()

        self.metadata = []
        for i in range(num_metadata):
            self.metadata.append(input_list[pos])
            pos += 1

    def length(self):
        return 2 + len(self.metadata) + sum(c.length() for c in self.children)

    def metadata_sum(self):
        return sum(self.metadata) + sum([c.metadata_sum() for c in self.children])

    def value(self):
        if not self.children:
            return sum(self.metadata)

        my_sum = 0

        for i in self.metadata:
            if 0 < i <= len(self.children):
                my_sum += self.children[i-1].value()

        return my_sum
