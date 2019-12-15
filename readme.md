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
|15|`0.426 ms`|`349.044 ms`|`1.633 ms`|`351.103 ms`|
|14|`0.948 ms`|`0.388 ms`|`8.478 ms`|`9.814 ms`|
|13|`0.746 ms`|`53.212 ms`|`1541.351 ms`|`1595.309 ms`|
|12|`0.174 ms`|`7.319 ms`|`1636.438 ms`|`1643.930 ms`|
|11|`0.314 ms`|`297.154 ms`|`27.638 ms`|`325.106 ms`|
|10|`0.928 ms`|`35.158 ms`|`1.708 ms`|`37.794 ms`|
| 9|`0.418 ms`|`0.596 ms`|`965.200 ms`|`966.214 ms`|
| 8|`2.685 ms`|`0.084 ms`|`13.174 ms`|`15.943 ms`|
| 7|`0.285 ms`|`7.294 ms`|`52.230 ms`|`59.809 ms`|
| 6|`5.867 ms`|`3.056 ms`|`0.086 ms`|`9.009 ms`|
| 5|`0.297 ms`|`0.154 ms`|`0.283 ms`|`0.734 ms`|
| 4|`0.040 ms`|`399.953 ms`|`639.071 ms`|`1039.064 ms`|
| 3|`0.193 ms`|`94.790 ms`|`30.596 ms`|`125.578 ms`|
| 2|`0.166 ms`|`0.026 ms`|`137.721 ms`|`137.912 ms`|
| 1|`0.170 ms`|`0.044 ms`|`0.473 ms`|`0.686 ms`|
