class JumpNode:

    def __init__(self, line_no, cmd, val):
        self.line_no = line_no
        self.cmd = cmd
        self.val = val

        self.main_target = {'jmp': line_no + val,
                            'nop': line_no + 1,
                            'acc': line_no + 1}.get(cmd)
        self.alt_target = {'nop': line_no + val,
                           'jmp': line_no + 1,
                           'acc': line_no + 1}.get(cmd)

        self.main_t_obj = None
        self.alt_t_obj = None

        self.m_path_end = None
        self.a_path_end = None

    def set_main_t_obj(self, obj):
        self.main_t_obj = obj

    def set_alt_t_obj(self, obj):
        self.alt_t_obj = obj

    def find_main_path(self, seen, acc):
        if self.m_path_end is not None:
            return self.m_path_end

        if self.cmd == 'acc':
            acc += self.val

        if self.main_t_obj in seen:
            res = 'inf'
        elif self.main_target == 625:
            res = acc
        elif self.main_target > 625 or self.main_target < 0:
            res = 'bust'
        else:
            res = self.main_t_obj.find_main_path(seen | frozenset([self]), acc)

        self.m_path_end = res
        return res

    def find_alt_path(self, acc):
        if self.a_path_end is not None:
            return self.a_path_end

        if self.cmd == 'acc':
            acc += self.val

        if 0 <= self.alt_target < 625:
            res = self.alt_t_obj.find_main_path(frozenset(), acc)
        elif self.alt_target == 625:
            res = acc
        else:
            res = 'bust'

        self.a_path_end = res
        return res


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
        nodes = []
        for i, line in enumerate(self.code):
            nodes.append(JumpNode(i, line[0], line[1]))
        for node in nodes:
            if 0 <= node.main_target < 625:
                node.set_main_t_obj(nodes[node.main_target])
            if 0 <= node.alt_target < 625:
                node.set_alt_t_obj(nodes[node.alt_target])

        node = nodes[0]
        ans = node.find_main_path(frozenset(), 0)
        acc = 0
        while not isinstance(ans, int):
            ans = node.find_alt_path(acc)
            if node.cmd == 'acc':
                acc += node.val
            node = node.main_t_obj
        return ans
