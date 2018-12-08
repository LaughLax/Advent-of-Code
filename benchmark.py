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

output_file = 'readme.md'

with open(output_file,'w') as f:
    f.write('# Advent of Code\n\n')
    f.write('Info about Advent of Code goes here\n\n')
    f.write('# Benchmarking Results\n\n')
    f.write('Info about my benchmarks goes here\n\n')

to_run = {}

for line in lines:
    line = line.split()
    to_run.setdefault(int(line[0]), set()).add(int(line[1]))

for year in sorted(to_run,reverse=True):
    with open(output_file,'a') as f:
        f.write(f'## Year {year}\n')
        f.write('|Day|Setup|Part 1|Part 2| Total|\n')
        f.write('|:---|---:|---:|---:|---:|\n')

    for day in sorted(to_run[year], reverse=True):
        with open(output_file,'a') as f:
            f.write(f'|{day:2}|')

        t0 = time_line('setup(year, day)')
        day_obj = setup(year, day)
        with open(output_file,'a') as f:
            f.write(f"`{t0:.3f} ms`|")

        t1 = time_line('day_obj.part1()')
        p1 = day_obj.part1()
        with open(output_file,'a') as f:
            f.write(f"`{t1:.3f} ms`|")

        t2 = time_line('day_obj.part2()')
        p2 = day_obj.part2()
        with open(output_file,'a') as f:
            f.write(f"`{t2:.3f} ms`|")

            f.write(f"`{(t0+t1+t2):.3f} ms`|\n")

