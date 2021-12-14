from functools import lru_cache


@lru_cache(maxsize=None)
def recurse(chars, r_in, r_out, depth):
    default = {
            chars[0]: 1,
            chars[-1]: 2 if chars[0] == chars[-1] else 1
        }
    if depth == 0:
        return default

    try:
        ind = r_in.index(chars)
        new_char = r_out[ind]
        r1 = recurse(chars[0] + new_char, r_in, r_out, depth-1)
        r2 = recurse(new_char + chars[1], r_in, r_out, depth-1)
        res = r1.copy()
        for key in r2:
            if key in res:
                res[key] += r2[key]
            else:
                res[key] = r2[key]
        res[new_char] -= 1
        return res
    except ValueError:
        return default


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
        self.chars = set()
        self.start, rules = self.input.strip().split('\n\n')
        self.chars |= set(self.start)
        self.rules_in = []
        self.rules_out = []
        for rule in rules.splitlines():
            r_in, r_out = rule.split(' -> ')
            self.rules_in.append(r_in)
            self.chars |= set(r_in)
            self.rules_out.append(r_out)
            self.chars |= set(r_out)

    def part1(self):
        poly = self.start
        for _ in range(10):
            new_poly = ''
            for i in range(len(poly)-1):
                new_poly += poly[i]
                try:
                    ind = self.rules_in.index(poly[i:i+2])
                    new_poly += self.rules_out[ind]
                except ValueError:
                    continue
            new_poly += poly[-1]
            poly = new_poly
        min_ct = 1e100
        max_ct = 0
        for ch in self.chars:
            ct = poly.count(ch)
            if ct < min_ct:
                min_ct = ct
            if ct > max_ct:
                max_ct = ct
        return max_ct - min_ct

    def part2(self):
        recurse.cache_clear()
        poly = self.start
        full_res = {}
        for i in range(len(poly)-1):
            res = recurse(poly[i:i+2], tuple(self.rules_in), tuple(self.rules_out), 40)
            for key in res:
                if key in full_res:
                    full_res[key] += res[key]
                else:
                    full_res[key] = res[key]
            if i > 1:
                full_res[poly[i]] -= 1
        min_ct = 1e100
        max_ct = 0
        for ch in full_res:
            ct = full_res[ch]
            if ct < min_ct:
                min_ct = ct
            if ct > max_ct:
                max_ct = ct
        return max_ct - min_ct
