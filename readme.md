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
|20|`74.023 ms`|`29.377 ms`|`748.291 ms`|`851.691 ms`|
|19|`0.238 ms`|`2250.352 ms`|`3575.447 ms`|`5826.037 ms`|
|18|`0.154 ms`|`4338.412 ms`|`6658.540 ms`|`10997.106 ms`|
|17|`0.431 ms`|`74.649 ms`|`168.770 ms`|`243.850 ms`|
|16|`0.298 ms`|`4247.426 ms`|`1372.308 ms`|`5620.032 ms`|
|15|`0.350 ms`|`321.541 ms`|`1.548 ms`|`323.439 ms`|
|14|`0.869 ms`|`0.386 ms`|`8.022 ms`|`9.277 ms`|
|13|`0.648 ms`|`47.288 ms`|`1518.544 ms`|`1566.480 ms`|
|12|`0.182 ms`|`9.953 ms`|`1909.529 ms`|`1919.664 ms`|
|11|`0.263 ms`|`254.156 ms`|`23.568 ms`|`277.987 ms`|
|10|`0.822 ms`|`30.708 ms`|`1.464 ms`|`32.994 ms`|
| 9|`0.335 ms`|`0.530 ms`|`922.913 ms`|`923.777 ms`|
| 8|`2.729 ms`|`0.084 ms`|`11.493 ms`|`14.306 ms`|
| 7|`0.239 ms`|`6.600 ms`|`52.576 ms`|`59.416 ms`|
| 6|`4.914 ms`|`2.854 ms`|`0.087 ms`|`7.855 ms`|
| 5|`0.268 ms`|`0.142 ms`|`0.258 ms`|`0.668 ms`|
| 4|`0.027 ms`|`369.231 ms`|`573.123 ms`|`942.381 ms`|
| 3|`0.167 ms`|`95.857 ms`|`30.593 ms`|`126.618 ms`|
| 2|`0.159 ms`|`0.025 ms`|`134.064 ms`|`134.248 ms`|
| 1|`0.162 ms`|`0.035 ms`|`0.467 ms`|`0.664 ms`|
