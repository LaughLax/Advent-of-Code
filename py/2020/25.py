class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        c_pub_key = int(self.input[0])
        d_pub_key = int(self.input[1])

        v = 1
        loop_size = 0
        key_to_use = 0
        while not key_to_use:
            loop_size += 1

            v = (v * 7) % 20201227

            if v == c_pub_key:
                key_to_use = d_pub_key
            elif v == d_pub_key:
                key_to_use = c_pub_key

        v = 1
        for _ in range(loop_size):
            v = (v * key_to_use) % 20201227

        return v

    def part2(self):
        pass
