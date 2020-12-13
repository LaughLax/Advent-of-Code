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
        self.map.build_central_region()
        return len(self.map.central_region)


class Map:

    def __init__(self):
        self.regions = []
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
        self.biggest_region = None
        self.central_region = set()

    def add_coordinate(self, xy):
        self.regions.append(Region(xy, len(self.regions)))

    def find_region(self, x, y):
        distances = [(x - r.x if x > r.x else r.x - x) + (y - r.y if y > r.y else r.y - y) for r in self.regions]

        d = min(distances)
        return self.regions[distances.index(d)] if distances.count(d) == 1 else None

    def total_distance(self, x, y):
        return sum(list(map(lambda r: r.distance_to_center(x, y), self.regions)))

    def find_bounding_box(self):
        self.min_x = float('inf')
        self.max_x = 0
        self.min_y = float('inf')
        self.max_y = 0

        for r in self.regions:
            self.min_x = self.min_x if self.min_x < r.x else r.x
            self.max_x = self.max_x if self.max_x > r.x else r.x

            self.min_y = self.min_y if self.min_y < r.y else r.y
            self.max_y = self.max_y if self.max_y > r.y else r.y

    def fill_map(self):
        if self.min_x is None:
            self.find_bounding_box()

        for x in range(self.min_x+1, self.max_x):
            for y in range(self.min_y+1, self.max_y):

                region = self.find_region(x, y)
                if region:
                    region.add_point(x, y)

        for y in range(self.min_y, self.max_y + 1):
            for x in [self.min_x, self.max_x]:
                region = self.find_region(x, y)
                if region:
                    region.border_region = True

        for x in range(self.min_x, self.max_x + 1):
            for y in [self.min_y, self.max_y]:
                region = self.find_region(x, y)
                if region:
                    region.border_region = True

    def build_central_region(self):
        if self.min_x is None:
            self.find_bounding_box()

        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):

                if self.total_distance(x, y) < 10000:
                    self.central_region.add((x, y))

    def largest_region(self):
        if not self.biggest_region:
            self.biggest_region = self.regions[0]
            for r in self.regions:
                self.biggest_region = self.biggest_region if self.biggest_region.area() > r.area() else r

        return self.biggest_region


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
        return (x - self.x if x > self.x else self.x - x) + (y - self.y if y > self.y else self.y - y)

    def add_point(self, x, y):
        self.points.add((x, y))

    def area(self):
        if self.border_region:
            return -1
        else:
            return len(self.points)
