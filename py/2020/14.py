import re


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        vals = dict()
        mask_0s = 0
        mask_1s = 0
        pattern = re.compile(r'mem\[(\d+)\] = (\d+)')
        for line in self.input:
            if line.startswith('mask'):
                mask_0s = 0
                mask_1s = 0
                for i, char in enumerate(line[7:]):
                    if char == '0':
                        mask_0s += 1 << (35-i)
                    elif char == '1':
                        mask_1s += 1 << (35-i)
            else:
                addr, val = pattern.match(line).group(1, 2)
                val_m0 = int(val) & ((1 << 36) - 1 - mask_0s)
                val_m1 = val_m0 | mask_1s
                vals[int(addr)] = val_m1

        total = 0
        for key in vals:
            total += vals[key]

        return total

    def part2(self):
        vals = dict()
        mask_1s = 0
        mask_xs = set()
        pattern = re.compile(r'mem\[(\d+)\] = (\d+)')
        for line in self.input:
            if line.startswith('mask'):
                mask_0s = 0
                mask_1s = 0
                mask_xs.clear()
                for i, char in enumerate(line[7:]):
                    if char == '0':
                        mask_0s += 1 << (35 - i)
                    elif char == '1':
                        mask_1s += 1 << (35 - i)
                    else:
                        mask_xs.add(35-i)
            else:
                addr, val = pattern.match(line).group(1, 2)

                addr_m1 = int(addr) | mask_1s
                addrs = [addr_m1]

                for i in mask_xs:
                    new_addrs = []
                    x_val = 1 << i
                    for address in addrs:
                        new_addrs.append(address | x_val)
                        new_addrs.append(address & ((1 << 36) - 1 - x_val))
                    addrs = new_addrs

                for a in addrs:
                    vals[a] = int(val)

        total = 0
        for key in vals:
            total += vals[key]

        return total
