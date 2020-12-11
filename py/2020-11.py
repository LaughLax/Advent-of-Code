from copy import deepcopy


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

        self.t = 0

    def link_neighbors_pt1(self):
        for pos in self.grid:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue

                    if (pos[0]+dy, pos[1]+dx) in self.grid:
                        self.grid[pos].attach_neighbor(self.grid[(pos[0]+dy, pos[1]+dx)])

    def link_neighbors_pt2(self):
        for pos in self.grid:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue

                    y = pos[0] + dy
                    x = pos[1] + dx
                    
                    while 0 <= y < self.height \
                          and 0 <= x < self.width:

                        if (y, x) in self.grid:
                            self.grid[pos].attach_neighbor(self.grid[(y, x)])
                            break

                        y += dy
                        x += dx
                        

    def reset_state(self):
        for pos in self.grid:
            self.grid[pos].occupied = False

    def tick(self, empty_threshold):
        self.t += 1
        
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
        self.neighbors = set()
        self.next_state = False

    def attach_neighbor(self, other_cell):
        self.neighbors.add(other_cell)
        other_cell.neighbors.add(self)

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

    def part1(self):
        state = Grid(self.input)
        state.link_neighbors_pt1()
        while state.tick(4):
            pass
        return state.count_occ()


    def part2(self):
        state = Grid(self.input)
        state.link_neighbors_pt2()
        while state.tick(5):
            pass
        return state.count_occ()
