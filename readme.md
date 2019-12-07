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
| 7|`0.452 ms`|`8.790 ms`|`63.485 ms`|`72.726 ms`|
| 6|`6.385 ms`|`6.036 ms`|`0.161 ms`|`12.582 ms`|
| 5|`0.461 ms`|`0.366 ms`|`0.917 ms`|`1.745 ms`|
| 4|`0.032 ms`|`489.307 ms`|`628.955 ms`|`1118.294 ms`|
| 3|`0.178 ms`|`109.712 ms`|`32.516 ms`|`142.406 ms`|
| 2|`0.158 ms`|`0.026 ms`|`140.431 ms`|`140.615 ms`|
| 1|`0.187 ms`|`0.042 ms`|`0.505 ms`|`0.734 ms`|
