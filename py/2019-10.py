import numpy as np

class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.roids = []
        for y in range(len(self.input)):
            for x in range(len(self.input[0])):
                if self.input[y][x] == '#':
                    self.roids.append(np.array((x, y)))

    def part1(self):
        r_ = np.array(self.roids)
        max_arg = None
        max_view = 0
        for roid in self.roids:
            vecs = roid[None, :] * np.ones((len(r_), 1)) - r_
            vecs_normalized = np.arctan2(vecs[:,1], vecs[:,0])
            roid_view_count = len(set(vecs_normalized))
            if roid_view_count > max_view:
                max_view = roid_view_count
                max_arg = roid

        # print(max_arg)
        return max_view

    def part2(self):
        my_roid = np.array([37, 25])
        r_ = np.array(self.roids)
        roids = r_ - my_roid[None, :] * np.ones((len(r_), 1))
        for i, v in enumerate(roids):
            if v[0] == v[1] == 0:
                roids = np.delete(roids, i, axis=0)
                break
        vecs = np.zeros((len(roids), 3))
        vecs[:, 0] = np.hypot(roids[:, 0], roids[:, 1])
        vecs[:, 1] = (np.arctan2(roids[:, 0], -roids[:, 1])*180/np.pi + 360) % 360
        vecs[:, 2] = np.arange(len(roids))

        vecs_sorted = np.sort(vecs.view('f8,f8,f8'), order=['f1', 'f0'], axis=0)

        vecs_super_sorted = []
        next_round = []
        while len(vecs_super_sorted) < 200:
            if len(vecs_sorted) == 0:
                if len(next_round) > 0:
                    vecs_sorted = next_round
                else:
                    break
            next_vec = vecs_sorted[0, :]
            vecs_super_sorted.append(next_vec)
            vecs_sorted = vecs_sorted[1:, :]
            while np.abs(vecs_sorted[0][0][1] - vecs_super_sorted[-1][0][1]) <= 1e-5:
                next_round.append(vecs_sorted[0, :])
                vecs_sorted = vecs_sorted[1:, :]

        roid = vecs_super_sorted[199]
        ans = roids[int(roid[0][2])] + my_roid
        return int(ans[0] * 100 + ans[1])
