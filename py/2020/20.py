from copy import copy


def rotate_str(string, n):
    for _ in range(n):
        lines = string.splitlines()
        string = '\n'.join([''.join([line[i] for line in lines][::-1]) for i in range(len(lines))])
    return string


def flip_str(string, fixed_side):
    lines = string.splitlines()
    new_lines = [[None] * len(lines) for _ in lines]
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            new_lines[i][j] = lines[j][i]
            new_lines[j][i] = lines[i][j]

    flipped = '\n'.join([''.join([ch for ch in line]) for line in new_lines])
    return rotate_str(flipped, 1 + 2 * (fixed_side % 2))


class Tile:
    def __init__(self, name, data_str):
        self.id = name
        self.orig = data_str
        self.raw = data_str

        self.borders = []
        self.neighbors = [None] * 4
        self.n_flip = [False, False, False, False]
        self.rotated = False
        self.flipped = False

        self.pt1_neighbors = []
        self.pt1_n_flip = []

        self.reset_pt2()

    def reset_pt1(self):
        self.neighbors = [None] * 4
        self.n_flip = [False, False, False, False]

    def store_pt1(self):
        self.pt1_neighbors = self.neighbors.copy()
        self.pt1_n_flip = self.n_flip.copy()

    def reset_pt2(self):
        self.raw = self.orig

        lines = self.raw.splitlines()
        self.borders = []
        self.borders.append(lines[0])
        self.borders.append(''.join([line[-1] for line in lines]))
        self.borders.append(''.join(lines[-1][::-1]))
        self.borders.append(''.join([line[0] for line in lines][::-1]))

        self.neighbors = self.pt1_neighbors.copy()
        self.n_flip = self.pt1_n_flip.copy()

        self.rotated = False
        self.flipped = False

    def num_neighb(self):
        return sum([1 if n is not None else 0 for n in self.neighbors])

    def set_neighb(self, direction, other, other_dir, flip):
        assert self.neighbors[direction] is other or self.neighbors[direction] is None
        assert other.neighbors[other_dir] is self or other.neighbors[other_dir] is None

        self.neighbors[direction] = other
        self.n_flip[direction] = flip
        other.neighbors[other_dir] = self
        other.n_flip[other_dir] = flip

    def _rot(self, n):
        for i in range(4-n):
            self.borders.append(self.borders.pop(0))
            self.neighbors.append(self.neighbors.pop(0))
            self.n_flip.append(self.n_flip.pop(0))

    def rotate(self, n):
        assert not self.rotated
        self._rot(n)
        for i in range(n):
            self.raw = rotate_str(self.raw, n)
        self.rotated = True

    def _flip(self, fixed_side):
        self.borders = [b[::-1] for b in self.borders[::-1]]
        self.neighbors = self.neighbors[::-1]
        self.n_flip = [not n for n in self.n_flip[::-1]]
        for n in self.neighbors:
            if n is not None:
                n.n_flip[n.neighbors.index(self)] = not n.n_flip[n.neighbors.index(self)]

        self.raw = flip_str(self.raw, fixed_side)
        self._rot(1 + 2 * (fixed_side % 2))

    def flip(self, fixed_side):
        assert not self.flipped
        self._flip(fixed_side)
        self.flipped = True

    def to_string(self):
        return copy(self.raw)


def monster_tiles(string):
    mon_coords = ((18, 0),
                  (0, 1),
                  (5, 1),
                  (6, 1),
                  (11, 1),
                  (12, 1),
                  (17, 1),
                  (18, 1),
                  (19, 1),
                  (1, 2),
                  (4, 2),
                  (7, 2),
                  (10, 2),
                  (13, 2),
                  (16, 2),
                  )
    confirmed_coords = set()
    lines = string.splitlines()
    for x in range(len(lines[0]) - 19):
        for y in range(len(lines) - 2):
            maybe_coords = set()
            for d in mon_coords:
                x2 = x+d[0]
                y2 = y+d[1]
                if lines[y2][x2] == '#':
                    maybe_coords.add((x2, y2))
                else:
                    break
            if len(maybe_coords) == len(mon_coords):
                confirmed_coords |= maybe_coords

    return confirmed_coords


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        tiles_str = self.input.split('\n\n')
        self.tiles = []
        for t in tiles_str:
            tile_id = int(t[5:9])
            _, _, lines = t.partition('\n')
            self.tiles.append(Tile(tile_id, lines))

    def part1(self):
        for t in self.tiles:
            t.reset_pt1()

        for tile1 in self.tiles:
            for i in range(4):
                if tile1.neighbors[i] is None:
                    for tile2 in self.tiles:
                        if tile1 is tile2:
                            continue
                        for j in range(4):
                            if tile2.neighbors[j] is None:
                                if tile1.borders[i] == tile2.borders[j][::-1]:
                                    tile1.set_neighb(i, tile2, j, False)
                                elif tile1.borders[i] == tile2.borders[j]:
                                    tile1.set_neighb(i, tile2, j, True)

        count = 0
        mult = 1
        for t in self.tiles:
            count += 1 if t.num_neighb() == 2 else 0
            mult *= t.id if t.num_neighb() == 2 else 1
        assert count == 4

        for t in self.tiles:
            t.store_pt1()

        return mult

    def part2(self):
        for t in self.tiles:
            t.reset_pt2()

        dirs = {
            0: (0, -1),
            1: (1, 0),
            2: (0, 1),
            3: (-1, 0)
        }

        grid = {}
        min_x = 999
        max_x = -999
        min_y = 999
        max_y = -999
        explored = set()
        to_explore = {(self.tiles[0], 0, 0)}
        while len(to_explore) > 0:
            t, x, y = to_explore.pop()
            grid[x, y] = t
            for i, n in enumerate(t.neighbors):
                if n is None or n in explored:
                    continue

                d = dirs[i]
                x2 = x + d[0]
                y2 = y + d[1]

                rot = (i - n.neighbors.index(t) + 2) % 4
                if rot > 0:
                    n.rotate(rot)
                if t.n_flip[i]:
                    n.flip(n.neighbors.index(t))

                to_explore.add((n, x2, y2))

                min_x = min(x2, min_x)
                max_x = max(x2, max_x)
                min_y = min(y2, min_y)
                max_y = max(y2, max_y)

            explored.add(t)

        t_grid = []
        for y in range(min_y, max_y+1):
            tile_row = []
            for x in range(min_x, max_x + 1):
                tile_row.append(grid[(x, y)].to_string())
            t_grid.append(tile_row)
        t_size = len(t_grid[0][0].splitlines())

        joined_list = []
        for t_row in t_grid:
            t_row_str = '\n'.join([''.join([t_str.splitlines()[i][1:-1] for t_str in t_row]) for i in range(1, t_size-1)])
            joined_list.append(t_row_str)
        joined_str = '\n'.join(joined_list)

        test_str = copy(joined_str)
        found = False
        for _ in range(4):
            m_tiles = monster_tiles(test_str)
            if len(m_tiles) > 0:
                found = True
                break
            test_str = rotate_str(test_str, 1)

        if not found:
            test_str = flip_str(test_str, 0)
            for _ in range(4):
                m_tiles = monster_tiles(test_str)
                if len(m_tiles) > 0:
                    found = True
                    break
                test_str = rotate_str(test_str, 1)

        assert found
        return test_str.count('#') - len(m_tiles)
