#!/usr/bin/env python3


def find_max_jolt(bank: list[int], cur_index: int):
    ma = max(bank)
    ma_index = bank.index(ma)

    while len(bank) - ma_index - 1 < 11 - cur_index:
        ma = max(bank[:ma_index])
        ma_index = bank.index(ma)

    return ma, ma_index


with open("./input") as input:
    banks = [[int(joltage) for joltage in line.strip()] for line in input.readlines()]

    total_output = 0

    for bank in banks:
        sub_jolts = ""

        for i in range(11):
            ma, ma_index = find_max_jolt(bank, i)

            sub_jolts += str(ma)
            bank = bank[ma_index + 1 :]

        joltage = int(sub_jolts) * 10 + max(bank)
        total_output += joltage

    print(total_output)
