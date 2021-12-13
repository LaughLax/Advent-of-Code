import numpy as np
import matplotlib.pyplot as plt


def fold(pts, axis, line):
    result = set()
    for pt in pts:
        if axis == 'x' and pt[0] > line:
            result.add((2 * line - pt[0], pt[1]))
        elif axis == 'y' and pt[1] > line:
            result.add((pt[0], 2 * line - pt[1]))
        else:
            result.add(pt)
    return result


def show_thing(my_set):
    max_x = max(p[0] for p in my_set)
    max_y = max(p[1] for p in my_set)
    chars = np.zeros((max_y+1, max_x+1), dtype=bool)
    for pt in my_set:
        chars[pt[1], pt[0]] = True
    plt.imshow(chars)
    plt.show()


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()
            pts, folds = self.input.strip().split('\n\n')
            pts = pts.split('\n')
            folds = folds.split('\n')
        self.pts = []
        for line in pts:
            nums = line.split(',')
            self.pts.append((int(nums[0]), int(nums[1])))
        self.folds = []
        for line in folds:
            self.folds.append((line[11], int(line[13:])))

    def part1(self):
        return len(fold(self.pts, self.folds[0][0], self.folds[0][1]))

    def part2(self):
        pts = self.pts.copy()
        for f in self.folds:
            pts = fold(pts, f[0], f[1])
        show_thing(pts)
        return
