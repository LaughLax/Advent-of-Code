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
| 5|`0.442 ms`|`0.004 ms`|`0.442 ms`|`0.888 ms`|
| 4|`0.033 ms`|`447.413 ms`|`630.408 ms`|`1077.853 ms`|
| 3|`0.190 ms`|`101.143 ms`|`34.645 ms`|`135.977 ms`|
| 2|`0.192 ms`|`0.029 ms`|`158.799 ms`|`159.019 ms`|
| 1|`0.199 ms`|`0.040 ms`|`0.524 ms`|`0.763 ms`|
