#!/usr/bin/env python3

from functools import reduce


with open("./input") as input:
    raw_input = [line.replace("\n", "") for line in input.readlines()]
    numbers, operators = raw_input[:-1], raw_input[-1]
    calcs = []
    col = 0
    while col < len(numbers[0]):
        cur_op = operators[col]
        tmp = 0
        nums = []

        while tmp != -1 and col < len(numbers[0]):
            tmp = -1
            for i in range(len(numbers)):
                c = numbers[i][col]
                if c != " ":
                    if tmp == -1:
                        tmp = 0
                    tmp = tmp * 10 + int(c)

            if tmp != -1:
                nums.append(tmp)
            col += 1

        calcs.append(nums + [cur_op])

    total = 0
    for calc in calcs:
        if calc[-1] == "+":
            total += sum(calc[:-1])
        elif calc[-1] == "*":
            total += reduce(lambda acc, e: acc * e, calc[:-1])
        else:
            print(f"Symbol '{calc[-1]}' not supported")

    print(total)
