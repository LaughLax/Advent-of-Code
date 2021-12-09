# Advent of Code

Advent of Code is an annual online coding challenge that presents 25 problems, one each day December 1 through Christmas.
Each problem has two parts; the second part is only revealed once the first has been completed.
They tend to get harder as the calendar progresses, with some problems building on previous ones.
The challenges are language-agnostic, and the creator guarantees that a solution exists for each that could run on older hardware.
I participated in real time beginning in 2018.
Starting in 2019, I tried to complete the problem as fast as possible in real time.
My rank and completion time (starting when the problem was released) is listed in the table below from 2019 onward; times for Part 2 include time spent on Part 1.
Since problems release at midnight EST, solution times longer than several hours include time spent sleeping.
After finding a solution, I've adjusted many of my scripts to execute faster.
Sometimes this has meant finding a more elegant way to solve the problem, and sometimes it's just meant improving my code.

## Completion Time and Ranking

#### Year 2021

|Day|Part 1 Time|Part 1 Rank|Part 2 Time|Part 2 Rank|
|---:|---:|:---:|---:|:---:|
|09|20:54|4889|36:33|2591|
|08|7:13|820|36:13|675|
|07|51:47|12051|1:01:14|11167|
|06|11:48:06|44115|12:08:52|37451|
|05|17:59:05|47405|18:17:31|44455|
|04|34:41|3220|38:28|2395|
|03|8:57|2343|32:47|2893|
|02|2:42|725|04:32|642|
|01|2:35|1080|06:28|1111|

#### Year 2020

|Day|Part 1 Time|Part 1 Rank|Part 2 Time|Part 2 Rank|
|---:|---:|:---:|---:|:---:|
|25|9:47|274|10:01|233|
|24|7:26|121|37:49|911|
|23|14:34|250|33:04|**54**|
|22|8:04|681|41:51|950|
|21|27:02|919|30:02|651|
|20|1:25:36|1987|14:23:12|4275|
|19|50:44|1448|1:32:44|1263|
|18|36:57|1936|10:56:54|11433|
|17|23:35|789|29:09|748|
|16|11:35|593|30:26|372|
|15|9:13|385|11:24|186|
|14|11:20|451|22:04|250|
|13|9:27|1550|38:48|759|
|12|8:52|583|29:39|1538|
|11|20:01|1102|35:33|1211|
|10|7:16|1036|13:09|302|
|09|5:57|693|12:26|806|
|08|5:17|513|19:25|1548|
|07|43:53|3947|48:42|2418|
|06|5:29|1322|10:03|1122|
|05|4:44|192|6:56|187|
|04|9:28|1282|24:59|786|
|03|3:02|166|6:40|297|
|02|5:14|765|9:37|958|
|01|9:33|1693|11:09|1430|

#### Year 2019

|Day|Part 1 Time|Part 1 Rank|Part 2 Time|Part 2 Rank|
|---:|---:|:---:|---:|:---:|
|25|50:19|244|50:43|187|
|24|21:15|366|56:34|205|
|23|14:15|137|29:11|189|
|22|34:35|524|3:20:28|296|
|21|31:22|361|4:09:37|987|
|20|56:32|392|1:51:47|390|
|19|1:24:12|1426|2:16:49|976|
|18|8:00:49|833|9:20:22|610|
|17|14:39|434|38:35|**51**|
|16|18:26|338|1:28:58|249|
|15|39:30|206|52:100|186|
|14|51:24|381|1:11:36|344|
|13|15:46|1348|48:03|655|
|12|16:18|310|1:25:14|736|
|11|9:30|**62**|16:41|114|
|10|15:18|128|1:14:24|405|
|09|21:06|256|21:50|244|
|08|12:08|818|17:00|354|
|07|27:37|965|51:39|373|
|06|22:57|1278|34:28|966|
|05|16:17|124|31:54|294|
|04|8:46|1102|20:20|1151|
|03|1:36:12|3137|1:45:59|2464|
|02|7:35|177|12:42|174|
|01|2:46|471|18:21|1169|

## Benchmarks

### Process

To benchmark code, execution is split into 3 sections: setup, part 1 solution-finding, and part 2 solution-finding. For each section, code is first timed for one execution to get an estimate of its run-time.
That estimate is used to decide how many times to repeat, aiming for about 10 seconds of work per section. Each section runs a minimum of 20 times and a maximum of 10,000.

