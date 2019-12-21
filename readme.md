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
|21|`0.563 ms`|`54.688 ms`|`1514.953 ms`|`1570.204 ms`|
|20|`66.102 ms`|`27.028 ms`|`641.007 ms`|`734.137 ms`|
|19|`0.220 ms`|`2207.593 ms`|`1178.112 ms`|`3385.925 ms`|
|18|`0.161 ms`|`4190.685 ms`|`6443.833 ms`|`10634.679 ms`|
|17|`0.438 ms`|`73.096 ms`|`166.519 ms`|`240.054 ms`|
|16|`0.274 ms`|`4119.622 ms`|`1338.415 ms`|`5458.312 ms`|
|15|`0.340 ms`|`317.084 ms`|`1.523 ms`|`318.947 ms`|
|14|`0.895 ms`|`0.364 ms`|`7.680 ms`|`8.939 ms`|
|13|`0.667 ms`|`46.002 ms`|`1476.477 ms`|`1523.146 ms`|
|12|`0.170 ms`|`9.323 ms`|`1883.003 ms`|`1892.496 ms`|
|11|`0.262 ms`|`249.644 ms`|`22.845 ms`|`272.751 ms`|
|10|`0.808 ms`|`30.560 ms`|`1.449 ms`|`32.817 ms`|
| 9|`0.329 ms`|`0.517 ms`|`899.850 ms`|`900.697 ms`|
| 8|`2.635 ms`|`0.082 ms`|`11.334 ms`|`14.051 ms`|
| 7|`0.239 ms`|`6.495 ms`|`52.550 ms`|`59.284 ms`|
| 6|`5.362 ms`|`2.867 ms`|`0.086 ms`|`8.315 ms`|
| 5|`0.276 ms`|`0.138 ms`|`0.261 ms`|`0.674 ms`|
| 4|`0.026 ms`|`367.570 ms`|`546.904 ms`|`914.500 ms`|
| 3|`0.163 ms`|`93.080 ms`|`28.920 ms`|`122.163 ms`|
| 2|`0.154 ms`|`0.025 ms`|`129.681 ms`|`129.860 ms`|
| 1|`0.162 ms`|`0.035 ms`|`0.449 ms`|`0.646 ms`|
