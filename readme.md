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
| 6|`5.410 ms`|`153.502 ms`|`41.995 ms`|`200.908 ms`|
| 5|`0.318 ms`|`0.003 ms`|`0.365 ms`|`0.686 ms`|
| 4|`0.029 ms`|`400.095 ms`|`609.903 ms`|`1010.027 ms`|
| 3|`0.168 ms`|`100.251 ms`|`32.084 ms`|`132.502 ms`|
| 2|`0.161 ms`|`0.025 ms`|`134.480 ms`|`134.666 ms`|
| 1|`0.161 ms`|`0.038 ms`|`0.481 ms`|`0.680 ms`|
