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
|19|`0.270 ms`|`2467.546 ms`|`3431.584 ms`|`5899.400 ms`|
|18|`0.165 ms`|`5802.654 ms`|`7887.000 ms`|`13689.819 ms`|
|17|`0.434 ms`|`73.283 ms`|`162.419 ms`|`236.136 ms`|
|16|`0.269 ms`|`4104.128 ms`|`1359.060 ms`|`5463.457 ms`|
|15|`0.344 ms`|`321.122 ms`|`1.533 ms`|`322.999 ms`|
|14|`0.914 ms`|`0.355 ms`|`7.478 ms`|`8.748 ms`|
|13|`0.697 ms`|`46.257 ms`|`1534.057 ms`|`1581.012 ms`|
|12|`0.172 ms`|`9.767 ms`|`1842.323 ms`|`1852.261 ms`|
|11|`0.266 ms`|`252.983 ms`|`23.156 ms`|`276.406 ms`|
|10|`0.795 ms`|`29.509 ms`|`1.421 ms`|`31.726 ms`|
| 9|`0.334 ms`|`0.519 ms`|`899.831 ms`|`900.684 ms`|
| 8|`2.567 ms`|`0.082 ms`|`11.184 ms`|`13.833 ms`|
| 7|`0.240 ms`|`6.475 ms`|`51.125 ms`|`57.841 ms`|
| 6|`4.656 ms`|`2.744 ms`|`0.083 ms`|`7.483 ms`|
| 5|`0.274 ms`|`0.143 ms`|`0.266 ms`|`0.683 ms`|
| 4|`0.027 ms`|`352.620 ms`|`546.292 ms`|`898.939 ms`|
| 3|`0.163 ms`|`93.843 ms`|`28.552 ms`|`122.558 ms`|
| 2|`0.159 ms`|`0.025 ms`|`126.788 ms`|`126.971 ms`|
| 1|`0.164 ms`|`0.034 ms`|`0.445 ms`|`0.642 ms`|
