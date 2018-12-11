import copy


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.serial = int(f.read())

        self.grid = {}

    def get_power(self, x, y):
        return int( ( ( (x+10)*y + self.serial) * (x+10) % 1000) / 100) - 5

    def build_grid(self):
        for x in range(1, 301):
            for y in range(1, 301):
                self.grid[(x, y)] = self.get_power(x, y)

    def integrate_grid(self, size):
        new_grid = {}
        for x in range(1, 299):
            for y in range(1, 299):
                new_grid[(x, y)] = (self.grid[(x, y)]
                                    + self.grid[(x+1, y)]
                                    + self.grid[(x+2, y)]
                                    + self.grid[(x, y+1)]
                                    + self.grid[(x+1, y+1)]
                                    + self.grid[(x+2, y+1)]
                                    + self.grid[(x, y+2)]
                                    + self.grid[(x+1, y+2)]
                                    + self.grid[(x+2, y+2)])

        return new_grid

    def part1(self):
        self.build_grid()
        integrated = self.integrate_grid(3)

        max_key = None
        max_val = -float('inf')
        for key, val in self.grid.items():
            if val > max_val:
                max_val = val
                max_key = key
        print(max_key)

        max_key = None
        max_val = -float('inf')
        for key, val in integrated.items():
            if val > max_val:
                max_val = val
                max_key = key
        print(max_key)
        return max_key

    def part2(self):
        grid = Grid(self.grid, 300, 300)

        print(grid.max_loc)
        grid.expand()
        grid.expand()
        print(grid.max_loc)
        
        while grid.size < 300:
            print(grid.size)
            grid.expand()

        return grid.max_loc


class Grid:

    def __init__(self, base_grid, width, height):
        self.orig = [[base_grid[(x, y)] for y in range(1, height+1)] for x in range(1, width+1)]
        self.vals = copy.deepcopy(self.orig)
        
        self.size = 1

        self.max_val = -float('inf')
        self.max_loc = (-1, -1, -1)
        for x, col in enumerate(self.vals):
            for y, val in enumerate(col):
                if val > self.max_val:
                    self.max_val = val
                    self.max_loc = (x+1, y+1, 1)

    def expand(self):
        self.size += 1
        self.vals.pop()
        for col in self.vals:
            col.pop()

        for y in range(len(self.vals[0])):
            for x in range(len(self.vals)):
                for y_add in range(y, y + self.size - 1):
                    self.vals[x][y] += self.orig[x + self.size - 1][y_add]
                for x_add in range(x, x + self.size):
                    self.vals[x][y] += self.orig[x_add][y + self.size - 1]

        max_col_val = [max(col) for col in self.vals]
        max_val = max(max_col_val)
        if max_val > self.max_val:
            self.max_val = max_val

            max_x = max_col_val.index(max_val)
            max_y = self.vals[max_x].index(max(self.vals[max_x]))
            self.max_loc = (max_x+1, max_y+1, self.size)

    def max_value(self):
        return self.max_loc
