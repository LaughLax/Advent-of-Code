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
|11|`0.468 ms`|`278.469 ms`|`24.321 ms`|`303.258 ms`|
|10|`0.818 ms`|`31.287 ms`|`1.509 ms`|`33.615 ms`|
| 9|`0.332 ms`|`0.540 ms`|`1085.609 ms`|`1086.480 ms`|
| 8|`3.155 ms`|`0.096 ms`|`13.082 ms`|`16.333 ms`|
| 7|`0.250 ms`|`7.062 ms`|`58.400 ms`|`65.712 ms`|
| 6|`5.843 ms`|`3.222 ms`|`0.088 ms`|`9.153 ms`|
| 5|`0.275 ms`|`0.162 ms`|`0.288 ms`|`0.725 ms`|
| 4|`0.032 ms`|`397.042 ms`|`576.685 ms`|`973.760 ms`|
| 3|`0.174 ms`|`108.535 ms`|`30.175 ms`|`138.884 ms`|
| 2|`0.160 ms`|`0.026 ms`|`136.149 ms`|`136.336 ms`|
| 1|`0.163 ms`|`0.037 ms`|`0.462 ms`|`0.661 ms`|
