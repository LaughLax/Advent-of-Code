import re


class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.original = f.read().strip()

        self.reduced = None

    @staticmethod
    def reduce(polymer):
        reduced = polymer
        while True:
            before = len(reduced)

            for char in 'abcdefghijklmnopqrstuvwxyz':
                reduced = reduced.replace(f'{char}{char.upper()}', '')
                reduced = reduced.replace(f'{char.upper()}{char}', '')

            if len(reduced) == before:
                return reduced

    def part1(self):
        self.reduced = self.reduce(self.original)

        return len(self.reduced)

    def part2(self):
        min_length = float('inf')

        for char in 'abcdefghijklmnopqrstuvwxyz':
            polymer = self.reduced
            polymer = polymer.replace(f'{char}', '')
            polymer = polymer.replace(f'{char.upper()}', '')

            length = len(self.reduce(polymer))
            if length < min_length:
                min_length = length

        return min_length
