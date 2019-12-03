import numpy as np

class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
            self.line1 = self.input[0].split(',')
            self.line2 = self.input[1].split(',')

    def part1(self):
        x = 0
        y = 0
        xdest = 0
        ydest = 0
        self.line1_segs = []
        for dir in self.line1:
            if dir[0] == 'R':
                xdest = x + int(dir[1:])
            elif dir[0] == 'D':
                ydest = y - int(dir[1:])
            elif dir[0] == 'L':
                xdest = x - int(dir[1:])
            elif dir[0] == 'U':
                ydest = y + int(dir[1:])
            self.line1_segs.append((x,y,xdest,ydest))
            x = xdest
            y = ydest

        x = 0
        y = 0
        xdest = 0
        ydest = 0
        self.line2_segs = []
        self.inters = []
        for dir in self.line2:
            if dir[0] == 'R':
                xdest = x + int(dir[1:])
                for seg in self.line1_segs:
                    if seg[0] == seg[2] and \
                            np.sign(x - seg[0]) != np.sign(xdest - seg[0]) and \
                            np.sign(y - seg[1]) != np.sign(y - seg[3]):
                        self.inters.append((seg[0], y))
            elif dir[0] == 'D':
                ydest = y - int(dir[1:])
                for seg in self.line1_segs:
                    if seg[1] == seg[3] and \
                            np.sign(x - seg[0]) != np.sign(x - seg[2]) and \
                            np.sign(y - seg[1]) != np.sign(ydest - seg[1]):
                        self.inters.append((x, seg[1]))
            elif dir[0] == 'L':
                xdest = x - int(dir[1:])
                for seg in self.line1_segs:
                    if seg[0] == seg[2] and \
                            np.sign(x - seg[0]) != np.sign(xdest - seg[0]) and \
                            np.sign(y - seg[1]) != np.sign(y - seg[3]):
                        self.inters.append((seg[0], y))
            elif dir[0] == 'U':
                ydest = y + int(dir[1:])
                for seg in self.line1_segs:
                    if seg[1] == seg[3] and \
                            np.sign(x - seg[0]) != np.sign(x - seg[2]) and \
                            np.sign(y - seg[1]) != np.sign(ydest - seg[1]):
                        self.inters.append((x, seg[1]))
            self.line2_segs.append((x,y,xdest,ydest))
            x = xdest
            y = ydest

        if (0,0) in self.inters:
            self.inters.remove((0,0))

        def man_dist(tup):
            return abs(tup[0]) + abs(tup[1])

        dist = map(man_dist, self.inters)
        return min(dist)

    def part2(self):
        def timing_dist(tup):
            d = 0

            for seg in self.line1_segs:
                if seg[0] == seg[2]:
                    if seg[0] == tup[0] and \
                            np.sign(seg[1] - tup[1]) != np.sign(seg[3] - tup[1]):
                        d += abs(tup[1] - seg[1])
                        break
                    else:
                        d += abs(seg[3]-seg[1])
                else:
                    if seg[1] == tup[1] and \
                            np.sign(seg[0] - tup[0]) != np.sign(seg[2] - tup[0]):
                        d += abs(tup[0] - seg[0])
                        break
                    else:
                        d += abs(seg[2] - seg[0])

            for seg in self.line2_segs:
                if seg[0] == seg[2]:
                    if seg[0] == tup[0] and \
                            np.sign(seg[1] - tup[1]) != np.sign(seg[3] - tup[1]):
                        d += abs(tup[1] - seg[1])
                        break
                    else:
                        d += abs(seg[3]-seg[1])
                else:
                    if seg[1] == tup[1] and \
                            np.sign(seg[0] - tup[0]) != np.sign(seg[2] - tup[0]):
                        d += abs(tup[0] - seg[0])
                        break
                    else:
                        d += abs(seg[2] - seg[0])

            return d

        dist = map(timing_dist, self.inters)
        return min(dist)
