class AdventOfCode:

    def __init__(self, filename):
        self.input = [171309, 643603]

    def part1(self):
        count = 0
        dubs = ['00']
        dubs.extend([str(i*11) for i in range(1,10)])

        for i in range(self.input[0], self.input[1] + 1):
            s = str(i)
            doubles = False
            for dub in dubs:
                if dub in s:
                    doubles = True
                    break
            incr = s[0] <= s[1] <= s[2] <= s[3] <= s[4] <= s[5]
            if doubles and incr:
                count += 1

        return count

    def part2(self):
        count = 0
        dubs = ['00']
        dubs.extend([str(i*11) for i in range(1,10)])
        trips = ['000']
        trips.extend([str(i*111) for i in range(1,10)])

        for i in range(self.input[0], self.input[1] + 1):
            s = str(i)

            dub_only = False
            for n in range(10):
                if dubs[n] in s and not trips[n] in s:
                    dub_only = True
                    break
            incr = s[0] <= s[1] <= s[2] <= s[3] <= s[4] <= s[5]

            if dub_only and incr:
                count += 1

        return count
