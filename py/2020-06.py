class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().split('\n\n')

    def part1(self):
        total = 0
        for group in self.input:
            q_s = set()
            for line in group:
                for char in line.strip():
                    q_s.add(char)
            total += len(q_s)
        return total


    def part2(self):
        total = 0
        for group in self.input:
            q_s = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
            for line in group.splitlines():
                person = set()
                for char in line.strip():
                    person.add(char)
                q_s = q_s & person
            total += len(q_s)
        return total
