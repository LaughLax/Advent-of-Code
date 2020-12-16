class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        fields, split, rem = self.input.partition('\n\n')
        fields = fields.splitlines()

        self.fields = dict()
        for f in fields:
            fname, _, nums = f.partition(': ')
            nums_1, nums_2 = nums.split(' or ')
            min_1, max_1 = nums_1.split('-')
            min_2, max_2 = nums_2.split('-')
            self.fields[fname] = tuple([int(v) for v in (min_1, max_1, min_2, max_2)])

        rem = rem.splitlines()
        self.my_ticket = tuple([int(v) for v in rem[1].split(',')])
        self.tickets = tuple(tuple([int(v) for v in line.split(',')]) for line in rem[4:])

        self.valid = set()

    def part1(self):
        allowable = set()
        minimum = 0
        maximum = 1_000_000
        for f_name in self.fields:
            f_vals = self.fields[f_name]
            if f_vals[0] < minimum:
                minimum = f_vals[0]
            if f_vals[1] < minimum:
                minimum = f_vals[1]
            if f_vals[2] > maximum:
                maximum = f_vals[2]
            if f_vals[3] > maximum:
                maximum = f_vals[3]

            for i1 in range(f_vals[0], f_vals[1]+1):
                allowable.add(i1)
            for i2 in range(f_vals[2], f_vals[3]+1):
                allowable.add(i2)

        error = 0
        for ticket in self.tickets:
            t_vals = set(ticket)
            bad = t_vals - allowable
            if len(bad) > 0:
                error += sum(bad)
            else:
                self.valid.add(ticket)

        return error

    def part2(self):
        possible = dict()
        for field in self.fields:
            possible[field] = list(range(len(self.fields)))

        for ticket in self.valid:
            for field in possible:
                to_check = possible[field]
                limits = self.fields[field]

                for i, t_val in enumerate(ticket):
                    if i in to_check:
                        if not ((limits[0] <= t_val <= limits[1])
                                or (limits[2] <= t_val <= limits[3])):
                            to_check.remove(i)

        ordered = sorted(possible.keys(), key=lambda f_name: len(possible[f_name]))
        known = set()
        prod = 1
        for f in ordered:
            for k in known:
                possible[f].remove(possible[k][0])
            known.add(f)
            if f.startswith('departure'):
                prod *= self.my_ticket[possible[f][0]]

        return prod


