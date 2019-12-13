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
|13|`1.105 ms`|`55.837 ms`|`4222.466 ms`|`4279.409 ms`|
|12|`0.204 ms`|`8.387 ms`|`1864.122 ms`|`1872.713 ms`|
|11|`0.436 ms`|`321.274 ms`|`31.899 ms`|`353.608 ms`|
|10|`1.241 ms`|`41.639 ms`|`1.760 ms`|`44.640 ms`|
| 9|`0.401 ms`|`0.615 ms`|`1080.379 ms`|`1081.394 ms`|
| 8|`3.046 ms`|`0.094 ms`|`13.201 ms`|`16.341 ms`|
| 7|`0.282 ms`|`7.965 ms`|`62.183 ms`|`70.430 ms`|
| 6|`6.826 ms`|`3.335 ms`|`0.094 ms`|`10.255 ms`|
| 5|`0.331 ms`|`0.172 ms`|`0.328 ms`|`0.831 ms`|
| 4|`0.033 ms`|`417.763 ms`|`655.456 ms`|`1073.252 ms`|
| 3|`0.257 ms`|`117.096 ms`|`32.678 ms`|`150.031 ms`|
| 2|`0.181 ms`|`0.027 ms`|`146.649 ms`|`146.858 ms`|
| 1|`0.188 ms`|`0.038 ms`|`0.503 ms`|`0.729 ms`|
