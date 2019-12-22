# multinv function by Raymond Hettinger
def multinv(modulus, value):
        '''Multiplicative inverse in a given modulus

            >>> multinv(191, 138)
            18
            >>> 18 * 138 % 191
            1

            >>> multinv(191, 38)
            186
            >>> 186 * 38 % 191
            1

            >>> multinv(120, 23)
            47
            >>> 47 * 23 % 120
            1

        '''
        # https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
        # http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
        x, lastx = 0, 1
        a, b = modulus, value
        while b:
            a, q, b = b, a // b, a % b
            x, lastx = lastx - q * x, x
        result = (1 - lastx * modulus) // value
        if result < 0:
            result += modulus
        assert 0 <= result < modulus and value * result % modulus == 1
        return result


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
        self.cmds = []
        for line in self.input:
            # print(line)
            if line[0:3] == 'cut':
                func = self.cut
                arg = int(line[4:])
            elif line[5:9] == 'with':
                func = self.deal_with
                arg = int(line[20:])
            elif line[5:9] == 'into':
                func = self.deal_into
                arg = None
            else:
                print('Unhandled line!!!')
            self.cmds.append((func, arg))

    def cut(self, deck, amt):
        num_cards = (len(deck) + amt) % len(deck)
        top_slice = deck[:num_cards]
        bottom_slice = deck[num_cards:]

        boundary = len(bottom_slice)
        deck[:boundary] = bottom_slice
        deck[boundary:] = top_slice

    def undo_cut(self, deck_len, amt, end_pos):
        return (end_pos + amt) % deck_len

    def deal_with(self, deck, incr):
        n = len(deck)
        copy = deck.copy()
        target_ind = [i*incr % n for i in range(n)]
        for i in range(n):
            deck[target_ind[i]] = copy[i]

    def undo_deal_with(self, deck_len, incr, end_pos):
        n = 0
        while (end_pos + n*deck_len) % incr != 0:
            n += 1
        return int((end_pos + n*deck_len) / incr)

    def deal_into(self, deck, _):
        deck.reverse()

    def undo_deal_into(self, deck_len, end_pos):
        return deck_len - end_pos - 1

    def part1(self):
        deck = list(range(10007))
        for cmd in self.cmds:
            # print(deck)
            cmd[0](deck, cmd[1])

        # print(deck)
        return deck.index(2019)

    def inverse_mod(self, deck_len, incr, end_pos):
        pass

    def part2(self):
        deck_len = 119315717514047
        reps = 101741582076661
        x0 = pos = 2020
        for cmd in self.cmds[::-1]:
            if cmd[0] == self.cut:
                # print(f'Undoing cut of amount {cmd[1]}')
                pos = self.undo_cut(deck_len, cmd[1], pos)
            elif cmd[0] == self.deal_with:
                # print(f'Undoing deal_with of amount {cmd[1]}')
                pos = self.undo_deal_with(deck_len, cmd[1], pos)
            elif cmd[0] == self.deal_into:
                # print(f'Undoing deal_into')
                pos = self.undo_deal_into(deck_len, pos)
        y0 = x1 = pos

        for cmd in self.cmds[::-1]:
            if cmd[0] == self.cut:
                # print(f'Undoing cut of amount {cmd[1]}')
                pos = self.undo_cut(deck_len, cmd[1], pos)
            elif cmd[0] == self.deal_with:
                # print(f'Undoing deal_with of amount {cmd[1]}')
                pos = self.undo_deal_with(deck_len, cmd[1], pos)
            elif cmd[0] == self.deal_into:
                # print(f'Undoing deal_into')
                pos = self.undo_deal_into(deck_len, pos)
        y1 = pos

        # y = ax + b
        # a = (y1 - y0) / (x1 - x0)
        # b = y0 - ax0
        a = (y1 - y0) * multinv(deck_len,x1 - x0 + deck_len) % deck_len
        b = (y0 - a*x0) % deck_len

        # geometric series: sum(a + ar + ar^2 . . . ar^[n-1]) = a * (1 - r^n) / (1 - r)
        # a = b
        # r = a
        b_stuff = b * (1 - pow(a, reps, deck_len)) * multinv(deck_len, 1 - a + deck_len)

        full_result = (pow(a, reps, deck_len)*x0 + b_stuff) % deck_len

        return full_result
