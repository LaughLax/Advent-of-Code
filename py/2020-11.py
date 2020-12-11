class Grid:
    def __init__(self, input_str):
        self.grid = {}
        self.height = len(input_str)
        self.width = len(input_str[0])

        for y in range(self.height):
            for x in range(self.width):
                if input_str[y][x] == 'L':
                    self.grid[(y, x)] = Chair()

        self.pos = frozenset(self.grid.keys())
        self.static = set()

    def link_neighbors(self):
        for pos in self.grid:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue

                    y = pos[0] + dy
                    x = pos[1] + dx
                    k = 1
                    
                    while 0 <= y < self.height \
                          and 0 <= x < self.width:

                        if (y, x) in self.grid:
                            self.grid[pos].attach_neighbor(self.grid[(y, x)], k>1)
                            break

                        y += dy
                        x += dx
                        k += 1
                        

    def reset_state(self, part2):
        for pos in self.grid:
            c = self.grid[pos]
            c.occupied = False
            if not part2:
                c.neighbors = c.neighbors_split[0]
            else:
                c.neighbors = c.neighbors_split[0] | c.neighbors_split[1]
        self.static.clear()

    def tick(self, empty_threshold):
        to_tick = self.pos - self.static
        for pos in to_tick:
            if not self.grid[pos].prep_tick(empty_threshold):
                self.static.add(pos)
        for pos in to_tick:
            self.grid[pos].do_tick()

        return len(self.pos) != len(self.static)

    def count_occ(self):
        return sum([self.grid[pos].occupied for pos in self.grid])

    def print(self):
        outpt = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if (y, x) in self.grid:
                    row.append('#' if self.grid[(y,x)].occupied else 'L')
                else:
                    row.append('.')
            outpt.append(row)
        print('\n'.join([''.join(l) for l in outpt]))


class Chair:
    def __init__(self):
        self.occupied = False
        self.neighbors_split = (set(), set())
        self.neighbors = set()
        self.next_state = False

    def attach_neighbor(self, other_cell, far):
        sel = 1 if far else 0
        self.neighbors_split[sel].add(other_cell)
        other_cell.neighbors_split[sel].add(self)

    def prep_tick(self, empty_threshold):
        occ_neighbors = sum([n.occupied for n in self.neighbors])
        if not self.occupied and occ_neighbors == 0:
            self.next_state = True
            return True
        if self.occupied and occ_neighbors >= empty_threshold:
            self.next_state = False
            return True
        return False

    def do_tick(self):
        self.occupied = self.next_state


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.state = Grid(self.input)
        self.state.link_neighbors()

    def part1(self):
        self.state.reset_state(False)
        while self.state.tick(4):
            pass
        return self.state.count_occ()


    def part2(self):
        self.state.reset_state(True)
        while self.state.tick(5):
            pass
        return self.state.count_occ()
