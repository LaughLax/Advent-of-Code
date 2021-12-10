import re
import numpy as np


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def part1(self):
        lines = self.input.copy()
        pair = re.compile(r'\{\}|<>|\[\]|\(\)')
        openers = re.compile(r'\{|<|\[|\(')
        total = 0
        scores = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        for line in lines:
            while True:
                if ('()' not in line
                        and '[]' not in line
                        and '{}' not in line
                        and '<>' not in line):
                    break
                line = pair.sub('', line)
            err = openers.sub('', line)
            if len(err) > 0 :
                total += scores[err[0]]
        return total

    def part2(self):
        lines = self.input.copy()
        pair = re.compile(r'\{\}|<>|\[\]|\(\)')
        all_scores = []
        scores = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4
        }
        for line in lines:
            score = 0
            while True:
                if ('()' not in line
                        and '[]' not in line
                        and '{}' not in line
                        and '<>' not in line):
                    break
                line = pair.sub('', line)
            if (')' not in line
                    and ']' not in line
                    and '}' not in line
                    and '>' not in line):
                for ch in reversed(line):
                    score *= 5
                    score += scores[ch]
                all_scores.append(score)

        all_scores = list(sorted(all_scores))
        return all_scores[int(np.floor(len(all_scores)/2))]
