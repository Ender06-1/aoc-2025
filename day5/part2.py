#!/usr/bin/env python3


with open("./input") as input:
    raw_database = input.read().split("\n\n")
    intervals = sorted(
        list(map(int, inter.split("-"))) for inter in raw_database[0].split()
    )

    merged_intervals = [intervals[0]]

    for inter in intervals:
        last = merged_intervals[-1]

        if inter[0] <= last[1]:
            last[1] = max(last[1], inter[1])
        else:
            merged_intervals.append(inter)

    amount_fresh = sum(end - start + 1 for start, end in merged_intervals)
    print(amount_fresh)
