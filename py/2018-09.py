class AdventOfCode:

    def __init__(self, filename):
        self.current_marble = Marble(0, None)
        self.current_player = 0

        with open(filename) as f:
            line = f.read().split()

        self.num_players = int(line[0])
        self.scores = [0] * self.num_players
        self.num_marbles = int(line[-2])

    def part1(self):
        for i in range(1, self.num_marbles + 1):
            if (i % 23) == 0:
                for j in range(6):
                    self.current_marble = self.current_marble.ccw
                self.scores[self.current_player] += i + self.current_marble.ccw.remove()
            else:
                self.current_marble = Marble(i, self.current_marble.cw)
            self.current_player = (self.current_player + 1) % self.num_players
        return max(self.scores)

    def part2(self):
        new_max = self.num_marbles * 100
        for i in range(self.num_marbles + 1, new_max + 1):
            if (i % 23) == 0:
                for j in range(6):
                    self.current_marble = self.current_marble.ccw
                self.scores[self.current_player] += i + self.current_marble.ccw.remove()
            else:
                self.current_marble = Marble(i, self.current_marble.cw)
            self.current_player = (self.current_player + 1) % self.num_players
        return max(self.scores)


class Marble:

    def __init__(self, num, preceding_marble):
        self.value = num

        if num == 0:
            self.ccw = self
            self.cw = self
        else:
            self.ccw = preceding_marble
            self.cw = preceding_marble.cw

            self.ccw.cw = self
            self.cw.ccw = self

    def remove(self):
        self.ccw.cw = self.cw
        self.cw.ccw = self.ccw

        return self.value
