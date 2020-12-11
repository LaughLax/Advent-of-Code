from copy import deepcopy


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = [list(line) for line in f.read().splitlines()]

    @staticmethod
    def same(old, new):
        for i in range(len(old)):
            for j in range(len(old[i])):
                if old[i][j] != new[i][j]:
                    return False
        return True

    @staticmethod
    def count_occ(state):
        count = 0
        for i in state:
            for j in i:
                if j == '#':
                    count += 1
        return count

    @staticmethod
    def copy_in_place(dest, orig):
        for i, row in enumerate(orig):
            for j, val in enumerate(row):
                dest[i][j] = val

    def part1(self):
        state = deepcopy(self.input)
        new_state = deepcopy(state)
        while True:
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] == '.':
                        continue

                    occ_neighb = 0
                    if i > 0:
                        if j > 0 and state[i-1][j-1] == '#':
                            occ_neighb += 1
                        if state[i-1][j] == '#':
                            occ_neighb += 1
                        if j+1 < len(state[i-1]) and state[i-1][j+1] == '#':
                            occ_neighb += 1
                    if j > 0 and state[i][j-1] == '#':
                            occ_neighb += 1
                    if j+1 < len(state[i]) and state[i][j+1] == '#':
                        occ_neighb += 1
                    if i+1 < len(state):
                        if j > 0 and state[i+1][j-1] == '#':
                            occ_neighb += 1
                        if state[i+1][j] == '#':
                            occ_neighb += 1
                        if j+1 < len(state[i+1]) and state[i+1][j+1] == '#':
                            occ_neighb += 1

                    if occ_neighb == 0:
                        new_state[i][j] = '#'
                    elif occ_neighb >= 4:
                        new_state[i][j] = 'L'

            if self.same(state, new_state):
                return self.count_occ(new_state)
            else:
                self.copy_in_place(state, new_state)


    def part2(self):
        state = deepcopy(self.input)
        new_state = deepcopy(state)
        while True:
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] == '.':
                        continue

                    occ_neighb = 0

                    # Up-left
                    k = 0
                    while True:
                        k += 1
                        if i-k >= 0 and j-k >= 0:
                            if state[i-k][j-k] == '#':
                                occ_neighb += 1
                                break
                            elif state[i-k][j-k] == 'L':
                                break
                        else:
                            break

                    # Up
                    k = 0
                    while True:
                        k += 1
                        if i-k >= 0:
                            if state[i-k][j] == '#':
                                occ_neighb += 1
                                break
                            elif state[i-k][j] == 'L':
                                break
                        else:
                            break

                    # Up-right
                    k = 0
                    while True:
                        k += 1
                        if i-k >= 0 and j+k < len(self.input[0]):
                            if state[i-k][j+k] == '#':
                                occ_neighb += 1
                                break
                            elif state[i-k][j+k] == 'L':
                                break
                        else:
                            break

                    # Right
                    k = 0
                    while True:
                        k += 1
                        if j+k < len(self.input[0]):
                            if state[i][j+k] == '#':
                                occ_neighb += 1
                                break
                            elif state[i][j+k] == 'L':
                                break
                        else:
                            break

                    # Down-right
                    k = 0
                    while True:
                        k += 1
                        if i+k < len(self.input) and j+k < len(self.input[0]):
                            if state[i+k][j+k] == '#':
                                occ_neighb += 1
                                break
                            elif state[i+k][j+k] == 'L':
                                break
                        else:
                            break

                    # Down
                    k = 0
                    while True:
                        k += 1
                        if i+k < len(self.input):
                            if state[i+k][j] == '#':
                                occ_neighb += 1
                                break
                            elif state[i+k][j] == 'L':
                                break
                        else:
                            break

                    # Down-left
                    k = 0
                    while True:
                        k += 1
                        if i+k < len(self.input) and j-k >= 0:
                            if state[i+k][j-k] == '#':
                                occ_neighb += 1
                                break
                            elif state[i+k][j-k] == 'L':
                                break
                        else:
                            break

                    # Left
                    k = 0
                    while True:
                        k += 1
                        if j-k >= 0:
                            if state[i][j-k] == '#':
                                occ_neighb += 1
                                break
                            elif state[i][j-k] == 'L':
                                break
                        else:
                            break

                    if occ_neighb == 0:
                        new_state[i][j] = '#'
                    elif occ_neighb >= 5:
                        new_state[i][j] = 'L'

            if self.same(state, new_state):
                return self.count_occ(new_state)
            else:
                self.copy_in_place(state, new_state)
