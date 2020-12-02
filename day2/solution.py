#!/bin/env python3

with open("input") as file:
    lines = file.readlines()

    print("part 1/2")
    valid = 0
    for line in lines:
        parts=line.strip().split()
        min, max = [int(parts[0].split('-')[i]) for i in (0,1)]
        counter = parts[2].count(parts[1][0])

        if counter >= min and counter <= max:
            valid += 1

    print(valid)

    print("part 2/2")
    valid = 0
    for line in lines:
        parts=line.strip().split()
        first, second = [int(parts[0].split('-')[i]) -1 for i in (0,1)]

        password = parts[2]
        key = parts[1][0]

        if (password[first] == key) ^ (len(password) > second and
                                       password[second] == key):
            valid += 1



    print(valid)
