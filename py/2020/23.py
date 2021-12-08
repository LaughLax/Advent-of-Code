from collections import deque


class MyLLNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = [int(i) for i in f.read().strip()]

    def part1(self):
        cups = deque(self.input)

        for _ in range(100):
            orig_val = cups[0]
            dest_val = cups[0] - 1
            if dest_val < 1:
                dest_val += 9
            cups.rotate(-1)

            c1 = cups.popleft()
            c2 = cups.popleft()
            c3 = cups.popleft()

            while dest_val in (c1, c2, c3):
                dest_val = dest_val - 1 if dest_val > 1 else dest_val + 8

            while cups[0] != dest_val:
                cups.rotate(-1)
            cups.rotate(-1)

            cups.append(c1)
            cups.append(c2)
            cups.append(c3)

            while cups[0] != orig_val:
                cups.rotate(-1)
            cups.rotate(-1)

        while cups[0] != 1:
            cups.rotate(-1)
        cups.popleft()

        return ''.join([str(i) for i in cups])

    def part2(self):
        nodes = {}

        # Build from input
        last_node = None
        for i in self.input:
            node = MyLLNode(i)
            nodes[i] = node
            if last_node is not None:
                last_node.right = node
                node.left = last_node
            last_node = node

        # Complete 1 million nodes
        for i in range(len(self.input)+1, 1_000_001):
            node = MyLLNode(i)
            nodes[i] = node
            if last_node is not None:
                last_node.right = node
                node.left = last_node
            last_node = node

        # Complete the circle
        ptr = nodes[self.input[0]]
        last_node.right = ptr
        ptr.left = last_node

        assert len(nodes) == 1_000_000

        ptr = nodes[self.input[0]]
        for i in range(10_000_000):
            p_val = ptr.val

            c1 = ptr.right
            c2 = c1.right
            c3 = c2.right

            ptr.right = c3.right
            ptr.right.left = ptr

            d_val = p_val - 1 or 1_000_000
            while d_val in (c1.val, c2.val, c3.val):
                d_val = d_val - 1 or 1_000_000

            d_node = nodes[d_val]

            c3.right = d_node.right
            c3.right.left = c3
            d_node.right = c1
            c1.left = d_node

            ptr = ptr.right

        while ptr.val != 1:
            ptr = ptr.right

        return ptr.right.val * ptr.right.right.val
