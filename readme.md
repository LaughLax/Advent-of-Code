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
|12|`0.186 ms`|`32.761 ms`|`14713.392 ms`|`14746.340 ms`|
|11|`0.272 ms`|`280.569 ms`|`24.879 ms`|`305.720 ms`|
|10|`0.857 ms`|`32.395 ms`|`1.556 ms`|`34.807 ms`|
| 9|`0.355 ms`|`0.556 ms`|`988.934 ms`|`989.845 ms`|
| 8|`2.641 ms`|`0.084 ms`|`11.948 ms`|`14.673 ms`|
| 7|`0.253 ms`|`6.841 ms`|`56.625 ms`|`63.719 ms`|
| 6|`4.864 ms`|`2.963 ms`|`0.087 ms`|`7.914 ms`|
| 5|`0.274 ms`|`0.146 ms`|`0.264 ms`|`0.684 ms`|
| 4|`0.031 ms`|`372.095 ms`|`584.063 ms`|`956.189 ms`|
| 3|`0.171 ms`|`98.119 ms`|`32.538 ms`|`130.828 ms`|
| 2|`0.170 ms`|`0.027 ms`|`141.100 ms`|`141.297 ms`|
| 1|`0.157 ms`|`0.037 ms`|`0.488 ms`|`0.683 ms`|
