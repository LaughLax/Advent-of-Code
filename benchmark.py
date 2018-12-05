import os.path as path
from importlib import import_module
import timeit


def setup(year, day):
    code = import_module(f'py.{year}-{day:02}')
    input_filename = path.join('input',f'{year}-{day:02}.txt')
    day_obj = code.AdventOfCode(input_filename)
    return day_obj


def time_line(line):

    # Run once for rough estimate of time
    t = timeit.timeit(line, number=1, globals=globals()) * 1000

    # Aim for 10 seconds of benchmarking.
    # Minimum 20 runs, maximum 10,000.
    num = max(20, min(int(10000 / t), 10000))

    return timeit.timeit(line, number=num, globals=globals()) / num * 1000


with open('days_to_run.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split()
        year = int(line[0])
        day = int(line[1])

        print(f'{year} Advent of Code - Day {day:2}')

        t0 = time_line('setup(year, day)')
        day_obj = setup(year, day)
        print(f"Setup:  {t0:.9f}ms")

        t1 = time_line('day_obj.part1()')
        p1 = day_obj.part1()
        print(f"Part 1: {t1:.9f}ms")

        t2 = time_line('day_obj.part2()')
        p2 = day_obj.part2()
        print(f"Part 2: {t2:.9f}ms")

        print(f"Total:  {(t0+t1+t2):.9f}ms\n")
