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
| 4|`0.031 ms`|`384.971 ms`|`584.490 ms`|`969.491 ms`|
| 3|`0.176 ms`|`103.098 ms`|`31.603 ms`|`134.878 ms`|
| 2|`0.166 ms`|`0.026 ms`|`140.726 ms`|`140.918 ms`|
| 1|`0.189 ms`|`0.039 ms`|`0.517 ms`|`0.745 ms`|
