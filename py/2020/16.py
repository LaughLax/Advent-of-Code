class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        self.fields, split, rem = self.input.partition('\n\n')
        self.fields = self.fields.splitlines()
        rem = rem.splitlines()
        self.my_ticket = [int(v) for v in rem[1].split(',')]
        self.tickets = rem[4:]

        self.valid = set()

    def part1(self):
        allowable = set()
        minimum = 0
        maximum = 1_000_000
        for line in self.fields:
            fname, _, nums = line.partition(': ')
            nums_1, nums_2 = nums.split(' or ')
            min_1, max_1 = nums_1.split('-')
            min_2, max_2 = nums_2.split('-')
            min_1, max_1, min_2, max_2 = [int(v) for v in (min_1, max_1, min_2, max_2)]

            if min_1 < minimum:
                minimum = min_1
            if min_2 < minimum:
                minimum = min_2
            if max_1 > maximum:
                maximum = max_1
            if max_2 > maximum:
                maximum = max_2

            for i1 in range (min_1, max_1+1):
                allowable.add(i1)
            for i2 in range (min_2, max_2+1):
                allowable.add(i2)

        error = 0
        for ticket in self.tickets:
            vals_list = tuple(int(v) for v in ticket.split(','))
            vals = set(vals_list)
            bad = vals - allowable
            if len(bad) > 0:
                error += sum(bad)
            else:
                self.valid.add(vals_list)

        return error

    def part2(self):
        f1 = dict()
        f2 = dict()
        for line in self.fields:
            fname, _, nums = line.partition(': ')
            nums_1, nums_2 = nums.split(' or ')
            min_1, max_1 = nums_1.split('-')
            min_2, max_2 = nums_2.split('-')
            f1[fname] = (int(min_1), int(max_1))
            f2[fname] = (int(min_2), int(max_2))

        possible = dict()
        for field in f1:
            possible[field] = list(range(len(f1)))

        for ticket in self.valid:
            for field in possible:
                for i, val in enumerate(ticket):
                    if i in possible[field]:
                        if (f1[field][0] > val or f1[field][1] < val)\
                                and (f2[field][0] > val or f2[field][1] < val):
                            possible[field].remove(i)

        possibilities = sorted(possible.keys(), key=lambda k: len(possible[k]))
        established = set()
        for f in possibilities:
            for k in established:
                possible[f].remove(possible[k][0])
            established.add(f)

        mult = 1
        for f in possible:
            if f.startswith('departure'):
                mult *= self.my_ticket[possible[f][0]]
        return mult


