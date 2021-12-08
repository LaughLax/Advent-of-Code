import os.path as path
from importlib import import_module
import cProfile
import pstats


def setup(year, day):
    code = import_module(f'py.{year}-{day:02}')
    input_filename = path.join('input',f'{year}-{day:02}.txt')
    day_obj = code.AdventOfCode(input_filename)
    return day_obj


with open('days_to_run.txt') as f:
    lines = f.read().splitlines()

to_run = {}

for line in lines:
    line = line.split()
    to_run.setdefault(int(line[0]), set()).add(int(line[1]))

for year in sorted(to_run,reverse=True):
    for day in sorted(to_run[year], reverse=True):
        cProfile.run('setup(year, day)', 'profile_setup')
        day_obj = setup(year, day)

        cProfile.run('day_obj.part1()', 'profile_part1')
        p1 = day_obj.part1()

        cProfile.run('day_obj.part2()', 'profile_part2')
        p2 = day_obj.part2()

p = pstats.Stats('profile_part1')
p.strip_dirs().sort_stats(pstats.SortKey.TIME).print_stats(10).print_callers()
