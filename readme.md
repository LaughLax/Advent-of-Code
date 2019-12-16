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
|16|`0.398 ms`|`4747.957 ms`|`1518.832 ms`|`6267.186 ms`|
|15|`0.374 ms`|`352.923 ms`|`1.799 ms`|`355.096 ms`|
|14|`1.000 ms`|`0.403 ms`|`8.805 ms`|`10.208 ms`|
|13|`0.959 ms`|`54.167 ms`|`1624.070 ms`|`1679.196 ms`|
|12|`0.192 ms`|`9.455 ms`|`1923.282 ms`|`1932.929 ms`|
|11|`0.281 ms`|`278.294 ms`|`25.050 ms`|`303.624 ms`|
|10|`0.829 ms`|`32.312 ms`|`1.596 ms`|`34.738 ms`|
| 9|`0.359 ms`|`0.590 ms`|`1001.371 ms`|`1002.320 ms`|
| 8|`2.922 ms`|`0.099 ms`|`13.242 ms`|`16.263 ms`|
| 7|`0.277 ms`|`7.216 ms`|`56.903 ms`|`64.396 ms`|
| 6|`5.300 ms`|`3.074 ms`|`0.092 ms`|`8.466 ms`|
| 5|`0.317 ms`|`0.161 ms`|`0.308 ms`|`0.786 ms`|
| 4|`0.029 ms`|`385.082 ms`|`587.377 ms`|`972.488 ms`|
| 3|`0.192 ms`|`102.077 ms`|`31.585 ms`|`133.853 ms`|
| 2|`0.169 ms`|`0.026 ms`|`149.843 ms`|`150.038 ms`|
| 1|`0.165 ms`|`0.039 ms`|`0.493 ms`|`0.697 ms`|
