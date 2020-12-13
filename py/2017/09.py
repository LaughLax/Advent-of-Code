class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = list(f.read())

        self.top_group = Group()

        current_group = self.top_group
        input = self.input[::-1]
        while len(input) > 0:
            char = input.pop()

            if char == '{':
                current_group = Group(current_group)
                # print(current_group.parent.items)

            elif char == '<':
                garbo = []
                char = input.pop()
                while char != '>':
                    if char == '!':
                        input.pop()
                    else:
                        garbo.append(char)
                    char = input.pop()
                current_group.add_item(garbo)

            elif char == '}':
                current_group = current_group.parent

    def part1(self):
        return self.top_group.total_value()

    def part2(self):
        return self.top_group.garbo_removed()


class Group:

    def __init__(self, parent=None):
        self.parent = parent

        if parent:
            self.value = parent.value + 1
            self.parent.add_item(self)
        else:
            self.value = 0

        self.subgroups = []
        self.garbo = []

    def add_item(self, item):
        if type(item) is list:
            self.garbo.append(''.join(item))
        else:
            self.subgroups.append(item)

    def total_value(self):
        return self.value + sum(g.total_value() for g in self.subgroups)

    def garbo_removed(self):
        return sum(len(i) for i in self.garbo) + sum(g.garbo_removed() for g in self.subgroups)
