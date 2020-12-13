class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.point_map = PointSet()
        for line in self.input:
            x = int(line[10:16])
            y = int(line[18:24])
            dx = int(line[36:38])
            dy = int(line[40:42])

            self.point_map.add_point(Point(x, y, dx, dy))

    def part1(self):
        t = self.point_map.min_total_distance()
        self.point_map.print(t)

        return t

    def part2(self):
        pass


class PointSet:

    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def min_total_distance(self):
        base = self.points[0]
        a = [pt.dx - base.dx for pt in self.points] + [pt.dy - base.dy for pt in self.points]
        b = [pt.x - base.x for pt in self.points] + [pt.y - base.y for pt in self.points]

        a_transpose_a = sum(i**2 for i in a)
        a_transpose_b = sum(a[i]*b[i] for i in range(len(a)))
        t = - a_transpose_b / a_transpose_a

        return int(t)

    def bounding_box(self, t):
        return (
            min(pt.get_x(t) for pt in self.points),
            min(pt.get_y(t) for pt in self.points),
            max(pt.get_x(t) for pt in self.points),
            max(pt.get_y(t) for pt in self.points),
        )

    def print(self, t):
        points = [(pt.get_x(t), pt.get_y(t)) for pt in self.points]
        bounds = self.bounding_box(t)
        # rows = [0] * (bounds[2] - bounds[0] + 1)
        for y in range(bounds[1], bounds[3] + 1):
            row = [((x, y) in points) for x in range(bounds[0], bounds[2] + 1)]
            print(''.join(['#' if i else '.' for i in row]))


class Point:

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y

        self.dx = dx
        self.dy = dy

    def get_x(self, t):
        return self.x + t * self.dx

    def get_y(self, t):
        return self.y + t * self.dy
