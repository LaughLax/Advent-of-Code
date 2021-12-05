import numpy as np
import itertools

EPS = 1e-10


class LineSeg:

    def __str__(self):
        return f"{self.x0},{self.y0} => {self.x1},{self.y1}"

    def __repr__(self):
        return f"{self.x0},{self.y0} => {self.x1},{self.y1}"

    def __init__(self, line):
        if isinstance(line, str):
            pt0, pt1 = line.split(' -> ')
            self.x0, self.y0 = list(map(int, pt0.split(',')))
            self.x1, self.y1 = list(map(int, pt1.split(',')))
        else:
            self.x0, self.y0, self.x1, self.y1 = line
        self.x_min, self.x_max = sorted([self.x0, self.x1])
        self.y_min, self.y_max = sorted([self.y0, self.y1])
        self.diag = False if ((self.x0 == self.x1) or (self.y0 == self.y1)) else True
        try:
            self.angle = np.arctan((self.y1-self.y0)/(self.x1-self.x0))
        except ZeroDivisionError:
            self.angle = np.pi/2
        self.pts = None

    def intersect_v1(self, other):
        np.abs(self.angle - other.angle)
        if np.abs(self.angle - other.angle) < EPS:
            if self.x0 == self.x1:
                # both vertical
                if (
                    self.x0 != other.x0 or
                    self.y_min > other.y_max or
                    self.y_max < other.y_min
                ):
                    return None
                return LineSeg([self.x0, max(self.y_min, other.y_min), self.x1, min(self.y_max, other.y_max)])
            elif self.y0 == self.y1:
                # both horizontal
                if (
                        self.y0 != other.y0 or
                        self.x_min > other.x_max or
                        self.x_max < other.x_min
                ):
                    return None
                return LineSeg([max(self.x_min, other.x_min), self.y0, min(self.x_max, other.x_max), self.y1])
        else:
            if self.x0 == self.x1:
                # self is vertical, other is horizontal
                if (
                    self.x0 < other.x_min or
                    self.x0 > other.x_max or
                    other.y0 < self.y_min or
                    other.y0 > self.y_max
                ):
                    return None
                return LineSeg([self.x0, other.y0, self.x0, other.y0])
            elif self.y0 == self.y1:
                # self is horizontal, other is vertical
                if (
                    self.y0 < other.y_min or
                    self.y0 > other.y_max or
                    other.x0 < self.x_min or
                    other.x0 > self.x_max
                ):
                    return None
                return LineSeg([other.x0, self.y0, other.x0, self.y0])

    def intersect_v2(self, other):
        return self.points() & other.points()

    def points(self):
        if self.pts is None:
            if (
                self.x0 == self.x1 or
                self.y0 == self.y1
            ):
                self.pts = set(itertools.product(range(self.x_min, self.x_max+1), range(self.y_min, self.y_max+1)))
            else:
                x_step = 1 if self.x1 > self.x0 else -1
                y_step = 1 if self.y1 > self.y0 else -1
                self.pts = set(zip(range(self.x0, self.x1 + x_step, x_step),
                                   range(self.y0, self.y1 + y_step, y_step)))
        return self.pts


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
        self.lines = [LineSeg(line) for line in self.input]

    def part1(self):
        straights = list(filter(lambda x: not x.diag, self.lines))
        pts = set()
        for i, line in enumerate(straights):
            for j in range(len(straights)-i-1):
                intersect = line.intersect_v1(straights[i+j+1])
                if intersect is not None:
                    pts |= intersect.points()
        return len(pts)

    def part2(self):
        pts = set()
        for i, line in enumerate(self.lines):
            for j in range(len(self.lines)-i-1):
                pts |= line.intersect_v2(self.lines[i+j+1])
        return len(pts)
