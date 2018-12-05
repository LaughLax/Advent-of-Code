class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        dubs = 0
        trips = 0

        for line in self.input:
            dub = False
            trip = False

            for char in 'abcdefghijklmnopqrstuvwxyz':
                if line.count(char) == 2:
                    dub = True
                elif line.count(char) == 3:
                    trip = True

                if dub and trip:
                    break

            if dub:
                dubs = dubs + 1
            if trip:
                trips = trips + 1
                if dub:
                    continue

        return dubs * trips

    def part2(self):
        length = len(self.input[0])

        for line_index, line1 in enumerate(self.input):
            for line2 in self.input[line_index+1:-1]:
                one_diff = -1
                two_diff = False

                for char_index in range(length):
                    if line1[char_index] != line2[char_index]:
                        if one_diff > -1:
                            two_diff = True
                            break
                        else:
                            one_diff = char_index

                if two_diff:
                    continue

                if one_diff > -1:
                    return line1[0:one_diff] + line1[one_diff+1:]

