#!/usr/bin/env python3

with open("./input") as input:
    grid = [line.strip() for line in input.readlines()]

    accessible_rolls = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):

            if grid[y][x] != "@":
                continue

            roll_count = 0

            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if (
                        j < 0
                        or j >= len(grid)
                        or i < 0
                        or i >= len(grid[y])
                        or (j == y and i == x)
                    ):
                        continue

                    roll_count += 1 if grid[j][i] == "@" else 0

            accessible_rolls += 1 if roll_count < 4 else 0

    print(accessible_rolls)
