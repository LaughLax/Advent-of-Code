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
|18|`0.183 ms`|`5992.819 ms`|`7790.928 ms`|`13783.930 ms`|
|17|`0.457 ms`|`77.325 ms`|`173.563 ms`|`251.345 ms`|
|16|`0.296 ms`|`4231.931 ms`|`1376.991 ms`|`5609.218 ms`|
|15|`0.409 ms`|`347.678 ms`|`1.676 ms`|`349.764 ms`|
|14|`0.983 ms`|`0.420 ms`|`7.984 ms`|`9.387 ms`|
|13|`0.703 ms`|`46.403 ms`|`1500.529 ms`|`1547.634 ms`|
|12|`0.213 ms`|`10.005 ms`|`1861.941 ms`|`1872.159 ms`|
|11|`0.336 ms`|`257.320 ms`|`24.479 ms`|`282.135 ms`|
|10|`0.811 ms`|`30.832 ms`|`1.488 ms`|`33.131 ms`|
| 9|`0.331 ms`|`0.538 ms`|`916.332 ms`|`917.201 ms`|
| 8|`3.319 ms`|`0.094 ms`|`11.840 ms`|`15.253 ms`|
| 7|`0.247 ms`|`6.843 ms`|`54.310 ms`|`61.400 ms`|
| 6|`5.788 ms`|`2.937 ms`|`0.096 ms`|`8.821 ms`|
| 5|`0.270 ms`|`0.153 ms`|`0.272 ms`|`0.695 ms`|
| 4|`0.030 ms`|`358.267 ms`|`562.502 ms`|`920.799 ms`|
| 3|`0.164 ms`|`98.074 ms`|`29.716 ms`|`127.954 ms`|
| 2|`0.168 ms`|`0.033 ms`|`137.763 ms`|`137.964 ms`|
| 1|`0.202 ms`|`0.040 ms`|`0.495 ms`|`0.737 ms`|
