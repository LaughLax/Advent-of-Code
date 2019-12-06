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
| 6|`5.521 ms`|`0.001 ms`|`0.098 ms`|`5.620 ms`|
| 5|`0.337 ms`|`0.004 ms`|`0.414 ms`|`0.755 ms`|
| 4|`0.033 ms`|`424.911 ms`|`634.231 ms`|`1059.175 ms`|
| 3|`0.207 ms`|`112.835 ms`|`32.678 ms`|`145.720 ms`|
| 2|`0.190 ms`|`0.029 ms`|`156.381 ms`|`156.599 ms`|
| 1|`0.195 ms`|`0.041 ms`|`0.533 ms`|`0.769 ms`|
