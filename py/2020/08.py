import networkx as nx


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.code = [line.split(' ') for line in self.input]
        self.code = [(i[0], int(i[1])) for i in self.code]

    def part1(self):
        ptr = 0
        acc = 0
        seen = set()
        while ptr not in seen:
            seen.add(ptr)
            if self.code[ptr][0] == 'acc':
                acc += self.code[ptr][1]
                ptr += 1
            elif self.code[ptr][0] == 'jmp':
                ptr += self.code[ptr][1]
            elif self.code[ptr][0] == 'nop':
                ptr += 1
        return acc

    def part2(self):
        g = nx.DiGraph()

        for i, line in enumerate(self.code):
            if line[0] != 'acc':
                g.add_edge(i,
                           i + line[1] if line[0] == 'nop' else i + 1,
                           weight=100_000)
            g.add_edge(i,
                       i + line[1] if line[0] == 'jmp' else i + 1,
                       weight=line[1] if line[0] == 'acc' else 0)
        path_len = nx.shortest_path_length(g, 0, 625, weight='weight')
        return path_len - 100_000
