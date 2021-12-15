import heapq


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
            self.input = [[int(ch) for ch in line] for line in self.input]
        self.w = len(self.input[0])
        self.h = len(self.input)

    def part1(self):

        memo = {(0, 0): 0}
        states_to_examine = [(0, (0, 0))]
        heapq.heapify(states_to_examine)

        while True:
            cdist, xy = heapq.heappop(states_to_examine)
            x, y = xy
            if y == self.h - 1 and x == self.w - 1:
                break

            for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (dir[0] + x >= self.w
                        or dir[0] + x < 0
                        or dir[1] + y >= self.h
                        or dir[1] + y < 0):
                    continue
                x1 = x + dir[0]
                y1 = y + dir[1]
                dist = self.input[y1][x1]
                next_dist = cdist + dist
                if (x1, y1) not in memo or next_dist < memo[(x1, y1)]:
                    memo[(x1, y1)] = next_dist
                    heapq.heappush(states_to_examine, (next_dist, (x1, y1)))
        return cdist

    def part2(self):
        memo = {(0, 0): 0}
        states_to_examine = [(0, (0, 0))]
        heapq.heapify(states_to_examine)

        while True:
            cdist, xy = heapq.heappop(states_to_examine)
            x, y = xy
            if y == self.h*5 - 1 and x == self.w*5 - 1:
                break

            for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (dir[0] + x >= self.w*5
                        or dir[0] + x < 0
                        or dir[1] + y >= self.h*5
                        or dir[1] + y < 0):
                    continue
                x1 = x + dir[0]
                y1 = y + dir[1]
                dist = (self.input[y1 % self.h][x1 % self.w]
                        + 1*(y1//self.h)
                        + 1*(x1//self.w) - 1) % 9 + 1
                next_dist = cdist + dist
                if (x1, y1) not in memo or next_dist < memo[(x1, y1)]:
                    memo[(x1, y1)] = next_dist
                    heapq.heappush(states_to_examine, (next_dist, (x1, y1)))
        return cdist
