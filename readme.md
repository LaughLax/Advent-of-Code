# Advent of Code

Info about Advent of Code goes here

# Benchmarking Process

To benchmark code, execution is split into 3 sections: setup, part 1 solution-finding, and part 2 solution-finding. For each section, code is first timed for one execution to get an estimate of its run-time. That estimate is used to decide how many times to repeat, aiming for about 10 seconds of work per section. Each section runs a minimum of 20 times and a maximum of 10,000.

Benchmarks are taken on one of the following 2 computers.

|Computer|Python Version|Processor|Memory|
|---:|---|---|---|
|1|3.7|To be filled|To be filled|
|2|3.6.6|i7-7600U|16 GB|

# Benchmarking Results

## Year 2019
|Day|Setup|Part 1|Part 2| Total|
|:---|---:|---:|---:|---:|
| 9|`0.352 ms`|`1.078 ms`|`1717.351 ms`|`1718.781 ms`|
| 8|`2.689 ms`|`0.083 ms`|`13.385 ms`|`16.157 ms`|
| 7|`0.241 ms`|`8.070 ms`|`63.686 ms`|`71.998 ms`|
| 6|`6.421 ms`|`3.061 ms`|`0.100 ms`|`9.582 ms`|
| 5|`0.275 ms`|`0.201 ms`|`0.398 ms`|`0.874 ms`|
| 4|`0.029 ms`|`371.153 ms`|`625.537 ms`|`996.719 ms`|
| 3|`0.202 ms`|`112.256 ms`|`31.008 ms`|`143.466 ms`|
| 2|`0.159 ms`|`0.025 ms`|`134.463 ms`|`134.647 ms`|
| 1|`0.163 ms`|`0.037 ms`|`0.477 ms`|`0.677 ms`|
