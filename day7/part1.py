#!/usr/bin/env python3

with open("./input") as input:
    manifold = input.readlines()

    positions = {manifold[0].find("S")}
    split_amount = 0

    for line in manifold[1:]:
        for i in range(len(line)):
            if i in positions and line[i] == "^":
                split_amount += 1

                positions.add(i - 1)
                positions.add(i + 1)
                positions.remove(i)

    print(split_amount)
