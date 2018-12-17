import copy

debug = False


def my_sort(obj):
    try:
        return obj.y * 1000 + obj.x
    except AttributeError:
        return obj.grid_cell.y * 1000 + obj.grid_cell.x


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        self.grid = Grid(self.input)

    def part1(self):
        grid = Grid(self.input)

        i = 0
        while True:
            res = grid.tick(False)
            if res == -1:
                break
            i += 1

        return i * grid.total_health()
    
    def part2(self):
        att = 4
        while True:
            grid = Grid(self.input)
            for elf in grid.elfos:
                elf.attack_power = att

            i = 0
            while True:
                res = grid.tick(True)
                if res and res < 0:
                    break
                i += 1

            if res == -1:
                break
            elif res == -2:
                att += 1

        return i * grid.total_health()


class Grid:

    def __init__(self, input_str):
        self.spots = {}
        self.lims = None

        self.units = []
        self.elfos = []
        self.gobbos = []

        for y, line in enumerate(input_str.splitlines()):
            for x, char in enumerate(line):
                if char == '#':
                    cont = 'wall'
                elif char == 'G':
                    cont = Unit(elf=False)
                    self.units.append(cont)
                    self.gobbos.append(cont)
                elif char == 'E':
                    cont = Unit(elf=True)
                    self.units.append(cont)
                    self.elfos.append(cont)
                elif char == '.':
                    cont = None

                self.spots[(x, y)] = GridCell(x, y, self, cont)

        self.lims = (x, y)

        self.link_cells()

    def link_cells(self):
        for y in range(1, self.lims[1]):
            for x in range(1, self.lims[0]):
                self.spots[(x, y)].neighbors = (
                    self.spots[(x, y-1)],
                    self.spots[(x-1, y)],
                    self.spots[(x+1, y)],
                    self.spots[(x, y+1)],
                    )

    def print(self):
        for y in range(self.lims[1]+1):
            print(''.join(str(self.spots[(x, y)]) for x in range(self.lims[0]+1)))
        print()

    def tick(self, break_on_elf_death):
        for unit in list(sorted(self.units, key=my_sort)):
            res = unit.take_turn()
            
            if res == -1:
                # One side has won
                return -1
            elif res == -2 and break_on_elf_death:
                return -2

    def total_health(self):
        return sum(u.hp for u in self.units)


class GridCell:

    def __init__(self, x, y, parent_grid, contents):
        self.x = x
        self.y = y
        self.parent = parent_grid
        
        self.contents = contents
        if type(contents) is Unit:
            contents.grid_cell = self

        self.neighbors = (self, self, self, self)

    def empty_neighbors(self):
        return [n for n in self.neighbors if not n.contents]

    def __str__(self):
        if self.contents == 'wall':
            return '#'
        elif type(self.contents) is Unit:
            return 'E' if self.contents.elf else 'G'
        else:
            return '.'


class Unit:

    def __init__(self, elf):
        self.elf = elf
        self.grid_cell = None
        self.hp = 200
        self.attack_power = 3

    def take_turn(self):
        if debug:
            unit_type = 'elf' if self.elf else 'gobbo'
            print(f'beginning turn for {unit_type} at {self.grid_cell.x},{self.grid_cell.y}')

        if self.hp <= 0:
            if debug:
                print('unit is dead')
            return
        
        if self.elf:
            if not self.grid_cell.parent.gobbos:
                if debug:
                    print('no elves left')
                return -1
        else:
            if not self.grid_cell.parent.elfos:
                if debug:
                    print('no gobbos left')
                return -1
        
        if not self.next_to_target():
            # Find target square
            destination = self.find_destination()
            if destination:
                # Take a step toward it
                self.step_toward_cell(destination)
            elif debug:
                print('not moving - no destination found')
        elif debug:
            print('not moving - no need to move')

        if self.next_to_target():
            if debug:
                print('next to a target')
            # Select lowest-health target among available
            target = self.select_attack_target()

            # Attack
            self.attack(target)
            if target.elf and target.hp <= 0:
                return -2

        if debug:
            print()

    def next_to_target(self):
        return any(type(n.contents) is Unit and n.contents.elf != self.elf for n in self.grid_cell.neighbors)

    def find_destination(self):
        destinations = set()
        explored = set()
        about_to_explore = set([self.grid_cell])

        while about_to_explore:
            for c in list(about_to_explore):
                for n in c.neighbors:
                    if type(n.contents) is Unit and n.contents.elf != self.elf:
                        destinations.add(c)
                    elif n not in explored and not n.contents:
                        about_to_explore.add(n)
                explored.add(c)
                about_to_explore.remove(c)
            if destinations:
                dest = list(sorted(destinations, key=my_sort))[0]
                if debug:
                    dests = [(d.x, d.y) for d in destinations]
                    print(f'destinations found at {dests}')
                    print(f'seeking path to {dest.x},{dest.y}')
                return dest

    def step_toward_cell(self, destination):
        target = self.decide_step(destination)
        self.move(target)

    def decide_step(self, destination):
        targets = set()
        explored = set()
        about_to_explore = set([destination])

        while about_to_explore:
            for c in list(about_to_explore):
                for n in c.neighbors:
                    if n.contents is self:
                        targets.add(c)
                    elif n not in explored and not n.contents:
                        about_to_explore.add(n)
                explored.add(c)
                about_to_explore.remove(c)
            if targets:
                dest = list(sorted(targets, key=my_sort))[0]
                if debug:
                    print(f'step toward destination found at {dest.x},{dest.y}')
                return dest

        raise Exception('Couldn\'t decide which way to step toward target')

    def move(self, target):
        if target.contents:
            raise Exception('Tried to move to an occupied cell')
        
        self.grid_cell.contents = None
        self.grid_cell = target
        self.grid_cell.contents = self
        if debug:
            print(f'stepped to {target.x},{target.y}')

    def select_attack_target(self):
        options = [n.contents for n in self.grid_cell.neighbors if (n.contents and (type(n.contents) is Unit) and (n.contents.elf != self.elf))]
        if options:
            target = list(sorted(options, key = lambda u: u.hp))[0]
            if debug:
                print(f'selected attack target at {target.grid_cell.x},{target.grid_cell.y} with hp {target.hp}')
            return target

    def attack(self, target):
        target.hp -= self.attack_power
        if target.hp <= 0:
            if debug:
                print('target died')
            target.grid_cell.contents = None
            grid = self.grid_cell.parent
            grid.units.remove(target)
            if target.elf:
                grid.elfos.remove(target)
                if debug:
                    print('dead elf')
            else:
                grid.gobbos.remove(target)
