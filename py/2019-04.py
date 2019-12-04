class AdventOfCode:

    def __init__(self, filename):
        self.input = [171309, 643603]

    def part1(self):
        count = 0
        dubs = ['00']
        dubs.extend([str(i*11) for i in range(1,10)])

        for i in range(self.input[0], self.input[1] + 1):
            s = str(i)
            doubles = any([dub in s for dub in dubs])
            incr = (i // 100000) \
                    <= (i // 10000 - 10*(i // 100000)) \
                    <= (i // 1000 - 10*(i // 10000)) \
                    <= (i // 100 - 10*(i // 1000)) \
                    <= (i // 10 - 10*(i // 100)) \
                    <= (i // 1 - 10*(i // 10))
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

            dub_only = any([dubs[n] in s and not trips[n] in s for n in range(10)])
            incr = (i // 100000) \
                    <= (i // 10000 - 10*(i // 100000)) \
                    <= (i // 1000 - 10*(i // 10000)) \
                    <= (i // 100 - 10*(i // 1000)) \
                    <= (i // 10 - 10*(i // 100)) \
                    <= (i // 1 - 10*(i // 10))

            if dub_only and incr:
                count += 1

        return count
