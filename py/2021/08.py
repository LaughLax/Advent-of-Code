def match_map(decoder, val):
    for i, v in enumerate(decoder):
        if val == v:
            return i


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
        self.decode = []
        self.output = []
        for line in self.input:
            decode, output = line.split(" | ")
            self.decode.append(decode.split(" "))
            self.output.append(output.split(" "))

    def part1(self):
        total = 0
        for line in self.output:
            # print(line)
            for digit in line:
                # print(len(digit))
                if len(digit) in (2, 3, 4, 7):
                    total += 1
        return total

    def part2(self):
        # 1 = len(2)
        # 7 = len(3)
        # 4 = len(4)
        # 8 = len(7)
        # 9 = len(6) with all of 4
        # 6 = len(6) missing one from 1
        # 0 = remaining len(6)
        # 5 = len(5) fully in 6
        # 3 = remaining len(5) fully in 9
        # 2 = remaining len(5) missing one from 1

        total = 0
        for i in range(len(self.input)):
            dec = [set(n) for n in self.decode[i]]
            outp = [set(n) for n in self.output[i]]
            n1 = next(filter(lambda x: len(x) == 2, dec))
            dec.remove(n1)
            n7 = next(filter(lambda x: len(x) == 3, dec))
            dec.remove(n7)
            n4 = next(filter(lambda x: len(x) == 4, dec))
            dec.remove(n4)
            n8 = next(filter(lambda x: len(x) == 7, dec))
            dec.remove(n8)
            n9 = next(filter(lambda x: (len(x) == 6) and n4.issubset(x), dec))
            dec.remove(n9)
            n0 = next(filter(lambda x: (len(x) == 6) and n1.issubset(x), dec))
            dec.remove(n0)
            n6 = next(filter(lambda x: len(x) == 6, dec))
            dec.remove(n6)
            n5 = next(filter(lambda x: (len(x) == 5) and x.issubset(n6), dec))
            dec.remove(n5)
            n3 = next(filter(lambda x: (len(x) == 5) and x.issubset(n9), dec))
            dec.remove(n3)
            n2 = dec.pop()

            n_map = [
                n0,
                n1,
                n2,
                n3,
                n4,
                n5,
                n6,
                n7,
                n8,
                n9,
            ]

            val = (1_000 * match_map(n_map, outp[0])
                   + 100 * match_map(n_map, outp[1])
                   + 10 * match_map(n_map, outp[2])
                   + match_map(n_map, outp[3]))
            total += val

        return total

