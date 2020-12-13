class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = list(map(int, f.read().split()))

    def part1(self):
        blocks = self.input[:]

        steps = 0
        seen = set()
        while tuple(blocks) not in seen:
            seen.add(tuple(blocks))

            to_move = max(blocks)
            ind = blocks.index(to_move)
            blocks[ind] = 0

            all_blocks = int(to_move / len(blocks))
            remainder = to_move % len(blocks)
            while remainder:
                ind = ind + 1 if ind < len(blocks) - 1 else 0
                blocks[ind] += all_blocks + (1 if remainder else 0)
                remainder -= 1

            steps += 1
        return steps

    def part2(self):
        blocks = self.input[:]

        steps = 0
        seen = {}
        while tuple(blocks) not in seen:
            seen[tuple(blocks)] = steps

            to_move = max(blocks)
            ind = blocks.index(to_move)
            blocks[ind] = 0

            all_blocks = int(to_move / len(blocks))
            remainder = to_move % len(blocks)
            while remainder:
                ind = ind + 1 if ind < len(blocks) - 1 else 0
                blocks[ind] += all_blocks + (1 if remainder else 0)
                remainder -= 1

            steps += 1
        return steps - seen[tuple(blocks)]
