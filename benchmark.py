import os.path as path
from importlib import import_module
import timeit

MAX_RUNS = 100_000
MIN_RUNS = 10
TIME_GOAL = 20 * 1000


def setup(y, d):
    code = import_module(f'py.{y}.{d:02}')
    input_filename = path.join('input', f'{y}', f'{d:02}.txt')
    d_obj = code.AdventOfCode(input_filename)
    return d_obj


def time_line(code):

    # Run once for rough estimate of time
    t = timeit.timeit(code, number=1, globals=globals()) * 1000

    # Aim for TIME_GOAL seconds of benchmarking (set above).
    # Minimum and maximum run counts also set above.
    num = max(MIN_RUNS, min(int(TIME_GOAL / t), MAX_RUNS))

    return timeit.timeit(code, number=num, globals=globals()) / num * 1000


with open('days_to_run.txt') as f:
    lines = f.read().splitlines()

output_file = 'readme.md'

with open(output_file, 'w') as f:
    with open('readme-boilerplate.md', 'r') as boilerplate:
        f.write(boilerplate.read())
    f.write(f'That estimate is used to decide how many times to repeat, aiming for \
about {TIME_GOAL / 1000:.0f} seconds of work per section. ')
    f.write(f'Each section runs a minimum of {MIN_RUNS:d} times \
and a maximum of {MAX_RUNS:,d}.\n\n')
    f.write('Benchmarks are taken on one of the following 2 computers.\n\n')
    f.write('|Computer|Python Version|Processor|Memory|\n')
    f.write('|---:|---|---|---|\n')
    f.write('|1|3.7|Intel i5-6300HQ 2.3 GHz|8 GB|\n')
    f.write('|2|3.6.6|Intel i7-7600U|16 GB|\n\n')

    f.write('### Results\n\n')

to_run = {}

for line in lines:
    line = line.split()
    to_run.setdefault(int(line[0]), set()).add(int(line[1]))

t_total = 0
for year in sorted(to_run, reverse=True):
    with open(output_file, 'a') as f:
        f.write(f'#### Year {year}\n')
        f.write('|Day|Setup|Part 1|Part 2| Total|\n')
        f.write('|:---|---:|---:|---:|---:|\n')

    for day in sorted(to_run[year], reverse=True):
        print(f'{year} Advent of Code - Day {day:2}\n')
        with open(output_file, 'a') as f:
            f.write(f'|{day:2}|')

        t0 = time_line('setup(year, day)')
        day_obj = setup(year, day)
        print(f"Setup:  {t0:9.3f}ms")
        with open(output_file, 'a') as f:
            f.write(f"`{t0:.3f} ms`|")

        t1 = time_line('day_obj.part1()')
        p1 = day_obj.part1()
        print(f"Part 1: {t1:9.3f}ms")
        with open(output_file, 'a') as f:
            f.write(f"`{t1:.3f} ms`|")

        t2 = time_line('day_obj.part2()')
        p2 = day_obj.part2()
        print(f"Part 2: {t2:9.3f}ms")
        print(f"Total:  {(t0+t1+t2):9.3f}ms\n")
        t_total += t0 + t1 + t2
        with open(output_file, 'a') as f:
            f.write(f"`{t2:.3f} ms`|")

            f.write(f"`{(t0+t1+t2):.3f} ms`|\n")

    with open(output_file, 'a') as f:
        f.write('\n')

print(f'Total (benchmarked) time: {(t_total/1000):.3f}s')
