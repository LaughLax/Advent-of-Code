import regex


class RuleNode:
    def __init__(self, node_id):
        self.id = node_id
        self.lchildren = []
        self.rchildren = []

        self.char = None

    def as_re(self, pt2):
        if pt2:
            if self.id == 8:
                return f'({"".join([c.as_re(pt2) for c in self.lchildren])})+'
            elif self.id == 11:
                return f'(?P<p11>{self.lchildren[0].as_re(pt2)}(?P>p11)?{self.lchildren[1].as_re(pt2)})'
                pass

        if self.char is not None:
            return self.char
        elif self.rchildren:
            return f'(({"".join([c.as_re(pt2) for c in self.lchildren])})' \
                   + '|' + \
                   f'({"".join([c.as_re(pt2) for c in self.rchildren])}))'
        else:
            return f'({"".join([c.as_re(pt2) for c in self.lchildren])})'

    def add_lchild(self, other):
        self.lchildren.append(other)

    def add_rchild(self, other):
        self.rchildren.append(other)

    def set_char(self, ch):
        self.char = ch


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        rules, lines = self.input.split('\n\n')
        self.lines = lines.split()

        d_rules = {}
        for line in rules.splitlines():
            pref, rem = line.split(': ')
            d_rules[int(pref)] = list(rem.split(' '))

        r_nodes = {}
        for i in d_rules:
            r_nodes[i] = RuleNode(i)

        for i in d_rules:
            rule = d_rules[i]
            left = True
            for part in rule:
                if part == '|':
                    left = False
                    continue
                if part == '"a"':
                    r_nodes[i].set_char('a')
                    break
                elif part == '"b"':
                    r_nodes[i].set_char('b')
                    break

                if left:
                    r_nodes[i].add_lchild(r_nodes[int(part)])
                else:
                    r_nodes[i].add_rchild(r_nodes[int(part)])

        self.rules = r_nodes

    def part1(self):
        reg = self.rules[0].as_re(False)
        pattern = regex.compile(reg)

        count = 0
        for line in self.lines:
            if pattern.fullmatch(line):
                count += 1

        return count

    def part2(self):
        reg = self.rules[0].as_re(True)
        pattern = regex.compile(reg)

        count = 0
        for line in self.lines:
            if pattern.fullmatch(line):
                count += 1

        return count
