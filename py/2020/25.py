class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        c_pub_key = int(self.input[0])
        d_pub_key = int(self.input[1])

        v = 1
        c_loop, d_loop = 0, 0
        c_found, d_found = False, False
        while not c_found and not d_found:
            if not c_found:
                c_loop += 1
            if not d_found:
                d_loop += 1

            v = (v * 7) % 20201227

            if v == c_pub_key:
                c_found = True
            if v == d_pub_key:
                d_found = True

        v = 1
        if c_found:
            for _ in range(c_loop):
                v = (v * d_pub_key) % 20201227
        elif d_found:
            for _ in range(d_loop):
                v = (v * c_pub_key) % 20201227

        return v

    def part2(self):
        pass
