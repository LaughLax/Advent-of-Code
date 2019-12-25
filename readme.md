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
|25|`1.205 ms`|`206.054 ms`|`0.000 ms`|`207.260 ms`|
|24|`0.125 ms`|`2.481 ms`|`601.334 ms`|`603.939 ms`|
|23|`1.644 ms`|`27.581 ms`|`489.231 ms`|`518.455 ms`|
|22|`0.205 ms`|`87.331 ms`|`0.526 ms`|`88.062 ms`|
|21|`0.575 ms`|`55.324 ms`|`1523.905 ms`|`1579.805 ms`|
|20|`66.725 ms`|`26.865 ms`|`646.678 ms`|`740.268 ms`|
|19|`0.223 ms`|`2208.060 ms`|`1196.439 ms`|`3404.722 ms`|
|18|`0.159 ms`|`4156.084 ms`|`6537.952 ms`|`10694.194 ms`|
|17|`0.433 ms`|`74.196 ms`|`167.279 ms`|`241.908 ms`|
|16|`0.271 ms`|`4164.995 ms`|`1343.133 ms`|`5508.399 ms`|
|15|`0.346 ms`|`319.158 ms`|`1.509 ms`|`321.013 ms`|
|14|`0.913 ms`|`0.367 ms`|`7.695 ms`|`8.976 ms`|
|13|`0.678 ms`|`45.495 ms`|`1476.501 ms`|`1522.675 ms`|
|12|`0.173 ms`|`7.207 ms`|`1550.845 ms`|`1558.225 ms`|
|11|`0.261 ms`|`253.743 ms`|`23.473 ms`|`277.476 ms`|
|10|`0.796 ms`|`29.792 ms`|`1.423 ms`|`32.011 ms`|
| 9|`0.337 ms`|`0.516 ms`|`906.178 ms`|`907.031 ms`|
| 8|`2.578 ms`|`0.083 ms`|`11.465 ms`|`14.126 ms`|
| 7|`0.238 ms`|`6.559 ms`|`52.800 ms`|`59.597 ms`|
| 6|`4.848 ms`|`2.857 ms`|`0.082 ms`|`7.787 ms`|
| 5|`0.282 ms`|`0.139 ms`|`0.260 ms`|`0.680 ms`|
| 4|`0.027 ms`|`354.607 ms`|`555.923 ms`|`910.556 ms`|
| 3|`0.166 ms`|`93.267 ms`|`28.557 ms`|`121.991 ms`|
| 2|`0.158 ms`|`0.024 ms`|`128.836 ms`|`129.017 ms`|
| 1|`0.161 ms`|`0.036 ms`|`0.447 ms`|`0.644 ms`|
## Year 2018
|Day|Setup|Part 1|Part 2| Total|
|:---|---:|---:|---:|---:|
|18|`0.129 ms`|`61.748 ms`|`9437.399 ms`|`9499.276 ms`|
|16|`4.425 ms`|`8.344 ms`|`2.925 ms`|`15.694 ms`|
|15|`1.744 ms`|`412.830 ms`|`1354.825 ms`|`1769.399 ms`|
|14|`0.117 ms`|`589.556 ms`|`12897.880 ms`|`13487.553 ms`|
|13|`0.228 ms`|`24.656 ms`|`158.543 ms`|`183.428 ms`|
|12|`0.137 ms`|`1.423 ms`|`8.439 ms`|`9.999 ms`|
|11|`0.117 ms`|`227.615 ms`|`11305.483 ms`|`11533.215 ms`|
|10|`0.837 ms`|`6.686 ms`|`0.000 ms`|`7.523 ms`|
| 9|`0.141 ms`|`63.971 ms`|`8733.986 ms`|`8798.099 ms`|
| 8|`10.813 ms`|`1.155 ms`|`0.537 ms`|`12.504 ms`|
| 7|`0.349 ms`|`1.297 ms`|`1.588 ms`|`3.234 ms`|
| 6|`0.212 ms`|`1394.147 ms`|`1923.035 ms`|`3317.394 ms`|
| 5|`0.273 ms`|`91.849 ms`|`357.352 ms`|`449.474 ms`|
| 4|`3.944 ms`|`0.005 ms`|`0.008 ms`|`3.957 ms`|
| 3|`3.988 ms`|`862.497 ms`|`560.968 ms`|`1427.453 ms`|
| 2|`0.161 ms`|`2.622 ms`|`8.526 ms`|`11.309 ms`|
| 1|`0.372 ms`|`0.013 ms`|`26.197 ms`|`26.583 ms`|
## Year 2017
|Day|Setup|Part 1|Part 2| Total|
|:---|---:|---:|---:|---:|
| 9|`6.490 ms`|`1.109 ms`|`1.895 ms`|`9.493 ms`|
| 8|`2.099 ms`|`0.455 ms`|`0.619 ms`|`3.174 ms`|
| 7|`2.946 ms`|`0.537 ms`|`0.015 ms`|`3.498 ms`|
| 6|`0.133 ms`|`59.267 ms`|`60.121 ms`|`119.521 ms`|
| 5|`0.374 ms`|`113.487 ms`|`8841.683 ms`|`8955.544 ms`|
| 4|`0.258 ms`|`1.169 ms`|`5.200 ms`|`6.627 ms`|
| 3|`0.122 ms`|`0.001 ms`|`0.274 ms`|`0.398 ms`|
| 2|`0.192 ms`|`0.018 ms`|`0.489 ms`|`0.699 ms`|
| 1|`0.496 ms`|`0.294 ms`|`0.299 ms`|`1.088 ms`|
