class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().split('\n\n')

    def part1(self):
        total = 0
        for group in self.input:
            group_ans = set(group)
            group_ans.discard('\n')
            total += len(group_ans)
        return total

    def part2(self):
        total = 0
        for group in self.input:
            g = group.splitlines()
            intersection = list(g[0])
            for line in g[1:]:
                for char in list(intersection):
                    if char not in line:
                        intersection.remove(char)
            total += len(intersection)
        return total
