#!/usr/bin/env python3

with open("input") as input:
    instructions = [(line[0], int(line[1:])) for line in input.readlines()]

    pos = 50
    zero_count = 0

    for direction, distance in instructions:
        if direction == "L":
            new_pos = (100 if pos == 0 else pos) - distance

            pos = new_pos % 100
            zero_count += abs(new_pos // 100)

            if pos == 0:
                zero_count += 1
        else:
            new_pos = pos + distance

            pos = new_pos % 100
            zero_count += new_pos // 100

    print(zero_count)
