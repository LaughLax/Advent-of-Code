from copy import deepcopy


class GridLayer:
    def __init__(self, depth, neighbor=None):
        self.depth = depth
        self.layer_above = None
        self.layer_below = None

        if neighbor is not None:
            assert depth != neighbor.depth
            if depth > neighbor.depth:
                self.layer_above = neighbor
                neighbor.layer_below = self
            else:
                self.layer_below = neighbor
                neighbor.layer_above = self

        self.grid = []
        for y in range(5):
            row = []
            for x in range(5):
                if y == 2 and x == 2:
                    row.append(None)
                else:
                    row.append(GridCell())
            self.grid.append(row)

        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                if y == 2 and x == 2:
                    continue

                neighbors = []
                if y > 0:
                    neighbors.append((x, y - 1))
                if y < 4:
                    neighbors.append((x, y + 1))
                if x > 0:
                    neighbors.append((x - 1, y))
                if x < 4:
                    neighbors.append((x + 1, y))

                if (2, 2) in neighbors:
                    neighbors.remove((2, 2))

                for n in neighbors:
                    self.grid[y][x].attach_neighbor(self.grid[n[1]][n[0]])

    def set_state(self, grid):
        for y in range(5):
            for x in range(5):
                if y == 2 and x == 2:
                    continue
                self.grid[y][x].bug = grid[y][x]

    def needs_layer_below(self):
        if self.layer_below is not None:
            return False

        if self.grid[1][2].bug == 1 or \
                self.grid[3][2].bug == 1 or \
                self.grid[2][1].bug == 1 or \
                self.grid[2][3].bug == 1:
            return True

    def create_layer_below(self):
        new_layer = GridLayer(self.depth + 1, self)

        # Connect cells to new neighbors
        for y in range(5):
            self.grid[2][1].attach_neighbor(new_layer.grid[y][0])
            self.grid[2][3].attach_neighbor(new_layer.grid[y][4])
        for x in range(5):
            self.grid[1][2].attach_neighbor(new_layer.grid[0][x])
            self.grid[3][2].attach_neighbor(new_layer.grid[4][x])

        return new_layer

    def needs_layer_above(self):
        if self.layer_above is not None:
            return False

        outer_rim_bugs = 0
        for y in range(5):
            outer_rim_bugs += self.grid[y][0].bug
            outer_rim_bugs += self.grid[y][4].bug
        for x in range(5):
            outer_rim_bugs += self.grid[0][x].bug
            outer_rim_bugs += self.grid[4][x].bug
        if outer_rim_bugs > 0:
            return True

    def create_layer_above(self):
        new_layer = GridLayer(self.depth - 1, self)

        # Connect cells to new neighbors
        for y in range(5):
            new_layer.grid[2][1].attach_neighbor(self.grid[y][0])
            new_layer.grid[2][3].attach_neighbor(self.grid[y][4])
        for x in range(5):
            new_layer.grid[1][2].attach_neighbor(self.grid[0][x])
            new_layer.grid[3][2].attach_neighbor(self.grid[4][x])

        return new_layer

    def prepare_next_state(self):
        for row in self.grid:
            for cell in row:
                if cell is not None:
                    cell.prepare_next_state()

    def update_state(self):
        for row in self.grid:
            for cell in row:
                if cell is not None:
                    cell.update_state()

    def count_bugs(self):
        total = 0
        for y in range(5):
            for x in range(5):
                if y == 2 and x == 2:
                    continue
                total += self.grid[y][x].bug
        return total

    def print(self):
        my_str = f'Layer at depth {self.depth}\n'
        for y in range(5):
            for x in range(5):
                if y == 2 and x == 2:
                    my_str += '?'
                else:
                    my_str += '#' if self.grid[y][x].bug else '.'
            my_str += '\n'
        print(my_str + '\n')



class GridCell:
    def __init__(self):
        self.bug = 0
        self.neighbors = set()
        self.next_state = None

    def attach_neighbor(self, other_cell):
        self.neighbors.add(other_cell)
        other_cell.neighbors.add(self)

    def prepare_next_state(self):
        live_neighbors = sum([n.bug for n in self.neighbors])
        if live_neighbors == 0 or live_neighbors > 2:
            self.next_state = 0
        elif live_neighbors == 1:
            self.next_state = 1
        elif live_neighbors == 2:
            self.next_state = 1 - self.bug

    def update_state(self):
        self.bug = self.next_state
        self.next_state = None


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.init_state = []
        for line in self.input:
            l = []
            for c in line:
                if c == '#':
                    l.append(1)
                else:
                    l.append(0)
            self.init_state.append(l)

    def serialize_state(self, grid):
        return tuple(tuple(line) for line in grid)

    def advance_state(self, grid):
        new_grid = deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid)):
                neighbors = []
                if y > 0:
                    neighbors.append((x, y - 1))
                if y < 4:
                    neighbors.append((x, y + 1))
                if x > 0:
                    neighbors.append((x - 1, y))
                if x < 4:
                    neighbors.append((x + 1, y))

                # print(grid)
                # print(neighbors)
                # print([grid[n[1]][n[0]] for n in neighbors])
                live_neighbors = sum([grid[n[1]][n[0]] for n in neighbors])
                # print(live_neighbors)
                if live_neighbors == 0 or live_neighbors > 2:
                    new_grid[y][x] = 0
                elif live_neighbors == 1:
                    new_grid[y][x] = 1
                elif live_neighbors == 2:
                    new_grid[y][x] = 1 - grid[y][x]
                else:
                    print('Error counting live neighbors')
        return new_grid

    def biodiversity(self, grid):
        total = 0
        val = 1
        for line in grid:
            for space in line:
                total += val if space == 1 else 0
                val *= 2
        return total

    def my_print(self, grid):
        my_str = ''
        for line in grid:
            for val in line:
                if val == 1:
                    my_str += '#'
                else:
                    my_str += '.'
            my_str += '\n'
        my_str += '\n'
        print(my_str)

    def part1(self):
        grid = deepcopy(self.init_state)
        # print(grid)
        # self.my_print(grid)
        states = set()
        states.add(self.serialize_state(grid))

        while True:
            grid = self.advance_state(grid)
            # self.my_print(grid)
            state = self.serialize_state(grid)
            if state in states:
                # print(state)
                return self.biodiversity(state)
            else:
                states.add(state)

    def part2(self):
        layers = [GridLayer(0)]
        layers[0].set_state(self.init_state)
        # layers[0].print()

        t = 0
        while t < 200:
            for layer in layers:
                if layer.needs_layer_above():
                    # print(f'Creating layer at depth {layer.depth - 1}')
                    layers.append(layer.create_layer_above())
                if layer.needs_layer_below():
                    # print(f'Creating layer at depth {layer.depth + 1}')
                    layers.append(layer.create_layer_below())
            for layer in layers:
                layer.prepare_next_state()
            for layer in layers:
                layer.update_state()
            t += 1

        # layers.sort(key=lambda l: l.depth)
        # for layer in layers:
        #     layer.print()

        return sum([l.count_bugs() for l in layers])
