class Grid:
    def __init__(self, input_str):
        self.grid = {}
        self.height = len(input_str)
        self.width = len(input_str[0])

        for y in range(self.height):
            for x in range(self.width):
                self.grid[(x, y)] = Cell(self, x, y, int(input_str[y][x]))

    def tick(self):
        flashed = 0
        for octo in self.grid.values():
            octo.energy_up()
        for octo in self.grid.values():
            if octo.flashed:
                flashed += 1
                octo.energy = 0
                octo.flashed = False
        return flashed

    def print(self):
        full = []
        for y in range(self.height):
            line = ''.join(str(self.grid[(x, y)].energy) for x in range(self.width))
            full.append(line)
        print('\n'.join(full))


class Cell:
    def __init__(self, grid, x, y, energy):
        self.energy = energy
        self.x = x
        self.y = y
        self.grid = grid
        self.flashed = False
        self._neighbors = None

    def neighbors(self):
        if self._neighbors is not None:
            return self._neighbors

        self._neighbors = []
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if (dx, dy) == (0, 0):
                    continue
                x, y = self.x+dx, self.y+dy
                n = self.grid.grid.get((x, y))
                if n is not None:
                    self._neighbors.append(n)
        return self._neighbors

    def energy_up(self):
        self.energy += 1
        if self.energy > 9 and not self.flashed:
            self.flash()

    def flash(self):
        self.flashed = True
        for n in self.neighbors():
            if not n.flashed:
                n.energy_up()


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        grid = Grid(self.input)
        total = 0
        for _ in range(100):
            flashed = grid.tick()
            total += flashed
        return total

    def part2(self):
        grid = Grid(self.input)
        goal = len(self.input) * len(self.input[0])
        i = 0
        while True:
            i += 1
            flashed = grid.tick()
            if flashed == goal:
                return i
