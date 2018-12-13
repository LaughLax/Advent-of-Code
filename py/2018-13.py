import time

DIR_RIGHT = 0
DIR_UP = 1
DIR_LEFT = 2
DIR_DOWN = 3


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

        self.grid = self.make_grid()
        
    def make_grid(self):
        grid = Grid(len(self.input[0]), len(self.input))
        
        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if char == '/':
                    grid.add_corner(x, y, 1)
                elif char == '\\':
                    grid.add_corner(x, y, -1)

                elif char == '+':
                    grid.add_intersection(x, y)

                elif char == '>':
                    grid.add_cart(Cart(x, y, DIR_RIGHT))
                elif char == '^':
                    grid.add_cart(Cart(x, y, DIR_UP))
                elif char == '<':
                    grid.add_cart(Cart(x, y, DIR_LEFT))
                elif char == 'v':
                    grid.add_cart(Cart(x, y, DIR_DOWN))

                elif char in ' -|':
                    pass
                else:
                    raise Exception(f'Unhandled character! ({char})')
        return grid
                        

    def part1(self):
        while not self.grid.wreck_location:
            self.grid.process_step()
        return self.grid.wreck_location
    
    def part2(self):
        self.grid = self.make_grid()

        while len(self.grid.carts) > 1:
            self.grid.process_step()
        
        last_cart = self.grid.carts.pop()
        return (last_cart.x, last_cart.y)


class Grid:

    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.corners = {}
        self.intersections = set()
        self.carts = set()

        self.wreck_location = None

    def print(self):
        chars = [[' ' for i in range(self.w)] for i in range(self.h)]

        for corner in self.corners:
            corner_type = self.corners[corner]
            if corner_type == 1:
                chars[corner[1]][corner[0]] = '/'
            else:
                chars[corner[1]][corner[0]] = '\\'

        for inter in self.intersections:
            chars[inter[1]][inter[0]] = '+'

        for cart in self.carts:
            char = {
                DIR_RIGHT: '>',
                DIR_UP: '^',
                DIR_LEFT: '<',
                DIR_DOWN: 'v',
                }.get(cart.direction)
            chars[cart.y][cart.x] = char

        for line in chars[0:10]:
            print(''.join(line))

    def add_corner(self, x, y, corner_type):
        self.corners[(x, y)] = corner_type

    def add_intersection(self, x, y):
        self.intersections.add((x, y))

    def add_cart(self, cart):
        self.carts.add(cart)

    def process_step(self):
        # Order carts for processing
        carts_ordered = list(sorted(self.carts, key=lambda c: c.y*1000 + c.x))
        
        # Process carts:
        for c in carts_ordered:
            if c.crash_location:
                continue
            
            # Move
            c.move()

            # Check for collisions
            for c2 in carts_ordered:
                if c2.crash_location or c2 is c:
                    continue
                if c.x == c2.x and c.y == c2.y:
                    c.crash_location = (c.x, c.y)
                    c2.crash_location = (c.x, c.y)
                    self.wreck_location = (c.x, c.y)
                    self.carts.remove(c)
                    self.carts.remove(c2)                    
                    break
            
            # Turn if needed
            if (c.x, c.y) in self.corners:
                corner_type = self.corners[(c.x, c.y)]
                if corner_type == 1:
                    c.direction = {
                        DIR_RIGHT: DIR_UP,
                        DIR_UP: DIR_RIGHT,
                        DIR_LEFT: DIR_DOWN,
                        DIR_DOWN: DIR_LEFT
                        }.get(c.direction)
                elif corner_type == -1:
                    c.direction = {
                        DIR_RIGHT: DIR_DOWN,
                        DIR_DOWN: DIR_RIGHT,
                        DIR_LEFT: DIR_UP,
                        DIR_UP: DIR_LEFT
                        }.get(c.direction)
            
            if (c.x, c.y) in self.intersections:
                c.turn_intersection()
                

class Cart:

    TURN_LEFT = 0
    TURN_STRAIGHT = 1
    TURN_RIGHT = 2

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.next_turn = Cart.TURN_LEFT

        self.crash_location = None

    def move(self):
        if self.direction == DIR_RIGHT:
            self.x += 1
        elif self.direction == DIR_LEFT:
            self.x -= 1
        elif self.direction == DIR_UP:
            self.y -= 1
        elif self.direction == DIR_DOWN:
            self.y += 1
        else:
            raise Exception(f'Unhandled direction! {self.direction}')

    def turn_intersection(self):
        if self.next_turn == Cart.TURN_LEFT:
            self.direction = (self.direction + 1) % 4
        elif self.next_turn == Cart.TURN_RIGHT:
            self.direction = (self.direction + 3) % 4

        self.next_turn = (self.next_turn + 1) % 3
