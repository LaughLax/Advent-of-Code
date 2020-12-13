class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().split('\n\n')

        self.passports = []
        for line_set in self.input:
            line_set = line_set.replace('\n', ' ').strip()
            data = line_set.split(' ')
            pp = dict()
            for d in data:
                d = d.split(':')
                pp[d[0]] = d[1]
            self.passports.append(pp)

    def part1(self):
        valid = 0
        for pp in self.passports:
            v = True
            keys = pp.keys()
            for att in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
                if att not in keys:
                    v = False
                    break
            if v:
                valid += 1
        return valid

    def part2(self):
        valid = 0
        for pp in self.passports:

            cont = False
            for att in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
                if att not in pp.keys():
                    cont = True
                    break
            if cont:
                continue

            if not (1920 <= int(pp['byr']) <= 2002):
                continue
            if not (2010 <= int(pp['iyr']) <= 2020):
                continue
            if not (2020 <= int(pp['eyr']) <= 2030):
                continue

            if pp['hgt'][-2:] == 'cm':
                if not (150 <= int(pp['hgt'][:-2]) <= 193):
                    continue
            elif pp['hgt'][-2:] == 'in':
                if not (59 <= int(pp['hgt'][:-2]) <= 76):
                    continue
            else:
                continue

            if len(pp['hcl']) != 7:
                continue
            if pp['hcl'][0] != '#':
                continue
            for i in range(6):
                if pp['hcl'][i+1] not in '0123456789abcdef':
                    continue

            if pp['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue

            if len(pp['pid']) != 9:
                continue

            valid += 1
        return valid
