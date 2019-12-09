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
| 9|`0.378 ms`|`0.911 ms`|`1561.828 ms`|`1563.117 ms`|
| 8|`3.684 ms`|`0.093 ms`|`15.226 ms`|`19.003 ms`|
| 7|`0.286 ms`|`6.932 ms`|`56.163 ms`|`63.382 ms`|
| 6|`5.832 ms`|`3.038 ms`|`0.084 ms`|`8.954 ms`|
| 5|`0.277 ms`|`0.142 ms`|`0.266 ms`|`0.685 ms`|
| 4|`0.028 ms`|`369.271 ms`|`607.502 ms`|`976.800 ms`|
| 3|`0.190 ms`|`111.542 ms`|`33.864 ms`|`145.597 ms`|
| 2|`0.189 ms`|`0.030 ms`|`157.432 ms`|`157.651 ms`|
| 1|`0.184 ms`|`0.039 ms`|`0.489 ms`|`0.712 ms`|
