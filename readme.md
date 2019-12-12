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
|12|`0.256 ms`|`6.945 ms`|`2730.529 ms`|`2737.730 ms`|
|11|`0.508 ms`|`219.249 ms`|`29.593 ms`|`249.350 ms`|
|10|`0.895 ms`|`27.762 ms`|`1.634 ms`|`30.290 ms`|
| 9|`0.447 ms`|`0.537 ms`|`793.361 ms`|`794.344 ms`|
| 8|`2.862 ms`|`0.105 ms`|`11.653 ms`|`14.620 ms`|
| 7|`0.291 ms`|`7.658 ms`|`48.174 ms`|`56.123 ms`|
| 6|`5.162 ms`|`2.833 ms`|`0.120 ms`|`8.114 ms`|
| 5|`0.297 ms`|`0.223 ms`|`0.272 ms`|`0.792 ms`|
| 4|`0.021 ms`|`317.247 ms`|`492.195 ms`|`809.463 ms`|
| 3|`0.157 ms`|`87.876 ms`|`23.968 ms`|`112.001 ms`|
| 2|`0.184 ms`|`0.032 ms`|`128.940 ms`|`129.157 ms`|
| 1|`0.177 ms`|`0.062 ms`|`0.407 ms`|`0.647 ms`|
