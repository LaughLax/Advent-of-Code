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
|24|`0.164 ms`|`2.741 ms`|`644.826 ms`|`647.732 ms`|
|23|`2.119 ms`|`29.563 ms`|`505.876 ms`|`537.559 ms`|
|22|`0.205 ms`|`89.241 ms`|`0.523 ms`|`89.969 ms`|
|21|`0.556 ms`|`54.139 ms`|`1511.866 ms`|`1566.562 ms`|
|20|`67.792 ms`|`27.240 ms`|`659.124 ms`|`754.156 ms`|
|19|`0.217 ms`|`2267.399 ms`|`1336.304 ms`|`3603.920 ms`|
|18|`0.157 ms`|`4360.283 ms`|`6628.197 ms`|`10988.637 ms`|
|17|`0.438 ms`|`74.124 ms`|`166.196 ms`|`240.758 ms`|
|16|`0.273 ms`|`4237.279 ms`|`1384.874 ms`|`5622.425 ms`|
|15|`0.347 ms`|`325.018 ms`|`1.554 ms`|`326.920 ms`|
|14|`0.889 ms`|`0.366 ms`|`7.647 ms`|`8.902 ms`|
|13|`0.670 ms`|`46.585 ms`|`1508.195 ms`|`1555.450 ms`|
|12|`0.181 ms`|`9.824 ms`|`1931.967 ms`|`1941.972 ms`|
|11|`0.267 ms`|`262.052 ms`|`23.803 ms`|`286.122 ms`|
|10|`0.781 ms`|`30.159 ms`|`1.437 ms`|`32.376 ms`|
| 9|`0.334 ms`|`0.529 ms`|`919.524 ms`|`920.388 ms`|
| 8|`2.697 ms`|`0.083 ms`|`11.782 ms`|`14.563 ms`|
| 7|`0.241 ms`|`6.743 ms`|`53.027 ms`|`60.011 ms`|
| 6|`4.870 ms`|`2.856 ms`|`0.087 ms`|`7.813 ms`|
| 5|`0.284 ms`|`0.142 ms`|`0.262 ms`|`0.688 ms`|
| 4|`0.028 ms`|`364.576 ms`|`553.410 ms`|`918.013 ms`|
| 3|`0.165 ms`|`92.252 ms`|`29.515 ms`|`121.932 ms`|
| 2|`0.157 ms`|`0.025 ms`|`131.395 ms`|`131.577 ms`|
| 1|`0.161 ms`|`0.035 ms`|`0.450 ms`|`0.646 ms`|
