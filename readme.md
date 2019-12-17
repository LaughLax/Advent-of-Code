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
|17|`0.492 ms`|`74.842 ms`|`164.506 ms`|`239.840 ms`|
|16|`0.282 ms`|`4166.159 ms`|`1354.302 ms`|`5520.743 ms`|
|15|`0.343 ms`|`318.143 ms`|`1.524 ms`|`320.010 ms`|
|14|`0.911 ms`|`0.362 ms`|`7.569 ms`|`8.841 ms`|
|13|`0.677 ms`|`45.380 ms`|`1507.044 ms`|`1553.101 ms`|
|12|`0.172 ms`|`9.436 ms`|`1870.965 ms`|`1880.573 ms`|
|11|`0.263 ms`|`255.588 ms`|`23.574 ms`|`279.425 ms`|
|10|`0.779 ms`|`38.454 ms`|`1.483 ms`|`40.717 ms`|
| 9|`0.338 ms`|`0.519 ms`|`910.893 ms`|`911.749 ms`|
| 8|`2.583 ms`|`0.083 ms`|`11.382 ms`|`14.048 ms`|
| 7|`0.238 ms`|`6.477 ms`|`51.883 ms`|`58.599 ms`|
| 6|`4.803 ms`|`2.855 ms`|`0.082 ms`|`7.740 ms`|
| 5|`0.277 ms`|`0.139 ms`|`0.256 ms`|`0.672 ms`|
| 4|`0.027 ms`|`353.370 ms`|`543.716 ms`|`897.112 ms`|
| 3|`0.162 ms`|`94.315 ms`|`30.323 ms`|`124.800 ms`|
| 2|`0.157 ms`|`0.024 ms`|`132.162 ms`|`132.343 ms`|
| 1|`0.159 ms`|`0.035 ms`|`0.446 ms`|`0.640 ms`|
