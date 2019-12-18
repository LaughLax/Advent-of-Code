import networkx as nx
from tqdm import tqdm
import heapq


class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().strip().splitlines()

        self.keys = None
        self.doors = None
        self.center = None
        self.key_to_key = None

    def define_graph(self, lines):
        trimming = True
        while trimming:
            trimming = False
            for y in range(1, len(lines) - 1):
                for x in range(1, len(lines[y]) - 1):
                    if lines[y][x] == '#':
                        continue

                    wall_neighbors = 0
                    for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        if lines[y+d[1]][x+d[0]] == '#':
                            wall_neighbors += 1

                    if wall_neighbors == 3 and not lines[y][x].islower() and lines[y][x] not in ('@', '0', '1', '2', '3'):
                        lines[y][x] = '#'
                        trimming = True

        # maze_map = '\n'.join([''.join(line) for line in lines])
        # print(maze_map)

        G = nx.Graph()
        self.keys = {}
        self.doors = {}
        self.center = {}
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                c = lines[y][x]
                if c != '#':
                    G.add_node((x, y), name=c)
                    if c.islower():
                        self.keys[c] = (x, y)
                    elif c.isupper():
                        self.doors[c] = (x, y)
                    elif c in ('@', '0', '1', '2', '3'):
                        self.center[c] = (x, y)

        for node in G:
            for direction in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                neighbor = (node[0] + direction[0], node[1] + direction[1])
                if neighbor in G.nodes:
                    G.add_edge(node, neighbor)

        self.key_to_key = {}
        for key1 in list(self.keys):
            key1_d = self.key_to_key.setdefault(key1, {})
            for key2 in self.keys:
                if key2 is key1:
                    continue

                if nx.has_path(G, self.keys[key1], self.keys[key2]):
                    path = nx.shortest_path(G, self.keys[key1], self.keys[key2])
                    my_len = len(path) - 1
                    doors = set()
                    for door in self.doors:
                        if self.doors[door] in path:
                            doors.add(door)

                    key1_d[key2] = (my_len, doors)

                    key2_d = self.key_to_key.setdefault(key2, {})
                    key2_d[key1] = (my_len, doors)

        for key1 in self.center:
            key1_d = self.key_to_key.setdefault(key1, {})
            for key2 in self.keys:
                if key2 is key1:
                    continue

                if nx.has_path(G, self.center[key1], self.keys[key2]):
                    path = nx.shortest_path(G, self.center[key1], self.keys[key2])
                    my_len = len(path) - 1
                    doors = set()
                    for door in self.doors:
                        if self.doors[door] in path:
                            doors.add(door)

                    key1_d[key2] = (my_len, doors)

                    key2_d = self.key_to_key.setdefault(key2, {})
                    key2_d[key1] = (my_len, doors)

    def part1(self):
        lines = [[c for c in line] for line in self.input]
        self.define_graph(lines)

        memo = {}

        states_to_examine = [(0, (frozenset(),
                                  '@',
                                  0))]
        heapq.heapify(states_to_examine)

        winner_state = None
        parents = {}

        while winner_state is None:
            cdist, state = heapq.heappop(states_to_examine)

            if len(state[0]) == 1 + 26:
                winner_state = state

            for next_key in self.key_to_key[state[1]]:
                if next_key in state[0]:
                    continue

                dist, doors = self.key_to_key[state[1]][next_key]

                key_failed = False
                for d in doors:
                    if d.lower() not in state[0]:
                        key_failed = True
                if key_failed:
                    continue

                next_layer_keys = state[0] | frozenset(next_key)

                next_layer_dist = state[2] + dist
                if (next_layer_keys, next_key) not in memo or next_layer_dist < memo[(next_layer_keys, next_key)]:
                    memo[(next_layer_keys, next_key)] = next_layer_dist
                    next_state = (next_layer_keys,
                                  next_key,
                                  next_layer_dist)
                    parents[(next_state[0], next_state[1])] = (state[0], state[1])
                    heapq.heappush(states_to_examine, (next_layer_dist, next_state))

        # s = (winner_state[0], winner_state[1])
        # sequence = [s[1]]
        # while s in parents:
        #     s = parents[s]
        #     sequence.append(s[1])
        # sequence.reverse()

        return winner_state[2]

    def part2(self):
        lines = [[c for c in line] for line in self.input]
        c_x = 40
        c_y = 40
        lines[c_y-1][c_x-1] = '0'
        lines[c_y-1][c_x] = '#'
        lines[c_y-1][c_x+1] = '1'
        lines[c_y][c_x-1] = '#'
        lines[c_y][c_x] = '#'
        lines[c_y][c_x+1] = '#'
        lines[c_y+1][c_x-1] = '2'
        lines[c_y+1][c_x] = '#'
        lines[c_y+1][c_x+1] = '3'
        self.define_graph(lines)

        memo = {}

        states_to_examine = [(0, (frozenset(('0', '1', '2', '3')),
                                  ('0', '1', '2', '3'),
                                  0))]
        heapq.heapify(states_to_examine)

        winner_state = None
        parents = {}

        while winner_state is None:
            cdist, state = heapq.heappop(states_to_examine)

            if len(state[0]) == 4+26:
                winner_state = state

            for i in range(4):
                for next_key in self.key_to_key[state[1][i]]:
                    if next_key in state[0]:
                        continue

                    dist, doors = self.key_to_key[state[1][i]][next_key]

                    key_failed = False
                    for d in doors:
                        if d.lower() not in state[0]:
                            key_failed = True
                    if key_failed:
                        continue

                    next_layer_keys = state[0] | frozenset(next_key)
                    next_pos = []
                    for j in range(4):
                        next_pos.append(state[1][j] if j != i else next_key)
                    next_pos = tuple(next_pos)

                    next_layer_dist = cdist + dist
                    if (next_layer_keys, next_pos) not in memo or next_layer_dist < memo[(next_layer_keys, next_pos)]:
                        memo[(next_layer_keys, next_pos)] = next_layer_dist
                        next_state = (next_layer_keys,
                                      next_pos,
                                      next_layer_dist)
                        parents[(next_state[0], next_state[1])] = (state[0], state[1])
                        heapq.heappush(states_to_examine, (next_layer_dist, next_state))

        # s = (winner_state[0], winner_state[1])
        # sequence = [s[1]]
        # while s in parents:
        #     s = parents[s]
        #     sequence.append(s[1])
        # sequence.reverse()

        return winner_state[2]
