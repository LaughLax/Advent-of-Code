class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        count = 0
        for line in self.input:
            good = True
            elements = line.split()
            while len(elements) > 0:
                if elements.pop() in elements:
                    good = False
                    break
            if good:
                count = count + 1

        return count

    def part2(self):
        count = 0
        for line in self.input:
            good = True
            elements = [self.count_letters(e) for e in line.split()]
            while len(elements) > 0 and good:
                current_elem = elements.pop()
                for e in elements:
                    if current_elem == e:
                        good = False
                        break
            if good:
                count = count + 1

        return count

    @staticmethod
    def count_letters(my_string):
        result = {}
        for letter in my_string:
            num = result.setdefault(letter, 0)
            result[letter] = num + 1
        return result
