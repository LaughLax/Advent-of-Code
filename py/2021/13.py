import numpy as np
import matplotlib.pyplot as plt


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
        new_pts = set()
        f = self.folds[0][1]
        for pt in self.pts:
            if self.folds[0][0] == 'x':
                if pt[0] > f:
                    new_pts.add((2 * f - pt[0], pt[1]))
                else:
                    new_pts.add(pt)
            elif self.folds[0][0] == 'y':
                if pt[1] > f:
                    new_pts.add((pt[0], 2 * f - pt[1]))
                else:
                    new_pts.add(pt)
        return len(new_pts)

    def part2(self):
        pts = self.pts.copy()
        for fold in self.folds:
            new_pts = set()
            f = fold[1]
            for pt in pts:
                if fold[0][0] == 'x':
                    if pt[0] > f:
                        new_pts.add((2 * f - pt[0], pt[1]))
                    else:
                        new_pts.add(pt)
                elif fold[0][0] == 'y':
                    if pt[1] > f:
                        new_pts.add((pt[0], 2 * f - pt[1]))
                    else:
                        new_pts.add(pt)
            pts = new_pts
        show_thing(pts)
        return
