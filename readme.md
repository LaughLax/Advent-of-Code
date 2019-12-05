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
| 5|`0.315 ms`|`0.003 ms`|`0.228 ms`|`0.547 ms`|
| 4|`0.027 ms`|`413.646 ms`|`608.854 ms`|`1022.528 ms`|
| 3|`0.233 ms`|`108.803 ms`|`33.080 ms`|`142.116 ms`|
| 2|`0.177 ms`|`0.026 ms`|`152.848 ms`|`153.051 ms`|
| 1|`0.215 ms`|`0.044 ms`|`0.507 ms`|`0.766 ms`|
