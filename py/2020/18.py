class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    @staticmethod
    def eval_expr_pt1(expr_list):
        level = len(expr_list[0]) - 1
        vals = ([0] * level) + [int(expr_list[0][-1])]
        oper = ['+'] * (level+1)
        for i, elem in enumerate(expr_list[1::2]):
            oper[level] = elem
            v2 = expr_list[i*2+2]

            if v2.startswith('('):
                level += len(v2) - 1
                vals.extend([0] * (len(v2) - 2))
                vals.append(int(v2[-1]))
                oper.extend(['+'] * (len(v2)-1))
            else:
                if oper[level] == '+':
                    vals[level] += int(v2[0])
                elif oper[level] == '*':
                    vals[level] *= int(v2[0])

                if v2.endswith(')'):
                    for j in range(len(v2) - 1):
                        oper.pop()
                        level -= 1
                        if oper[level] == '+':
                            vals[level] += vals.pop()
                        elif oper[level] == '*':
                            vals[level] *= vals.pop()

        return vals[0]

    def eval_expr_pt2(self, expr_line):
        while '(' in expr_line:
            s = expr_line.find('(')
            e = s+1
            depth = 1
            for i, ch in enumerate(expr_line[s+1:]):
                if ch == ')':
                    if depth == 1:
                        break
                    else:
                        depth -= 1
                if ch == '(':
                    depth += 1
                e += 1

            pre = expr_line[0:s]
            post = expr_line[e+1:]
            in_paren = self.eval_expr_pt2(expr_line[s+1:e])
            expr_line = f'{pre}{in_paren}{post}'

        expr = expr_line.split(' ')

        while len(expr) > 1:
            # Perform addition
            last_i = len(expr) - 1
            i = 0
            while i <= last_i:
                if expr[i] == '+':
                    item1 = expr[i-1]
                    expr.pop(i)
                    item2 = expr.pop(i)
                    i -= 1
                    expr[i] = int(item1) + int(item2)
                    last_i -= 2
                i += 1

            # Perform multiplication
            last_i = len(expr) - 1
            i = 0
            while i <= last_i:
                if expr[i] == '*':
                    item1 = expr[i-1]
                    expr.pop(i)
                    item2 = expr.pop(i)
                    i -= 1
                    expr[i] = int(item1) * int(item2)
                    last_i -= 2
                i += 1

        return expr[0]

    def part1(self):
        total = 0
        for i, line in enumerate(self.input):
            res = self.eval_expr_pt1(line.split(' '))
            total += res

        return total

    def part2(self):
        total = 0
        for i, line in enumerate(self.input):
            res = self.eval_expr_pt2(line)
            total += res

        return total
