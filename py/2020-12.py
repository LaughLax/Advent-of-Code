class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.instr = [(l[0], int(l[1:])) for l in self.input]

        self.dir_map = {
            'N': 0,
            'E': 90,
            'S': 180,
            'W': 270
        }

        self.deg_to_yx = {
            0: (-1, 0),
            90: (0, 1),
            180: (1, 0),
            270: (0, -1)
        }

    def part1(self):
        pos_x = 0
        pos_y = 0
        dir_now = 90
        for char, val in self.instr:
            if char == 'L':
                dir_now = (dir_now - val) % 360
            elif char == 'R':
                dir_now = (dir_now + val) % 360
            elif char == 'F':
                yx = self.deg_to_yx[dir_now]
                pos_y += yx[0] * val
                pos_x += yx[1] * val
            else:
                yx = self.deg_to_yx[self.dir_map[char]]
                pos_y += yx[0] * val
                pos_x += yx[1] * val

        return abs(pos_x) + abs(pos_y)

    def part2(self):
        ship_x = 0
        ship_y = 0
        dx = 10
        dy = -1

        for char, val in self.instr:
            if char == 'L':
                for i in range(int(val/90)):
                    dy, dx = -dx, dy
            elif char == 'R':
                for i in range(int(val/90)):
                    dy, dx = dx, -dy
            elif char == 'F':
                ship_x += dx * val
                ship_y += dy * val
            else:
                yx = self.deg_to_yx[self.dir_map[char]]
                dy += yx[0] * val
                dx += yx[1] * val

        return abs(ship_x) + abs(ship_y)
