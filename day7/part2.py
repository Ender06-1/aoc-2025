#!/usr/bin/env python3

with open("./input") as input:
    manifold = input.readlines()

    timelines = [0] * len(manifold[0])
    timelines[manifold[0].find("S")] = 1

    for line in manifold[1:]:
        for i in range(len(line)):
            if timelines[i] != 0 and line[i] == "^":
                timelines[i - 1] += timelines[i]
                timelines[i + 1] += timelines[i]
                timelines[i] = 0

    timeline_amount = sum(timelines)

    print(timeline_amount)
