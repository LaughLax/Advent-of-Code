class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        max_id = 0
        for line in self.input:
            row = 0
            for char in line[0:7]:
                if char == 'B':
                    row += 1
                row = row << 1
            row = row >> 1
            col = 0
            for char in line[7:]:
                if char == 'R':
                    col += 1
                col = col << 1
            col = col >> 1
            seat_id = row * 8 + col
            max_id = max(max_id, seat_id)

        return max_id

    def part2(self):
        ids = set()
        min_id = 10000
        max_id = 0
        for line in self.input:
            row = 0
            for char in line[0:7]:
                if char == 'B':
                    row += 1
                row = row << 1
            row = row >> 1
            col = 0
            for char in line[7:]:
                if char == 'R':
                    col += 1
                col = col << 1
            col = col >> 1
            seat_id = row * 8 + col
            ids.add(seat_id)
            min_id = min(min_id, seat_id)
            max_id = max(max_id, seat_id)

        all_ids = set(range(min_id,max_id+1))
        reduced = all_ids ^ ids
        for seat in reduced:
            if min_id < seat < max_id:
                return seat
