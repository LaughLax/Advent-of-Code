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
|22|`0.238 ms`|`97.852 ms`|`0.542 ms`|`98.632 ms`|
|21|`0.577 ms`|`55.317 ms`|`1524.923 ms`|`1580.817 ms`|
|20|`67.478 ms`|`27.062 ms`|`649.818 ms`|`744.357 ms`|
|19|`0.222 ms`|`2213.218 ms`|`1197.471 ms`|`3410.911 ms`|
|18|`0.161 ms`|`4215.258 ms`|`6497.045 ms`|`10712.463 ms`|
|17|`0.430 ms`|`74.329 ms`|`163.183 ms`|`237.942 ms`|
|16|`0.277 ms`|`4088.824 ms`|`1366.543 ms`|`5455.644 ms`|
|15|`0.342 ms`|`313.992 ms`|`1.540 ms`|`315.874 ms`|
|14|`0.870 ms`|`0.352 ms`|`7.504 ms`|`8.726 ms`|
|13|`0.653 ms`|`45.507 ms`|`1489.825 ms`|`1535.984 ms`|
|12|`0.171 ms`|`9.786 ms`|`1863.530 ms`|`1873.487 ms`|
|11|`0.256 ms`|`252.778 ms`|`22.721 ms`|`275.755 ms`|
|10|`0.787 ms`|`30.115 ms`|`1.417 ms`|`32.319 ms`|
| 9|`0.334 ms`|`0.510 ms`|`898.612 ms`|`899.455 ms`|
| 8|`2.953 ms`|`0.093 ms`|`11.220 ms`|`14.266 ms`|
| 7|`0.237 ms`|`6.472 ms`|`51.487 ms`|`58.197 ms`|
| 6|`4.815 ms`|`2.803 ms`|`0.082 ms`|`7.700 ms`|
| 5|`0.281 ms`|`0.137 ms`|`0.252 ms`|`0.670 ms`|
| 4|`0.026 ms`|`361.399 ms`|`544.849 ms`|`906.273 ms`|
| 3|`0.159 ms`|`90.724 ms`|`28.502 ms`|`119.385 ms`|
| 2|`0.157 ms`|`0.025 ms`|`127.799 ms`|`127.981 ms`|
| 1|`0.165 ms`|`0.035 ms`|`0.453 ms`|`0.654 ms`|
