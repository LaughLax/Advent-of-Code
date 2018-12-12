from collections import deque


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.state = self.input.pop(0).split()[2]
        self.input.pop(0)
        self.first=0

        self.rules = {}
        for line in self.input:
            key, val = line.split(' => ')
            self.rules[key] = val

    def next_state(self, f_input):
        next_st = []
        old_st = deque(f_input)
        
        neighbors = deque(['.','.','.','.'])
        old_st.extend(['.','.','.','.'])

        while len(old_st) > 0:
            neighbors.append(old_st.popleft())
            next_st.append(self.rules[''.join(neighbors)])
            neighbors.popleft()

        left_shift = -2
        for char in next_st:
            if char == '.':
                left_shift += 1
            else:
                break
        self.first += left_shift

        next_st = ''.join(next_st)
        next_st = next_st.strip('.')

        return next_st

    def my_sum(self, state, first_val):
        val = first_val
        tot_val = 0
        for char in state:
            if char == '#':
                tot_val += val
            val += 1
        return tot_val

    def row(self, state):
        if self.first > 0:
            prepend = ['_']
            for i in range(self.first-1):
                prepend.append('.')
            return ''.join(prepend) + state
        if self.first == 0:
            return ('@' if state[0] == '#' else '_') + state[1:]
        
        return state[0:-self.first] + ('@' if state[-self.first] == '#' else '_') + state[-self.first+1:]

    def part1(self):
        state = self.state
        for i in range(20):
            state = self.next_state(state)
        return self.my_sum(state, self.first)

    def part2(self):
        state = self.state
        self.first = 0

        lim = 50000000000
        
        total = self.my_sum(state, self.first)
        d_total = 0
        last_run_smooth = False

        for i in range(lim):
            state = self.next_state(state)
            new_tot = self.my_sum(state, self.first)

            if new_tot - total == d_total:
                if last_run_smooth:
                    return new_tot + d_total * (lim - i - 1)
                last_run_smooth = True

            d_total = new_tot - total
            total = new_tot

        return self.my_sum(state, self.first)
