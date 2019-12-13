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
|13|`0.922 ms`|`51.867 ms`|`1552.080 ms`|`1604.868 ms`|
|12|`0.194 ms`|`7.805 ms`|`1695.367 ms`|`1703.367 ms`|
|11|`0.276 ms`|`262.300 ms`|`24.485 ms`|`287.061 ms`|
|10|`0.839 ms`|`32.833 ms`|`1.815 ms`|`35.487 ms`|
| 9|`0.474 ms`|`0.578 ms`|`1050.157 ms`|`1051.208 ms`|
| 8|`2.788 ms`|`0.083 ms`|`12.382 ms`|`15.253 ms`|
| 7|`0.242 ms`|`6.490 ms`|`52.220 ms`|`58.952 ms`|
| 6|`4.936 ms`|`2.805 ms`|`0.084 ms`|`7.824 ms`|
| 5|`0.278 ms`|`0.143 ms`|`0.257 ms`|`0.679 ms`|
| 4|`0.027 ms`|`361.978 ms`|`553.343 ms`|`915.348 ms`|
| 3|`0.164 ms`|`94.961 ms`|`31.470 ms`|`126.596 ms`|
| 2|`0.173 ms`|`0.027 ms`|`145.942 ms`|`146.141 ms`|
| 1|`0.172 ms`|`0.036 ms`|`0.460 ms`|`0.668 ms`|
