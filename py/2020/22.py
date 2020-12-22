from collections import deque
from copy import copy


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        p1, p2 = self.input.split('\n\n')
        self.deck_1 = deque([int(i) for i in p1.splitlines()[1:]])
        self.deck_2 = deque([int(i) for i in p2.splitlines()[1:]])

    def part1(self):
        p1 = copy(self.deck_1)
        p2 = copy(self.deck_2)

        while len(p1) > 0 and len(p2) > 0:
            c1 = p1.popleft()
            c2 = p2.popleft()

            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            elif c2 > c1:
                p2.append(c2)
                p2.append(c1)
            # print(p1)
            # print(p2)
            # print()

        winner = p1 if len(p1) > 0 else p2

        i, tot = 0, 0
        for _ in range(len(winner)):
            i += 1
            v = winner.pop()
            tot += i * v

        return tot

    def r_combat(self, deck1: deque, deck2: deque):
        states = set()

        while len(deck1) > 0 and len(deck2) > 0:
            state = (tuple(deck1), tuple(deck2))
            if state in states:
                return 1, list(deck1)
            states.add(state)

            c1 = deck1.popleft()
            c2 = deck2.popleft()
            recurse = (c1 <= len(deck1)) and (c2 <= len(deck2))
            if recurse:
                d1_subcopy = deque(copy(tuple(deck1)[0:c1]))
                d2_subcopy = deque(copy(tuple(deck2)[0:c2]))
                winner, _ = self.r_combat(d1_subcopy, d2_subcopy)
                if winner == 1:
                    deck1.append(c1)
                    deck1.append(c2)
                elif winner == 2:
                    deck2.append(c2)
                    deck2.append(c1)
                else:
                    raise Exception(winner)
            else:
                if c1 > c2:
                    deck1.append(c1)
                    deck1.append(c2)
                elif c2 > c1:
                    deck2.append(c2)
                    deck2.append(c1)

        if len(deck1) > 0:
            return 1, list(deck1)
        elif len(deck2) > 0:
            return 2, list(deck2)

        raise Exception()

    def part2(self):
        winner, win_deck = self.r_combat(copy(self.deck_1), copy(self.deck_2))

        i, tot = 0, 0
        for _ in range(len(win_deck)):
            i += 1
            v = win_deck.pop()
            tot += i * v

        return tot
