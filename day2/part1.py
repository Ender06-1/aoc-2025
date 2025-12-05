#!/usr/bin/env python3

with open("input") as input:
    intervals = list(
        map(
            lambda i: (i[0], i[1]),
            [inter.split("-") for inter in input.read().strip().split(",")],
        )
    )

    def is_invalid(num):
        return num[: len(num) // 2] == num[len(num) // 2 :]

    invalids = [
        num
        for inter in intervals
        for num in range(int(inter[0]), int(inter[1]))
        if is_invalid(str(num))
    ]

    print(sum(invalids))
