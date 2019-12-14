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
|14|`0.965 ms`|`0.389 ms`|`9.048 ms`|`10.402 ms`|
|13|`0.701 ms`|`51.048 ms`|`1690.429 ms`|`1742.177 ms`|
|12|`0.197 ms`|`7.999 ms`|`1674.245 ms`|`1682.442 ms`|
|11|`0.322 ms`|`288.057 ms`|`26.094 ms`|`314.474 ms`|
|10|`0.910 ms`|`34.437 ms`|`1.706 ms`|`37.053 ms`|
| 9|`0.430 ms`|`0.634 ms`|`1052.116 ms`|`1053.180 ms`|
| 8|`3.006 ms`|`0.100 ms`|`14.218 ms`|`17.324 ms`|
| 7|`0.289 ms`|`7.576 ms`|`60.271 ms`|`68.136 ms`|
| 6|`5.290 ms`|`3.165 ms`|`0.089 ms`|`8.544 ms`|
| 5|`0.289 ms`|`0.143 ms`|`0.270 ms`|`0.703 ms`|
| 4|`0.028 ms`|`388.414 ms`|`590.489 ms`|`978.930 ms`|
| 3|`0.169 ms`|`99.886 ms`|`32.052 ms`|`132.108 ms`|
| 2|`0.165 ms`|`0.026 ms`|`142.612 ms`|`142.804 ms`|
| 1|`0.172 ms`|`0.039 ms`|`0.494 ms`|`0.706 ms`|
