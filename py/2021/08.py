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
        # 0 = remaining len(6) with all of 1
        # 6 = remaining len(6)
        # 5 = len(5) fully in 6
        # 3 = remaining len(5) fully in 9
        # 2 = remaining len(5) missing one from 1

        total = 0
        nums = [None]*10
        for i in range(len(self.input)):
            dec = [set(n) for n in self.decode[i]]
            outp = [set(n) for n in self.output[i]]

            nums[1] = next(filter(lambda x: len(x) == 2, dec))
            dec.remove(nums[1])
            nums[7] = next(filter(lambda x: len(x) == 3, dec))
            dec.remove(nums[7])
            nums[4] = next(filter(lambda x: len(x) == 4, dec))
            dec.remove(nums[4])
            nums[8] = next(filter(lambda x: len(x) == 7, dec))
            dec.remove(nums[8])
            nums[9] = next(filter(lambda x: (len(x) == 6) and nums[4].issubset(x), dec))
            dec.remove(nums[9])
            nums[0] = next(filter(lambda x: (len(x) == 6) and nums[1].issubset(x), dec))
            dec.remove(nums[0])
            nums[6] = next(filter(lambda x: len(x) == 6, dec))
            dec.remove(nums[6])
            nums[5] = next(filter(lambda x: (len(x) == 5) and x.issubset(nums[6]), dec))
            dec.remove(nums[5])
            nums[3] = next(filter(lambda x: (len(x) == 5) and x.issubset(nums[9]), dec))
            dec.remove(nums[3])
            nums[2] = dec.pop()

            val = (1_000 * nums.index(outp[0])
                   + 100 * nums.index(outp[1])
                   + 10 * nums.index(outp[2])
                   + nums.index(outp[3]))
            total += val

        return total
