import numpy as np


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            raw = f.read().strip()
        _, rem = raw.split('=', maxsplit=1)
        x_min, rem = rem.split('..', maxsplit=1)
        self.x_min = int(x_min)
        x_max, rem = rem.split(',', maxsplit=1)
        self.x_max = int(x_max)
        _, rem = rem.split('=', maxsplit=1)
        y_min, y_max = rem.split('..', maxsplit=1)
        self.y_min = int(y_min)
        self.y_max = int(y_max)

    def part1(self):
        max_top = 0
        y_target = set(range(self.y_min, self.y_max+1))
        steps = np.array([a*(a+1)/2 for a in range(1000)], dtype=int)
        for y in range(500):
            top = int(y*(y+1)/2)
            y_locs = top - steps
            target_hit = len(set(y_locs) & set(y_target)) > 0
            if target_hit and top > max_top:
                max_top = top
        return max_top

    def part2(self):
        # dx in target range and dy in target range = hit
        # Then any number of parabolic paths above that (lower dx, higher dy)
        # dy as high as 224 found in Part 1
        # dx as low as 8 (final x=36)
        # What the heck, just simulate it with smart parameters

        n_velocities = 0
        for d_x in range(8, self.x_max+1):
            for d_y in range(self.y_min, 224+1):
                dx = d_x
                dy = d_y    # if d_y < 0 else -d_y - 1
                x, y = 0, 0
                while True:
                    x += dx
                    y += dy
                    dx -= 1 if dx > 0 else 0
                    dy -= 1
                    if ((self.y_min <= y <= self.y_max)
                            and (self.x_min <= x <= self.x_max)):
                        n_velocities += 1
                        break
                    if (x > self.x_max
                            or y < self.y_min):
                        break
        return n_velocities
