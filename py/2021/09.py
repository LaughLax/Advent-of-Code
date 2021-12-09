class Grid:
    def __init__(self, input_str):
        self.grid = {}
        self.height = len(input_str)
        self.width = len(input_str[0])

        for y in range(self.height):
            for x in range(self.width):
                self.grid[(x, y)] = Cell(self, x, y, int(input_str[y][x]))


class Cell:
    def __init__(self, grid, x, y, depth):
        self.depth = depth
        self.x = x
        self.y = y
        self.grid = grid
        self.neighbors = []

    def get_neighbors(self):
        if len(self.neighbors) > 0:
            return self.neighbors

        for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = self.x+dir[0], self.y+dir[1]
            n = self.grid.grid.get((x, y))
            if n is not None:
                self.neighbors.append(n)
        return self.neighbors

    def is_low_point(self):
        for n in self.get_neighbors():
            if n.depth <= self.depth:
                return False
        return True

    def explore_basin(self, so_far):
        if self.depth == 9:
            return frozenset()
        else:
            so_far |= frozenset([self])
            for n in self.get_neighbors():
                if n.depth == 9 or n in so_far:
                    continue
                so_far |= n.explore_basin(so_far)
            return so_far


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        state = Grid(self.input)
        total = 0
        for key in state.grid:
            if state.grid[key].is_low_point():
                total += state.grid[key].depth+1
        return total

    def part2(self):
        state = Grid(self.input)
        in_a_basin = frozenset()
        basins = []
        for y in range(len(self.input)):
            for x in range(len(self.input[0])):
                if state.grid[(x, y)] not in in_a_basin:
                    basin = state.grid[(x, y)].explore_basin(frozenset())
                    basins.append(len(basin))
                    in_a_basin |= basin
        basins = list(reversed(sorted(basins)))
        return basins[0] * basins[1] * basins[2]
