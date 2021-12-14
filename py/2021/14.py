from functools import lru_cache


def dict_merge(d1, d2):
    res = d1.copy()
    for key in d2:
        res[key] = d2[key] + res.setdefault(key, 0)
    return res


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
        res = dict_merge(r1, r2)
        res[new_char] -= 1
        return res
    except ValueError:
        return default


def propagate(string, r_in, r_out, depth):
    full_res = {}
    for i in range(len(string) - 1):
        res = recurse(string[i:i + 2], r_in, r_out, depth)
        full_res = dict_merge(full_res, res)
        if i > 1:
            full_res[string[i]] -= 1
    min_ct = 1e100
    max_ct = 0
    for ch in full_res:
        ct = full_res[ch]
        if ct < min_ct:
            min_ct = ct
        if ct > max_ct:
            max_ct = ct
    return max_ct - min_ct


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
        self.start, rules = self.input.strip().split('\n\n')
        self.rules_in = []
        self.rules_out = []
        for rule in rules.splitlines():
            r_in, r_out = rule.split(' -> ')
            self.rules_in.append(r_in)
            self.rules_out.append(r_out)

    def part1(self):
        recurse.cache_clear()
        return propagate(self.start, tuple(self.rules_in), tuple(self.rules_out), 10)

    def part2(self):
        recurse.cache_clear()
        return propagate(self.start, tuple(self.rules_in), tuple(self.rules_out), 40)
