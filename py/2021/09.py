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

    def is_low_point(self):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if ((dx == 0 and dy == 0)
                        or dx != 0 and dy != 0):
                    continue
                x, y, = self.x+dx, self.y+dy

                neighbor = self.grid.grid.get((x, y))
                if (neighbor is not None) and (neighbor.depth <= self.depth):
                    return False
        return True

    def explore_basin(self, so_far):
        if self.depth == 9:
            return frozenset()
        else:
            so_far |= frozenset([self])
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if ((dx == 0 and dy == 0)
                            or dx != 0 and dy != 0):
                        continue
                    x, y, = self.x + dx, self.y + dy

                    neighbor = self.grid.grid.get((x, y))
                    if (neighbor is None) or (neighbor.depth == 9) or (neighbor in so_far):
                        continue
                    so_far |= neighbor.explore_basin(so_far)
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
        pos = set(state.grid.keys())
        min_x = min([x[0] for x in pos])
        max_x = max([x[0] for x in pos])
        min_y = min([x[1] for x in pos])
        max_y = max([x[1] for x in pos])
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in state.grid and state.grid[(x, y)] not in in_a_basin:
                    basin = state.grid[(x, y)].explore_basin(frozenset())
                    basins.append(len(basin))
                    in_a_basin |= basin
        basins = list(reversed(sorted(basins)))
        return basins[0] * basins[1] * basins[2]
