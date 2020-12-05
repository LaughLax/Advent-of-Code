class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read() \
                .replace('F', '0').replace('B', '1') \
                .replace('L', '0').replace('R', '1') \
                .splitlines()
            self.seat_ids = set([int(line, base=2) for line in self.input])

    def part1(self):
        return max(self.seat_ids)

    def part2(self):
        min_id = min(self.seat_ids)
        max_id = max(self.seat_ids)
        all_ids = set(range(min_id, max_id+1))
        return (all_ids - self.seat_ids).pop()
