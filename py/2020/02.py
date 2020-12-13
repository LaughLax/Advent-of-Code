class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        count = 0
        for line in self.input:
            [policy_min, remainder] = line.split('-')
            policy_min = int(policy_min)
            [policy_max, letter, password] = remainder.split(' ')
            policy_max = int(policy_max)
            letter = letter[0]
            if policy_min <= password.count(letter) <= policy_max:
                count += 1
        return count

    def part2(self):
        count = 0
        for line in self.input:
            [num_1, remainder] = line.split('-')
            num_1 = int(num_1)
            [num_2, letter, password] = remainder.split(' ')
            num_2 = int(num_2)
            letter = letter[0]

            if (password[num_1-1] == letter) ^ (password[num_2-1] == letter):
                count += 1

        return count
