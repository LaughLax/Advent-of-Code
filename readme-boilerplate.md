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
|15|16:08|856|19:34|224|
|14|13:14|1568|41:08|1617|
|13|13:18|766|19:52|854|
|12|31:10|2795|40:11|2002|
|11|16:36|860|19:01|801|
|10|11:33|2040|18:37|1523|
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
