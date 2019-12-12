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
|12|`0.190 ms`|`8.026 ms`|`5935.377 ms`|`5943.593 ms`|
|11|`0.280 ms`|`283.935 ms`|`25.112 ms`|`309.327 ms`|
|10|`0.872 ms`|`31.609 ms`|`1.530 ms`|`34.011 ms`|
| 9|`0.366 ms`|`0.579 ms`|`1002.393 ms`|`1003.338 ms`|
| 8|`3.024 ms`|`0.095 ms`|`12.583 ms`|`15.702 ms`|
| 7|`0.277 ms`|`7.429 ms`|`58.348 ms`|`66.055 ms`|
| 6|`5.307 ms`|`3.142 ms`|`0.089 ms`|`8.538 ms`|
| 5|`0.308 ms`|`0.145 ms`|`0.262 ms`|`0.715 ms`|
| 4|`0.027 ms`|`372.785 ms`|`621.209 ms`|`994.021 ms`|
| 3|`0.181 ms`|`102.368 ms`|`31.460 ms`|`134.010 ms`|
| 2|`0.178 ms`|`0.028 ms`|`145.485 ms`|`145.690 ms`|
| 1|`0.163 ms`|`0.037 ms`|`0.481 ms`|`0.681 ms`|
