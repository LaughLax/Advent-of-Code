class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def slope_check(self, x, y):
        row = 0
        col = 0
        trees = 0
        while row <= len(self.input) - 1:
            row += y
            if row > len(self.input) - 1:
                break
            col += x
            col %= len(self.input[0])
            if self.input[row][col] == '#':
                trees += 1
        return trees

    def part1(self):
        return self.slope_check(3, 1)

    def part2(self):
        return self.slope_check(1,1) * self.slope_check(3,1) * self.slope_check(5,1) * self.slope_check(7,1) * self.slope_check(1,2)
