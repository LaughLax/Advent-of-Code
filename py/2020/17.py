class Grid1:
    def __init__(self, input_str):
        self.grid = {}
        self.height = len(input_str)
        self.width = len(input_str[0])

        for y in range(self.height):
            for x in range(self.width):
                if input_str[y][x] == '#':
                    self.grid[(x, y, 0)] = Cell1(self, x, y, 0, True)
                elif input_str[y][x] == '.':
                    self.grid[(x, y, 0)] = Cell1(self, x, y, 0, False)

        for key in set(self.grid.keys()):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for dz in (-1, 0, 1):
                        x, y, z = key[0]+dx, key[1]+dy, key[2]+dz
                        if (x, y, z) not in self.grid:
                            self.grid[(x, y, z)] = Cell1(self, x, y, z, False)

    def reset_state(self, part2):
        for pos in self.grid:
            c = self.grid[pos]
            c.occupied = False
            if not part2:
                c.neighbors = c.neighbors_split[0]
            else:
                c.neighbors = c.neighbors_split[0] | c.neighbors_split[1]
        self.static.clear()

    def tick(self):
        to_tick = set(self.grid.keys())
        changed = set()
        for pos in to_tick:
            if self.grid[pos].prep_tick():
                changed.add(pos)
        for pos in changed:
            self.grid[pos].do_tick()

        return len(changed) > 0

    def count_active(self):
        return sum([self.grid[pos].active for pos in self.grid])

    def print(self):
        output = []
        pos = set(self.grid.keys())
        min_x = min([x[0] for x in pos])
        max_x = max([x[0] for x in pos])
        min_y = min([x[1] for x in pos])
        max_y = max([x[1] for x in pos])
        min_z = min([x[2] for x in pos])
        max_z = max([x[2] for x in pos])
        for z in range(min_z, max_z+1):
            output.append(f'z={z}')
            for y in range(min_y, max_y+1):
                row = []
                for x in range(min_x, max_x+1):
                    if (x, y, z) in self.grid:
                        row.append('#' if self.grid[(x, y, z)].active else '.')
                    else:
                        row.append('.')
                output.append(row)
            output.append('\n')
        print('\n'.join([''.join(line) for line in output]))


class Cell1:
    def __init__(self, grid, x, y, z, active):
        self.active = active
        self.x = x
        self.y = y
        self.z = z
        self.next_state = False
        self.grid = grid

    def make_neighbors(self):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    x, y, z = self.x+dx, self.y+dy, self.z+dz

                    if (x, y, z) not in self.grid.grid:
                        self.grid.grid[(x, y, z)] = Cell1(self.grid, x, y, z, False)

    def prep_tick(self):
        occ = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    x, y, z = self.x+dx, self.y+dy, self.z+dz
                    if (x, y, z) in self.grid.grid:
                        if self.grid.grid[(x, y, z)].active:
                            occ += 1
                    if occ > 3:
                        break
                if occ > 3:
                    break
            if occ > 3:
                break

        if self.active and (occ not in (2, 3)):
            self.next_state = False
            return True

        if (not self.active) and (occ == 3):
            self.next_state = True
            self.make_neighbors()
            return True

        return False

    def do_tick(self):
        self.active = self.next_state


class Grid2:
    def __init__(self, input_str):
        self.grid = {}
        self.height = len(input_str)
        self.width = len(input_str[0])

        for y in range(self.height):
            for x in range(self.width):
                if input_str[y][x] == '#':
                    self.grid[(x, y, 0, 0)] = Cell2(self, x, y, 0, 0, True)
                elif input_str[y][x] == '.':
                    self.grid[(x, y, 0, 0)] = Cell2(self, x, y, 0, 0, False)

        for key in set(self.grid.keys()):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for dz in (-1, 0, 1):
                        for dw in (-1, 0, 1):
                            x, y, z, w = key[0]+dx, key[1]+dy, key[2]+dz, key[3]+dw
                            if (x, y, z, w) not in self.grid:
                                self.grid[(x, y, z, w)] = Cell2(self, x, y, z, w, False)

    def reset_state(self, part2):
        for pos in self.grid:
            c = self.grid[pos]
            c.occupied = False
            if not part2:
                c.neighbors = c.neighbors_split[0]
            else:
                c.neighbors = c.neighbors_split[0] | c.neighbors_split[1]
        self.static.clear()

    def tick(self):
        to_tick = set(self.grid.keys())
        changed = set()
        for pos in to_tick:
            if self.grid[pos].prep_tick():
                changed.add(pos)
        for pos in changed:
            self.grid[pos].do_tick()

        return len(changed) > 0

    def count_active(self):
        return sum([self.grid[pos].active for pos in self.grid])

    def print(self):
        output = []
        pos = set(self.grid.keys())
        min_x = min([x[0] for x in pos])
        max_x = max([x[0] for x in pos])
        min_y = min([x[1] for x in pos])
        max_y = max([x[1] for x in pos])
        min_z = min([x[2] for x in pos])
        max_z = max([x[2] for x in pos])
        min_w = min([x[3] for x in pos])
        max_w = max([x[3] for x in pos])
        for w in range(min_w, max_w+1):
            for z in range(min_z, max_z+1):
                output.append(f'z={z}, w={w}')
                for y in range(min_y, max_y+1):
                    row = []
                    for x in range(min_x, max_x+1):
                        if (x, y, z) in self.grid:
                            row.append('#' if self.grid[(x, y, z, w)].active else '.')
                        else:
                            row.append('.')
                    output.append(row)
                output.append('\n')
        print('\n'.join([''.join(line) for line in output]))


class Cell2:
    def __init__(self, grid, x, y, z, w, active):
        self.active = active
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.next_state = False
        self.grid = grid

    def make_neighbors(self):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for dw in (-1, 0, 1):
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        x, y, z, w = self.x+dx, self.y+dy, self.z+dz, self.w+dw

                        if (x, y, z, w) not in self.grid.grid:
                            self.grid.grid[(x, y, z, w)] = Cell2(self.grid, x, y, z, w, False)

    def prep_tick(self):
        occ = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for dw in (-1, 0, 1):
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        x, y, z, w = self.x+dx, self.y+dy, self.z+dz, self.w+dw
                        if (x, y, z, w) in self.grid.grid:
                            if self.grid.grid[(x, y, z, w)].active:
                                occ += 1
                        if occ > 3:
                            break
                    if occ > 3:
                        break
                if occ > 3:
                    break
            if occ > 3:
                break

        if self.active and (occ not in (2, 3)):
            self.next_state = False
            return True

        if (not self.active) and (occ == 3):
            self.next_state = True
            self.make_neighbors()
            return True

        return False

    def do_tick(self):
        self.active = self.next_state


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        state = Grid1(self.input)
        for i in range(6):
            state.tick()
        return state.count_active()

    def part2(self):
        state = Grid2(self.input)
        for i in range(6):
            state.tick()
        return state.count_active()
