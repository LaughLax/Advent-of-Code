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
| 4|`0.098 ms`|`749.768 ms`|`968.990 ms`|`1718.856 ms`|
| 3|`0.212 ms`|`102.636 ms`|`30.697 ms`|`133.546 ms`|
| 2|`0.174 ms`|`0.026 ms`|`140.799 ms`|`140.999 ms`|
| 1|`0.210 ms`|`0.043 ms`|`0.522 ms`|`0.774 ms`|
