class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().split('\n\n')

    def part1(self):
        total = 0
        for group in self.input:
            group_ans = set()
            for char in group:
                if char != '\n':
                    group_ans.add(char)
            total += len(group_ans)
        return total

    def part2(self):
        total = 0
        for group in self.input:
            g = group.splitlines()
            group_ans = set(g[0])
            for line in g[1:]:
                group_ans = group_ans & set(line)
            total += len(group_ans)
        return total