Benchmarks are taken on one of the following 2 computers.

|Computer|Python Version|Processor|Memory|
|---:|---|---|---|
|1|3.7|Intel i5-6300HQ 2.3 GHz|8 GB|
|2|3.6.6|Intel i7-7600U|16 GB|

### Results

#### Year 2020
|Day|Setup|Part 1|Part 2| Total|
|:---|---:|---:|---:|---:|
|25|`0.130 ms`|`1388.260 ms`|`0.000 ms`|`1388.390 ms`|
|24|`0.217 ms`|`2.373 ms`|`116.771 ms`|`119.362 ms`|
|23|`0.129 ms`|`0.172 ms`|`17370.137 ms`|`17370.438 ms`|
|22|`0.145 ms`|`0.104 ms`|`1465.073 ms`|`1465.321 ms`|
|21|`0.192 ms`|`23.035 ms`|`0.002 ms`|`23.229 ms`|
|20|`1.081 ms`|`56.196 ms`|`20.263 ms`|`77.540 ms`|
|19|`0.757 ms`|`6.555 ms`|`24.646 ms`|`31.958 ms`|
|18|`0.237 ms`|`5.075 ms`|`9.039 ms`|`14.350 ms`|
|17|`0.125 ms`|`102.707 ms`|`3845.840 ms`|`3948.671 ms`|
|16|`1.572 ms`|`2.073 ms`|`20.485 ms`|`24.130 ms`|
|15|`0.131 ms`|`0.391 ms`|`10869.275 ms`|`10869.797 ms`|
|14|`0.231 ms`|`1.422 ms`|`52.121 ms`|`53.775 ms`|
|13|`0.139 ms`|`0.002 ms`|`0.326 ms`|`0.468 ms`|
|12|`0.433 ms`|`0.243 ms`|`0.320 ms`|`0.996 ms`|
|11|`70.044 ms`|`268.584 ms`|`547.199 ms`|`885.827 ms`|
|10|`0.162 ms`|`0.016 ms`|`0.253 ms`|`0.431 ms`|
| 9|`0.454 ms`|`5.627 ms`|`9.996 ms`|`16.077 ms`|
| 8|`0.573 ms`|`0.076 ms`|`2.545 ms`|`3.194 ms`|
| 7|`4.562 ms`|`0.076 ms`|`0.022 ms`|`4.660 ms`|
| 6|`0.291 ms`|`0.702 ms`|`1.392 ms`|`2.385 ms`|
| 5|`0.639 ms`|`0.021 ms`|`0.084 ms`|`0.744 ms`|
| 4|`1.330 ms`|`0.131 ms`|`0.709 ms`|`2.171 ms`|
| 3|`0.192 ms`|`0.192 ms`|`0.845 ms`|`1.228 ms`|
| 2|`0.290 ms`|`1.112 ms`|`1.013 ms`|`2.416 ms`|
| 1|`0.191 ms`|`0.145 ms`|`0.137 ms`|`0.473 ms`|
#### Year 2019
|Day|Setup|Part 1|Part 2| Total|
|:---|---:|---:|---:|---:|
|25|`1.169 ms`|`210.730 ms`|`0.000 ms`|`211.899 ms`|
|24|`0.131 ms`|`2.484 ms`|`594.303 ms`|`596.918 ms`|
|23|`1.533 ms`|`27.462 ms`|`486.581 ms`|`515.575 ms`|
|22|`0.211 ms`|`87.862 ms`|`0.524 ms`|`88.596 ms`|
|21|`0.567 ms`|`55.523 ms`|`1538.094 ms`|`1594.184 ms`|
|20|`66.893 ms`|`26.780 ms`|`659.781 ms`|`753.454 ms`|
|19|`0.237 ms`|`2220.121 ms`|`1200.331 ms`|`3420.690 ms`|
|18|`0.169 ms`|`4274.146 ms`|`6588.886 ms`|`10863.201 ms`|
|17|`0.433 ms`|`74.080 ms`|`165.826 ms`|`240.339 ms`|
|16|`0.292 ms`|`4212.030 ms`|`1062.623 ms`|`5274.944 ms`|
|15|`0.350 ms`|`319.773 ms`|`1.545 ms`|`321.668 ms`|
|14|`0.886 ms`|`0.375 ms`|`7.893 ms`|`9.154 ms`|
|13|`0.655 ms`|`45.901 ms`|`1486.941 ms`|`1533.498 ms`|
|12|`0.178 ms`|`7.552 ms`|`1637.244 ms`|`1644.975 ms`|
|11|`0.287 ms`|`254.057 ms`|`23.340 ms`|`277.685 ms`|
|10|`0.812 ms`|`30.216 ms`|`1.486 ms`|`32.513 ms`|
| 9|`0.335 ms`|`0.525 ms`|`916.199 ms`|`917.059 ms`|
| 8|`2.593 ms`|`0.082 ms`|`11.684 ms`|`14.360 ms`|
| 7|`0.248 ms`|`6.933 ms`|`54.701 ms`|`61.882 ms`|
| 6|`4.986 ms`|`2.857 ms`|`0.083 ms`|`7.926 ms`|
| 5|`0.281 ms`|`0.138 ms`|`0.256 ms`|`0.675 ms`|
| 4|`0.030 ms`|`358.423 ms`|`545.278 ms`|`903.732 ms`|
| 3|`0.171 ms`|`101.306 ms`|`29.132 ms`|`130.609 ms`|
| 2|`0.164 ms`|`0.025 ms`|`131.814 ms`|`132.003 ms`|
| 1|`0.162 ms`|`0.035 ms`|`0.445 ms`|`0.643 ms`|
#### Year 2018
|Day|Setup|Part 1|Part 2| Total|
|:---|---:|---:|---:|---:|
|18|`0.136 ms`|`61.361 ms`|`9339.890 ms`|`9401.386 ms`|
|16|`4.396 ms`|`8.173 ms`|`2.860 ms`|`15.429 ms`|
|15|`1.758 ms`|`402.547 ms`|`1341.214 ms`|`1745.520 ms`|
|14|`0.130 ms`|`591.812 ms`|`12697.089 ms`|`13289.031 ms`|
|13|`0.235 ms`|`24.236 ms`|`161.376 ms`|`185.846 ms`|
|12|`0.146 ms`|`1.425 ms`|`8.416 ms`|`9.987 ms`|
|11|`0.125 ms`|`225.404 ms`|`11322.879 ms`|`11548.409 ms`|
|10|`0.882 ms`|`6.651 ms`|`0.000 ms`|`7.533 ms`|
| 9|`0.142 ms`|`63.945 ms`|`8843.011 ms`|`8907.098 ms`|
| 8|`10.815 ms`|`1.142 ms`|`0.550 ms`|`12.507 ms`|
| 7|`0.349 ms`|`1.331 ms`|`1.600 ms`|`3.280 ms`|
| 6|`0.216 ms`|`1396.633 ms`|`1988.474 ms`|`3385.324 ms`|
| 5|`0.279 ms`|`92.498 ms`|`358.598 ms`|`451.375 ms`|
| 4|`3.982 ms`|`0.006 ms`|`0.009 ms`|`3.996 ms`|
| 3|`3.995 ms`|`847.821 ms`|`569.229 ms`|`1421.045 ms`|
| 2|`0.170 ms`|`2.643 ms`|`8.107 ms`|`10.920 ms`|
| 1|`0.372 ms`|`0.013 ms`|`23.561 ms`|`23.947 ms`|
#### Year 2017
|Day|Setup|Part 1|Part 2| Total|
|:---|---:|---:|---:|---:|
| 9|`6.280 ms`|`1.065 ms`|`1.875 ms`|`9.221 ms`|
| 8|`2.065 ms`|`0.459 ms`|`0.627 ms`|`3.150 ms`|
| 7|`2.890 ms`|`0.558 ms`|`0.015 ms`|`3.463 ms`|
| 6|`0.133 ms`|`60.241 ms`|`60.885 ms`|`121.259 ms`|
| 5|`0.367 ms`|`114.680 ms`|`8967.913 ms`|`9082.960 ms`|
| 4|`0.273 ms`|`1.242 ms`|`5.241 ms`|`6.755 ms`|
| 3|`0.125 ms`|`0.001 ms`|`0.277 ms`|`0.403 ms`|
| 2|`0.201 ms`|`0.018 ms`|`0.486 ms`|`0.705 ms`|
| 1|`0.496 ms`|`0.293 ms`|`0.299 ms`|`1.088 ms`|
