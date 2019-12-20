import networkx as nx
from tqdm import tqdm
import heapq


class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().strip().splitlines()

        self.key_to_key1 = None
        self.key_to_key2 = None

    def define_graph(self, lines):
        keys = {}
        doors = {}
        center = {}
        paths = set()

        for y in range(1, len(lines) - 1):
            for x in range(1, len(lines[y]) - 1):
                c = lines[y][x]
                if c != '#':
                    paths.add((x, y))
                    if c.islower():
                        keys[c] = (x, y)
                    elif c.isupper():
                        doors[c] = (x, y)
                    elif c in ('@', '0', '1', '2', '3'):
                        center[c] = (x, y)

        to_remove = set()
        for x, y in paths:
            if lines[y][x] in keys or lines[y][x] in center or (x, y) in to_remove:
                continue

            path_neighbors = []
            for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                if (x+d[0], y+d[1]) in paths:
                    path_neighbors.append((x, y))

            if len(path_neighbors) == 1:
                to_remove.add((x, y))
        while len(to_remove) > 0:
            x, y = to_remove.pop()
            if lines[y][x] in keys or lines[y][x] in center:
                continue

            path_neighbors = []
            for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                if (x+d[0], y+d[1]) in paths:
                    path_neighbors.append((x+d[0], y+d[1]))

            if len(path_neighbors) == 1:
                lines[y][x] = '#'
                paths.remove((x, y))
                to_remove.add(path_neighbors[0])

        # maze_map = '\n'.join([''.join(line) for line in lines])
        # print(maze_map)

        G = nx.Graph()
        for x, y in paths:
            G.add_node((x, y))

        for node in G:
            for direction in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                neighbor = (node[0] + direction[0], node[1] + direction[1])
                if neighbor in G.nodes:
                    G.add_edge(node, neighbor)

        key_to_key = {}
        for key1 in list(keys):
            key1_d = key_to_key.setdefault(key1, {})
            for key2 in keys:
                if key2 is key1:
                    continue

                if nx.has_path(G, keys[key1], keys[key2]):
                    path = nx.shortest_path(G, keys[key1], keys[key2])
                    my_len = len(path) - 1
                    path_doors = set()
                    for door in doors:
                        if doors[door] in path:
                            path_doors.add(door.lower())

                    key1_d[key2] = (my_len, path_doors)

                    key2_d = key_to_key.setdefault(key2, {})
                    key2_d[key1] = (my_len, path_doors)

        for key1 in center:
            key1_d = key_to_key.setdefault(key1, {})
            for key2 in keys:
                if key2 is key1:
                    continue

                if nx.has_path(G, center[key1], keys[key2]):
                    path = nx.shortest_path(G, center[key1], keys[key2])
                    my_len = len(path) - 1
                    path_doors = set()
                    for door in doors:
                        if doors[door] in path:
                            path_doors.add(door.lower())

                    key1_d[key2] = (my_len, path_doors)

                    key2_d = key_to_key.setdefault(key2, {})
                    key2_d[key1] = (my_len, path_doors)

        return key_to_key

    def part1(self):
        lines = [[c for c in line] for line in self.input]
        self.key_to_key1 = self.define_graph(lines)

        memo = {}

        states_to_examine = [(0, (frozenset(), '@'))]
        heapq.heapify(states_to_examine)

        while True:
            cdist, state = heapq.heappop(states_to_examine)
            keys, pos = state

            if len(keys) == 1 + 26:
                break

            for next_key in self.key_to_key1[pos]:
                if next_key in keys:
                    continue

                dist, doors = self.key_to_key1[pos][next_key]

                key_failed = False
                for d in doors:
                    if d not in keys:
                        key_failed = True
                        break
                if key_failed:
                    continue

                next_layer_dist = cdist + dist
                next_layer_keys = keys | frozenset(next_key)
                next_state = (next_layer_keys,
                              next_key)

                if next_state not in memo or next_layer_dist < memo[next_state]:
                    memo[next_state] = next_layer_dist
                    heapq.heappush(states_to_examine, (next_layer_dist, next_state))

        return cdist

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
        self.key_to_key2 = self.define_graph(lines)

        memo = {}

        states_to_examine = [(0, (frozenset(('0', '1', '2', '3')), ('0', '1', '2', '3')))]
        heapq.heapify(states_to_examine)

        while True:
            cdist, state = heapq.heappop(states_to_examine)
            keys, pos = state

            if len(keys) == 4+26:
                break

            for i in range(4):
                for next_key in self.key_to_key2[pos[i]]:
                    if next_key in keys:
                        continue

                    dist, doors = self.key_to_key2[pos[i]][next_key]

                    key_failed = False
                    for d in doors:
                        if d not in keys:
                            key_failed = True
                            break
                    if key_failed:
                        continue

                    next_layer_keys = keys | frozenset(next_key)
                    next_pos = tuple(pos[j] if j != i else next_key for j in range(4))

                    next_layer_dist = cdist + dist
                    next_state = (next_layer_keys,
                                  next_pos)

                    if next_state not in memo or next_layer_dist < memo[next_state]:
                        memo[next_state] = next_layer_dist
                        heapq.heappush(states_to_examine, (next_layer_dist, next_state))

        return cdist
