#!/bin/env python3

def traverse(lines, slope):
    pos = slope
    trees = 0
    lineNum = 1
    for line in lines[1:]:
        row = [c == '#' for c in line]
        lineNum += 1
        if lineNum <= pos[1]:
            continue

        if row[pos[0]]:
            trees += 1

        pos = ((pos[0]+ slope[0]) % (len(row) - 1), pos[1] + slope[1])
    return trees


with open("input") as file:
    lines = file.readlines()
    slope = (3, 1)
    trees = traverse(lines, slope)

    print("1/2:", trees)

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    trees = 1
    for slope in slopes:
        trees *= traverse(lines, slope)

    print("2/2:", trees)

