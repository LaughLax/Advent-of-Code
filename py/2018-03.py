class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
        self.claims = list(map(Claim, self.input))

    def part1(self):
        occupied_squares = set()
        for i, c1 in enumerate(self.claims):
            for c2 in self.claims[i+1:]:
                (x, y, width, height) = c1.overlap(c2)
                for x_i in range(width):
                    for y_i in range(height):
                        occupied_squares.add((x+x_i,y+y_i))

        return len(occupied_squares)

    def part2(self):
        candidates = set(self.claims)
        for i, c1 in enumerate(self.claims):
            for c2 in self.claims[i+1:]:
                (x, y, width, height) = c1.overlap(c2)
                if width and height:
                    candidates.discard(c1)
                    candidates.discard(c2)
                    continue

        return candidates.pop().id


class Claim:
    def __init__(self, claim_string):
        [id, remaining] = claim_string.split('@')
        self.id = id.strip('# ')
        x_y, width_height = remaining.split(': ')
        self.x, self.y = list(map(int, x_y.strip().split(',')))
        self.width, self.height = list(map(int, width_height.strip().split('x')))

    def overlap(self, other):
        if self.x <= other.x <= self.x + self.width:
            x = other.x
            width = min(self.x + self.width - other.x, other.width)
        elif other.x <= self.x <= other.x + other.width:
            x = self.x
            width = min(other.x + other.width - self.x, self.width)
        else:
            x = 0
            width = 0

        if self.y <= other.y <= self.y + self.height:
            y = other.y
            height = min(self.y + self.height - other.y, other.height)
        elif other.y <= self.y <= other.y + other.height:
            y = self.y
            height = min(other.y + other.height - self.y, self.height)
        else:
            y = 0
            height = 0

        return (x, y, width, height)

    def __str__(self):
        return '#{0.id} @ {0.x},{0.y}: {0.width}x{0.height}'.format(self)
