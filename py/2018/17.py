class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read()

        self.grid = Grid(self.input)

    def part1(self):
        return self.grid.flood_the_earth()

    def part2(self):
        pass


class Grid:

    def __init__(self, input_str):
        self.walls = set()
        self.x_lims = [float('inf'), -float('inf')]
        self.y_lims = [float('inf'), -float('inf')]

        for line in input_str.splitlines():
            left, right = line.split(', ')
            if left.startswith('x='):
                x_range = [int(left[2:]), int(left[2:])]
                y_left, y_right = right[2:].split('..')
                y_range = [int(y_left), int(y_right)]
            else:
                y_range = [int(left[2:]), int(left[2:])]
                x_left, x_right = right[2:].split('..')
                x_range = [int(x_left), int(x_right)]

            self.x_lims[0] = x_range[0] if x_range[0] < self.x_lims[0] else self.x_lims[0]
            self.x_lims[1] = x_range[1] if x_range[1] > self.x_lims[1] else self.x_lims[1]
            self.y_lims[0] = y_range[0] if y_range[0] < self.y_lims[0] else self.y_lims[0]
            self.y_lims[1] = y_range[1] if y_range[1] > self.y_lims[1] else self.y_lims[1]

            for x in range(x_range[0], x_range[1]+1):
                for y in range(y_range[0], y_range[1]+1):
                    self.walls.add((x, y))

        self.flood = set()

    def flood_the_earth(self):
        x = 500
        y = self.y_lims[0]

        sources_to_process = [(x, y)]

        while sources_to_process:
            # Print status to file
            with open('status.txt', 'w') as f:
                for y in range(self.y_lims[0], self.y_lims[1]+1):
                    row = []
                    for x in range(self.x_lims[0], self.x_lims[1]+1):
                        if (x, y) in self.walls:
                            row.append('#')
                        elif (x, y) in self.flood:
                            row.append('~')
                        else:
                            row.append(' ')
                    print(''.join(row), file=f)
                print(file=f)

            for (x, y) in sources_to_process[:]:
                self.flood.add((x, y))
                sources_to_process.remove((x, y))

                if (x, y+1) in self.flood:
                    continue

                # Flood down
                already_flooded = False
                while (x, y+1) not in self.walls:
                    y = y+1
                    if (x, y) in self.flood:
                        already_flooded = True
                        y = y - 1
                        break
                    print(y)
                    self.flood.add((x, y))
                    if y+1 > self.y_lims[1]:
                        return

                while True:
                    x_orig = x
                    y_orig = y

                    if already_flooded:
                        hit_left_wall = False
                        while (x, y+1) in self.walls or (x, y+1) in self.flood:
                            if (x-1, y) not in self.walls:
                                x = x - 1
                            else:
                                hit_left_wall = True
                                break
                        if not hit_left_wall and (x+1, y) in self.flood or (x, y) in sources_to_process:
                            break

                        x = x_orig
                        hit_right_wall = False
                        while (x, y+1) in self.walls or (x, y+1) in self.flood:
                            if (x+1, y) not in self.walls:
                                x = x + 1
                            else:
                                hit_right_wall = True
                                break
                        if not hit_right_wall and (x-1, y) in self.flood or (x, y) in sources_to_process:
                            break

                    # Flood left
                    x = x_orig
                    y = y_orig
                    hit_left_wall = False
                    while (x, y+1) in self.walls or (x, y+1) in self.flood:
                        # If there's something beneath us, go left
                        if (x-1, y) not in self.walls:
                            x = x - 1
                            self.flood.add((x, y))
                        else:
                            hit_left_wall = True
                            break

                    if (x, y+1) not in self.walls and (x, y+1) not in self.flood:
                        sources_to_process.append((x, y))

                    # Flood right
                    x = x_orig
                    y = y_orig
                    hit_right_wall = False
                    while (x, y+1) in self.walls or (x, y+1) in self.flood:
                        # If there's something beneath us, go right
                        if (x+1, y) not in self.walls:
                            x = x + 1
                            self.flood.add((x, y))
                        else:
                            hit_right_wall = True
                            break

                    if (x, y+1) not in self.walls and (x, y+1) not in self.flood:
                        sources_to_process.append((x, y))

                    if hit_left_wall and hit_right_wall:
                        x = x_orig
                        y = y_orig - 1
                        if (x, y) not in self.flood:
                            self.flood.add((x, y))
                        print(y)
                    else:
                        break

    def print(self):
        for y in range(self.y_lims[1]+1):
            print(''.join(str(self.spots[(x, y)]) for x in range(self.lims[0]+1)))
        print()

