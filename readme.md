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
|20|`70.050 ms`|`30.701 ms`|`3356.383 ms`|`3457.134 ms`|
|19|`0.222 ms`|`2452.910 ms`|`3671.363 ms`|`6124.496 ms`|
|18|`0.162 ms`|`6514.960 ms`|`8727.336 ms`|`15242.457 ms`|
|17|`0.428 ms`|`78.693 ms`|`174.439 ms`|`253.560 ms`|
|16|`0.305 ms`|`4356.177 ms`|`1395.182 ms`|`5751.664 ms`|
|15|`0.354 ms`|`335.002 ms`|`1.581 ms`|`336.936 ms`|
|14|`0.892 ms`|`0.379 ms`|`7.781 ms`|`9.052 ms`|
|13|`0.665 ms`|`48.482 ms`|`1573.904 ms`|`1623.052 ms`|
|12|`0.173 ms`|`9.792 ms`|`2069.908 ms`|`2079.873 ms`|
|11|`0.276 ms`|`271.642 ms`|`25.140 ms`|`297.058 ms`|
|10|`0.853 ms`|`31.947 ms`|`1.554 ms`|`34.353 ms`|
| 9|`0.395 ms`|`0.566 ms`|`973.584 ms`|`974.545 ms`|
| 8|`2.790 ms`|`0.088 ms`|`12.221 ms`|`15.099 ms`|
| 7|`0.253 ms`|`6.811 ms`|`54.385 ms`|`61.449 ms`|
| 6|`5.292 ms`|`3.085 ms`|`0.090 ms`|`8.467 ms`|
| 5|`0.293 ms`|`0.144 ms`|`0.265 ms`|`0.702 ms`|
| 4|`0.027 ms`|`387.415 ms`|`588.208 ms`|`975.650 ms`|
| 3|`0.176 ms`|`100.593 ms`|`33.298 ms`|`134.067 ms`|
| 2|`0.203 ms`|`0.031 ms`|`149.340 ms`|`149.574 ms`|
| 1|`0.181 ms`|`0.046 ms`|`0.504 ms`|`0.732 ms`|
