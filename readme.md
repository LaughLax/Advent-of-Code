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
|23|`1.738 ms`|`32.338 ms`|`565.359 ms`|`599.434 ms`|
|22|`0.237 ms`|`102.073 ms`|`0.558 ms`|`102.868 ms`|
|21|`0.577 ms`|`56.703 ms`|`1543.178 ms`|`1600.458 ms`|
|20|`68.391 ms`|`27.306 ms`|`659.198 ms`|`754.895 ms`|
|19|`0.220 ms`|`2249.695 ms`|`1213.448 ms`|`3463.363 ms`|
|18|`0.155 ms`|`4253.452 ms`|`6626.882 ms`|`10880.489 ms`|
|17|`0.433 ms`|`73.703 ms`|`166.525 ms`|`240.662 ms`|
|16|`0.279 ms`|`4192.408 ms`|`1387.841 ms`|`5580.527 ms`|
|15|`0.351 ms`|`321.135 ms`|`1.547 ms`|`323.033 ms`|
|14|`0.922 ms`|`0.368 ms`|`7.732 ms`|`9.022 ms`|
|13|`0.645 ms`|`46.081 ms`|`1510.848 ms`|`1557.574 ms`|
|12|`0.172 ms`|`9.593 ms`|`1851.850 ms`|`1861.616 ms`|
|11|`0.271 ms`|`257.306 ms`|`22.923 ms`|`280.500 ms`|
|10|`0.824 ms`|`29.953 ms`|`1.427 ms`|`32.205 ms`|
| 9|`0.329 ms`|`0.533 ms`|`953.173 ms`|`954.034 ms`|
| 8|`3.160 ms`|`0.093 ms`|`12.777 ms`|`16.030 ms`|
| 7|`0.242 ms`|`6.631 ms`|`52.287 ms`|`59.159 ms`|
| 6|`4.803 ms`|`2.821 ms`|`0.084 ms`|`7.708 ms`|
| 5|`0.274 ms`|`0.140 ms`|`0.255 ms`|`0.669 ms`|
| 4|`0.028 ms`|`361.346 ms`|`556.337 ms`|`917.711 ms`|
| 3|`0.159 ms`|`91.353 ms`|`28.844 ms`|`120.355 ms`|
| 2|`0.168 ms`|`0.026 ms`|`133.940 ms`|`134.134 ms`|
| 1|`0.166 ms`|`0.035 ms`|`0.453 ms`|`0.654 ms`|
