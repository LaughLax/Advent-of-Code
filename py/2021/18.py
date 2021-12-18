from copy import deepcopy
import math


class SnailNum:

    def __init__(self, string):
        self.nums = []
        depth = 0
        for i, ch in enumerate(string):
            if ch == '[':
                depth += 1
            elif ch == ']':
                depth -= 1
            elif ch == ',':
                continue
            else:
                self.nums.append(Number(depth, int(ch)))

    def reduce(self):
        while True:
            try:
                exploders = [n.depth >= 5 for n in self.nums]
                ind = exploders.index(True)
                self.explode(ind)
            except ValueError:
                try:
                    splitters = [n.value >= 10 for n in self.nums]
                    ind = splitters.index(True)
                    self.split(ind)
                except ValueError:
                    return

    def explode(self, ind):
        left = self.nums[ind].value
        right = self.nums[ind+1].value
        if ind > 0:
            self.nums[ind-1].value += left
        if ind+2 < len(self.nums):
            self.nums[ind+2].value += right
        self.nums[ind].depth -= 1
        self.nums[ind].value = 0
        self.nums.pop(ind+1)

    def split(self, ind):
        s = self.nums[ind]
        left = math.floor(s.value / 2.0)
        right = math.ceil(s.value / 2.0)
        s.depth += 1
        s.value = left
        self.nums.insert(ind+1, Number(s.depth, right))

    def add(self, other):
        s_copy = deepcopy(self)
        for n in s_copy.nums:
            n.depth += 1
        o_copy = deepcopy(other)
        for n in o_copy.nums:
            n.depth += 1

        tot = SnailNum('')
        tot.nums = s_copy.nums
        tot.nums.extend(o_copy.nums)
        tot.reduce()
        return tot

    def mult(self):
        reduced = deepcopy(self.nums)
        while len(reduced) > 1:
            for i, n in enumerate(reduced[:-1].copy()):
                if n.depth == reduced[i+1].depth:
                    n.depth -= 1
                    n.value = 3*n.value + 2*reduced[i+1].value
                    reduced.pop(i+1)
                    break
        return reduced[0].value

    def __str__(self):
        curr_d = self.nums[0].depth
        string = '['*curr_d + str(self.nums[0].value)
        for num in self.nums[1:]:
            d_d = num.depth - curr_d
            if d_d == 0:
                string += f",{num.value}"
            elif d_d > 0:
                string += '[' * d_d + str(num.value)
            elif d_d < 0:
                string += ']' * -d_d + ',' + str(num.value)
            curr_d += d_d

        return string + ']'*curr_d

    def __repr__(self):
        return str(self.nums)


class Number:

    def __init__(self, depth, value):
        self.depth = depth
        self.value = value

    def __repr__(self):
        return f"({self.depth}, {self.value})"


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
        self.nums = [SnailNum(line) for line in self.input]

    def part1(self):
        total = self.nums[0]
        for num in self.nums[1:]:
            total = total.add(num)
        return total.mult()

    def part2(self):
        max_mult = 0
        for i in range(len(self.nums)-1):
            for j in range(i+1, len(self.nums)):

                s = self.nums[i].add(self.nums[j])
                res = s.mult()
                if res > max_mult:
                    max_mult = res

                s = self.nums[j].add(self.nums[i])
                res = s.mult()
                if res > max_mult:
                    max_mult = res
        return max_mult
