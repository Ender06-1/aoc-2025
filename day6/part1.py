#!/usr/bin/env python3

from functools import reduce


with open("./input") as input:
    raw_input = [line.strip().split() for line in input.readlines()]
    calcs = []
    for j in range(len(raw_input[0])):
        tmp = []
        for i in range(len(raw_input)):
            elem = raw_input[i][j]
            if elem.isdigit():
                elem = int(elem)
            tmp.append(elem)

        calcs.append(tmp)

    total = 0
    for calc in calcs:
        if calc[-1] == "+":
            total += sum(calc[:-1])
        elif calc[-1] == "*":
            total += reduce(lambda acc, e: acc * e, calc[:-1])
        else:
            print(f"Symbol '{calc[-1]}' not supported")

    print(total)
