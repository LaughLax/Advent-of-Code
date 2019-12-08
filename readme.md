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
| 8|`2.798 ms`|`0.093 ms`|`12.504 ms`|`15.395 ms`|
| 7|`0.280 ms`|`8.798 ms`|`71.572 ms`|`80.650 ms`|
| 6|`5.676 ms`|`3.134 ms`|`0.093 ms`|`8.903 ms`|
| 5|`0.341 ms`|`0.204 ms`|`0.422 ms`|`0.967 ms`|
| 4|`0.075 ms`|`413.933 ms`|`585.572 ms`|`999.580 ms`|
| 3|`0.185 ms`|`103.241 ms`|`35.374 ms`|`138.800 ms`|
| 2|`0.194 ms`|`0.033 ms`|`139.570 ms`|`139.797 ms`|
| 1|`0.192 ms`|`0.044 ms`|`0.497 ms`|`0.733 ms`|
