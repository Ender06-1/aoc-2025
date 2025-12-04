#!/usr/bin/env python3

with open("input") as input:
    instructions = [(line[0], int(line[1:])) for line in input.readlines()]

    pos = 50
    zero_count = 0

    for direction, distance in instructions:
        if direction == "L":
            pos = (pos - distance) % 100
        else:
            pos = (pos + distance) % 100

        if pos == 0:
            zero_count += 1

    print(zero_count)
