class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.black = set()
        self.d = {
            'nw': (0, -1),
            'ne': (1, -1),
            'e': (1, 0),
            'se': (0, 1),
            'sw': (-1, 1),
            'w': (-1, 0)
        }

    def part1(self):
        dirs = [line.replace('e', 'e,').replace('w', 'w,') for line in self.input]

        self.black.clear()
        for line in dirs:
            x, y = 0, 0
            for v in line.split(',')[:-1]:
                v_d = self.d[v]
                x += v_d[0]
                y += v_d[1]
            if (x, y) in self.black:
                self.black.remove((x, y))
            else:
                self.black.add((x, y))

        return len(self.black)

    def part2(self):
        black = set(self.black)
        neigh_black = {}

        for t in range(100):
            neigh_black.clear()
            for tile in black:
                for d in self.d.values():
                    x = tile[0] + d[0]
                    y = tile[1] + d[1]
                    neigh_black[tile] = neigh_black.setdefault((x, y), 0) + 1

            for tile in set(black):
                if tile not in neigh_black.keys():
                    black.remove(tile)

            for tile, num in neigh_black.items():
                if tile in black:
                    if num > 2:
                        black.remove(tile)
                else:
                    if num == 2:
                        black.add(tile)

        return len(black)
