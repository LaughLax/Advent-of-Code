class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        self.grid = None

    def part1(self):
        self.grid = Grid(self.input)

        for i in range(10):
            self.grid.tick()

        return self.grid.count_trees() * self.grid.count_yards()

    def part2(self):
        self.grid = Grid(self.input)

        with open('yard_data.txt', 'w') as f:
            for i in range(2000):
                print(f'{self.grid.count_trees()}\t{self.grid.count_yards()}', file=f)
                self.grid.tick()

        return self.grid.count_trees() * self.grid.count_yards()


class Grid:

    def __init__(self, input_str):
        self.spots = {}
        self.lims = None

        for y, line in enumerate(input_str.splitlines()):
            for x, char in enumerate(line):
                if char == '#':
                    cont = 'yard'
                elif char == '|':
                    cont = 'tree'
                elif char == '.':
                    cont = 'space'
                else:
                    raise Exception(f'Unhandled character {char}')

                self.spots[(x, y)] = GridCell(x, y, cont)

        self.lims = (x+1, y+1)

        self.link_cells()

    def link_cells(self):
        for y in range(self.lims[1]):
            for x in range(self.lims[0]):
                self.spots[(x, y)].neighbors = tuple(self.spots[(i, j)] for i in range(x-1, x+2) for j in range(y-1, y+2) if 0 <= i < self.lims[0] and 0 <= j < self.lims[1] and (i, j) != (x, y))

    def print(self):
        for y in range(self.lims[1]):
            print(''.join(str(self.spots[(x, y)]) for x in range(self.lims[0])))
        print()

    def tick(self):
        for cell in self.spots.values():
            cell.find_next_contents()
        for cell in self.spots.values():
            cell.contents = cell.next_contents

    def count_trees(self):
        return sum(c.contents == 'tree' for c in self.spots.values())

    def count_yards(self):
        return sum(c.contents == 'yard' for c in self.spots.values())


class GridCell:

    def __init__(self, x, y, contents):
        self.x = x
        self.y = y

        self.contents = contents
        self.next_contents = None

        self.neighbors = None

    def find_next_contents(self):
        if self.contents == 'space':
            if sum(n.contents == 'tree' for n in self.neighbors) >= 3:
                self.next_contents = 'tree'
            else:
                self.next_contents = 'space'

        elif self.contents == 'tree':
            if sum(n.contents == 'yard' for n in self.neighbors) >= 3:
                self.next_contents = 'yard'
            else:
                self.next_contents = 'tree'

        elif self.contents == 'yard':
            if (sum(n.contents == 'yard' for n in self.neighbors) >= 1
                    and sum(n.contents == 'tree' for n in self.neighbors) >= 1):
                self.next_contents = 'yard'
            else:
                self.next_contents = 'space'

    def empty_neighbors(self):
        return [n for n in self.neighbors if not n.contents]

    def __str__(self):
        if self.contents == 'yard':
            return '#'
        elif self.contents == 'tree':
            return '|'
        else:
            return '.'

