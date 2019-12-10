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
|10|`0.879 ms`|`34.776 ms`|`1.742 ms`|`37.397 ms`|
| 9|`0.403 ms`|`0.563 ms`|`975.046 ms`|`976.012 ms`|
| 8|`2.737 ms`|`0.087 ms`|`12.290 ms`|`15.114 ms`|
| 7|`0.265 ms`|`7.309 ms`|`56.006 ms`|`63.580 ms`|
| 6|`5.436 ms`|`3.021 ms`|`0.098 ms`|`8.555 ms`|
| 5|`0.303 ms`|`0.158 ms`|`0.307 ms`|`0.767 ms`|
| 4|`0.034 ms`|`406.266 ms`|`599.125 ms`|`1005.426 ms`|
| 3|`0.188 ms`|`108.187 ms`|`34.458 ms`|`142.833 ms`|
| 2|`0.192 ms`|`0.026 ms`|`153.519 ms`|`153.737 ms`|
| 1|`0.178 ms`|`0.041 ms`|`0.497 ms`|`0.715 ms`|
