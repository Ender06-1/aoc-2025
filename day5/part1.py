#!/usr/bin/env python3

with open("./input") as input:
    raw_database = [line.split() for line in input.read().split("\n\n")]
    intervals = list(
        map(
            lambda i: (int(i[0]), int(i[1])),
            [inter.split("-") for inter in raw_database[0]],
        )
    )
    ids = [int(id) for id in raw_database[1]]

    fresh_ids = 0
    for id in ids:
        for inter in intervals:
            if id >= inter[0] and id <= inter[1]:
                fresh_ids += 1
                break

    print(fresh_ids)
