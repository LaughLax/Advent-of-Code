import os.path as path
from importlib import import_module
import time

with open('days_to_run.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split()
        year = int(line[0])
        day = int(line[1])

        print(f'{year} Advent of Code - Day {day:2}\n')

        t = time.time()

        code = import_module(f'py.{year}-{day:02}')
        if len(line) > 2:
            input_filename = path.join('input',f'{year}-{day:02}-example.txt')
        else:
            input_filename = path.join('input',f'{year}-{day:02}.txt')

        day_obj = code.AdventOfCode(input_filename)
        t0 = (time.time() - t) * 1000

        t1 = time.time()
        p1 = day_obj.part1()
        t1 = (time.time() - t1) * 1000

        t2 = time.time()
        p2 = day_obj.part2()
        t2 = (time.time() - t2) * 1000

        t = (time.time() - t) * 1000

        print(f"Part 1: {p1}")
        print(f"Part 2: {p2}\n")
        print(f"Setup:  {t0:8.3f}ms")
        print(f"Part 1: {t1:8.3f}ms")
        print(f"Part 2: {t2:8.3f}ms")
        print(f"Total:  {t:8.3f}ms\n")
