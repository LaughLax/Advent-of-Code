class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.map = Map()
        for line in self.input:
            self.map.add_coordinate(line)

    def part1(self):
        self.map.fill_map()
        return self.map.largest_region().area()

    def part2(self):
        return len(self.map.central_region)


class Map:

    def __init__(self):
        self.regions = set()
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
        self.biggest_region = None
        self.central_region = set()

    def add_coordinate(self, xy):
        self.regions.add(Region(xy, len(self.regions)))

    def find_region(self, x, y):
        close_sort = sorted(self.regions, key=lambda p: p.distance_to_center(x, y))
        return close_sort[0] if close_sort[0].distance_to_center(x, y) < close_sort[1].distance_to_center(x, y) else None

    def total_distance(self, x, y):
        return sum(list(map(lambda r: r.distance_to_center(x, y), self.regions)))

    def fill_map(self):
        sorted_x = sorted(self.regions, key=lambda p: p.x)
        self.min_x = sorted_x[0].x
        self.max_x = sorted_x[-1].x

        sorted_y = sorted(self.regions, key=lambda p: p.y)
        self.min_y = sorted_y[0].y
        self.max_y = sorted_y[-1].y

        for x in range(self.max_x - self.min_x + 1):
            x = x + self.min_x
            for y in range(self.max_y - self.min_y + 1):
                y = y + self.min_y

                if self.total_distance(x, y) < 10000:
                    self.central_region.add((x,y))

                region = self.find_region(x, y)
                if not region or region.border_region:
                    continue

                region.add_point(x, y)

                if (x == self.min_x
                        or x == self.max_x
                        or y == self.min_y
                        or y == self.max_y):
                    region.border_region = True

    def largest_region(self):
        if self.biggest_region:
            return self.biggest_region

        return sorted(self.regions, key=lambda r: r.area())[-1]


class Region:

    def __init__(self, xy, region_id):
        self.id = region_id

        xy = xy.split(', ')
        self.x = int(xy[0])
        self.y = int(xy[1])

        self.points = set()
        self.border_region = False

        self.furthest_distance = -1

    def distance_to_center(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def add_point(self, x, y):
        self.points.add((x, y))
        if self.distance_to_center(x, y) > self.furthest_distance:
            self.furthest_distance = self.distance_to_center(x, y)

    def area(self):
        if self.border_region:
            return -1
        else:
            return len(self.points)
