class BingoBoard:

    def __init__(self, board_str):
        self.called = [[False]*5 for _ in range(5)]
        self.nums = [[int(n) for n in line.split()] for line in board_str.splitlines()]
        self.won = False
        self.score = None

    def call(self, num):
        for i, row in enumerate(self.nums):
            for j, n in enumerate(row):
                if num == n:
                    self.called[i][j] = True
                    if self.check_victory(i, j):
                        return self.get_score(num)

    def check_victory(self, row, column):
        if all(self.called[row]):
            self.won = True
            return self.won
        if all([self.called[i][column] for i in range(5)]):
            self.won = True
            return self.won
        return False

    def get_score(self, last_num):
        total = 0
        for i, row in enumerate(self.called):
            for j, b in enumerate(row):
                if not b:
                    total += self.nums[i][j]
        self.score = total * last_num
        return self.score

    def reset(self):
        self.called = [[False]*5 for _ in range(5)]
        self.won = False
        self.score = None


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().split('\n\n')

        self.calls = list(map(int, self.input[0].split(',')))
        self.boards = []
        for brd in self.input[1:]:
            self.boards.append(BingoBoard(brd))

    def part1(self):
        [board.reset() for board in self.boards]
        for call in self.calls:
            for board in self.boards:
                board.call(call)
                if board.won:
                    return board.score

    def part2(self):
        [board.reset() for board in self.boards]
        boards = set(self.boards)
        for call in self.calls:
            next_boards = set(boards)
            for board in boards:
                board.call(call)
                if board.won:
                    next_boards.remove(board)
                    if len(next_boards) == 0:
                        return board.score
            boards = next_boards
