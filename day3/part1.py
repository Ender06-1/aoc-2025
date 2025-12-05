#!/usr/bin/env python3

with open("./input") as input:
    banks = [[int(joltage) for joltage in line.strip()] for line in input.readlines()]

    total_output = 0

    for bank in banks:
        ma = max(bank)
        ma_index = bank.index(ma)

        if ma_index == len(bank) - 1:
            ma = max(bank[: len(bank) - 1])
            ma_index = bank.index(ma)

        ma2 = max(bank[ma_index + 1 :])

        total_output += ma * 10 + ma2

    print(total_output)
