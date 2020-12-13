import math


class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = int(f.read().strip())

    def part1(self):
        ring = math.ceil((math.sqrt(self.input) - 1) / 2)
        rotation = self.input - (4*ring**2 - 3*ring + 1) # Steps CW along the ring to 0 radians
        rotation = rotation % (2*ring) # Steps CW along the ring to 0, pi/2, pi, or 3pi/2 radians
        rotation = rotation if rotation < ring else 2*ring - rotation # Allow CCW steps if closer

        return ring + rotation

    def part2(self):
        spiral = SpiralMaker()
        while spiral.take_a_step() < self.input:
            pass
        return spiral.current_value()


class SpiralMaker:
    def __init__(self):
        self.landscape = {(0,0): 1}
        self.pos = (0,0)
        self.dir = 3

    def left(self):
        return (self.dir + 1) % 4

    @staticmethod
    def square_ahead(pos, dir):
        if dir == 0:
            return pos[0]+1, pos[1]
        elif dir == 1:
            return pos[0], pos[1]+1
        elif dir == 2:
            return pos[0]-1, pos[1]
        else:
            return pos[0], pos[1]-1

    def get_next_square_position(self):
        if self.square_ahead(self.pos, self.left()) not in self.landscape:
            self.dir = self.left()

        return self.square_ahead(self.pos, self.dir)

    def square_value(self, pos):
        sum = 0
        for x in (-1,0,1):
            for y in (-1,0,1):
                sum = sum + self.landscape.get((pos[0] + x, pos[1] + y), 0)

        return sum

    def take_a_step(self):
        new_pos = self.get_next_square_position()
        new_val = self.square_value(new_pos)

        self.pos = new_pos
        self.landscape[new_pos] = new_val

        return new_val

    def current_value(self):
        return self.landscape[self.pos]

    def __str__(self):
        min_y = min([t[1] for t in self.landscape])
        max_y = max([t[1] for t in self.landscape])
        min_x = min([t[0] for t in self.landscape])
        max_x = max([t[0] for t in self.landscape])

        rows = []
        y = max_y
        while y >= min_y:
            row = []
            x = min_x
            while x <= max_x:
                if (x, y) in self.landscape:
                    row.append(f'{self.landscape[(x, y)]}')
                else:
                    row.append('')

                x = x + 1

            rows.append('\t'.join(row))

            y = y - 1

        return '\n'.join(rows)
