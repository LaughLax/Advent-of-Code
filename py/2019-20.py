import networkx as nx
import heapq
from copy import deepcopy


class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()
        self.lines = [[c for c in line] for line in self.input]

        trimming = True
        paths = set()
        for y in range(2, len(self.lines) - 2):
            for x in range(2, len(self.lines[y]) - 2):
                if self.lines[y][x] == '.':
                    paths.add((x, y))

        while trimming:
            trimming = False
            to_remove = set()
            for x, y in paths:
                c = self.lines[y][x]

                wall_neighbors = 0
                for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    if self.lines[y+d[1]][x+d[0]] == '#':
                        wall_neighbors += 1

                if c == '.' and wall_neighbors == 3:
                    self.lines[y][x] = '#'
                    to_remove.add((x, y))
                    trimming = True
            for coord in to_remove:
                paths.remove(coord)

        # maze_map = '\n'.join([''.join(line) for line in self.lines])
        # print(maze_map)

        self.oc = ((2, 2), (len(self.lines[2])-1, len(self.lines)-3))
        self.ic = ((30, 30), (88, 90))   # Actual problem
        # self.ic = ((6, 6), (14, 12))   # Example 1
        # self.ic = ((8, 8), (26, 28))   # Example 2

        self.G = nx.Graph()
        self.portals = {}
        for y in range(self.oc[0][1], self.oc[1][1] + 1):
            for x in range(self.oc[0][0], self.oc[1][0] + 1):
                c = self.lines[y][x]
                if c == '.':
                    loc = (x, y)
                    self.G.add_node(loc)

                    portal_name = None
                    outer = None
                    if y == self.oc[0][1] or (y == self.ic[1][1] and self.ic[0][0] < x < self.ic[1][0]):
                        portal_name = self.lines[y-2][x] + self.lines[y-1][x]
                        outer = y == self.oc[0][1]
                    elif y == self.oc[1][1] or (y == self.ic[0][1] and self.ic[0][0] < x < self.ic[1][0]):
                        portal_name = self.lines[y+1][x] + self.lines[y+2][x]
                        outer = y == self.oc[1][1]
                    elif x == self.oc[0][0] or (x == self.ic[1][0] and self.ic[0][1] < y < self.ic[1][1]):
                        portal_name = self.lines[y][x-2] + self.lines[y][x-1]
                        outer = x == self.oc[0][0]
                    elif x == self.oc[1][0] or (x == self.ic[0][0] and self.ic[0][1] < y < self.ic[1][1]):
                        portal_name = self.lines[y][x+1] + self.lines[y][x+2]
                        outer = x == self.oc[1][0]
                    if portal_name is not None:
                        # print(f'Found {portal_name} at ({x}, {y})')
                        locations = self.portals.setdefault(portal_name, [None, None])
                        locations[outer] = loc

        for node in self.G:
            for direction in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                neighbor = (node[0] + direction[0], node[1] + direction[1])
                if neighbor in self.G.nodes:
                    self.G.add_edge(node, neighbor)

    def part1(self):
        G = deepcopy(self.G)

        for p in self.portals:
            if p == 'AA' or p == 'ZZ':
                continue
            locs = self.portals[p]
            assert len(locs) == 2
            G.add_edge(locs[0], locs[1])

        start = self.portals['AA'][1]
        end = self.portals['ZZ'][1]
        return nx.shortest_path_length(G, start, end)

    def part2(self):
        p_to_p = {}
        for p1 in self.portals:
            p1_i, p1_o = self.portals[p1]
            for p2 in self.portals:
                p2_i, p2_o = self.portals[p2]

                if p1 is not p2:
                    if p1_i is not None:
                        if p2_i is not None:
                            if nx.has_path(self.G, p1_i, p2_i):
                                path = nx.shortest_path(self.G, p1_i, p2_i)
                                my_len = len(path) - 1

                                p1_dict = p_to_p.setdefault(p1 + '_i', {})
                                p1_dict[p2 + '_i'] = my_len

                                p2_dict = p_to_p.setdefault(p2 + '_i', {})
                                p2_dict[p1 + '_i'] = my_len

                        if nx.has_path(self.G, p1_i, p2_o):
                            path = nx.shortest_path(self.G, p1_i, p2_o)
                            my_len = len(path) - 1

                            p1_dict = p_to_p.setdefault(p1 + '_i', {})
                            p1_dict[p2 + '_o'] = my_len

                            p2_dict = p_to_p.setdefault(p2 + '_o', {})
                            p2_dict[p1 + '_i'] = my_len

                    if nx.has_path(self.G, p1_o, p2_o):
                        path = nx.shortest_path(self.G, p1_o, p2_o)
                        my_len = len(path) - 1

                        p1_dict = p_to_p.setdefault(p1 + '_o', {})
                        p1_dict[p2 + '_o'] = my_len

                        p2_dict = p_to_p.setdefault(p2 + '_o', {})
                        p2_dict[p1 + '_o'] = my_len

                if p2_i is not None:
                    if nx.has_path(self.G, p1_o, p2_i):
                        path = nx.shortest_path(self.G, p1_o, p2_i)
                        my_len = len(path) - 1

                        p1_dict = p_to_p.setdefault(p1 + '_o', {})
                        p1_dict[p2 + '_i'] = my_len

                        p2_dict = p_to_p.setdefault(p2 + '_i', {})
                        p2_dict[p1 + '_o'] = my_len

        # print(self.p_to_p)

        # --------------Begin navigating-----------------

        states_to_examine = [(0, ((),           # 0: Portals passed through
                                  0,            # 1: Depth
                                  'AA_o',       # 2: Position
                                  0))]          # 3: Cumulative distance
        heapq.heapify(states_to_examine)

        winner_state = None
        parents = {}
        while winner_state is None:
            cum_dist, state = heapq.heappop(states_to_examine)

            memo = {}

            history = state[0]
            depth = state[1]
            pos = state[2]
            assert cum_dist == state[3]

            if pos == 'ZZ_i' and depth == -1:
                winner_state = state
                break

            for _pos in p_to_p[pos]:
                dist = p_to_p[pos][_pos]
                direction = _pos[-1]
                if _pos != 'ZZ_o':
                    if depth == 0 and direction == 'o':
                        continue
                    dist += 1

                if _pos == 'AA_o' or (_pos == 'ZZ_o' and depth != 0):
                    continue

                _pos = _pos[:-1] + ('o' if direction == 'i' else 'i')
                _depth = depth + (1 if direction == 'i' else -1)
                _history = tuple(sorted(history + (_pos,)))
                _cum_dist = cum_dist + dist

                if (_history, _depth, _pos) not in memo or _cum_dist < memo[(_history, _depth, _pos)]:
                    memo[(_history, _depth, _pos)] = _cum_dist
                    _state = (_history,
                              _depth,
                              _pos,
                              _cum_dist)
                    parents[(_state[0], _state[1], _state[2])] = (state[0], state[1], state[2])
                    heapq.heappush(states_to_examine, (_cum_dist, _state))

        return winner_state[3]

