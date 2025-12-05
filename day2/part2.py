#!/usr/bin/env python3

with open("input") as input:
    intervals = map(
        lambda i: (int(i[0]), int(i[1])),
        [inter.split("-") for inter in input.read().strip().split(",")],
    )

    def is_invalid(num):
        for i in range(len(num) // 2):
            if len(num.replace(num[: (i + 1)], "")) == 0:
                return True
        return False

    invalids = [
        num
        for inter in intervals
        for num in range(inter[0], inter[1])
        if is_invalid(str(num))
    ]

    print(sum(invalids))
