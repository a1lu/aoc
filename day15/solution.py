#!/bin/env python3

def lastNumber(starting, count):

    history = dict()
    for i,n in enumerate(starting[:-1]):
        history[n] = i

    lastNum = starting[-1]

    for turn in range(len(starting[:-1]), count-1):
        num = turn - history.get(lastNum, turn)
        history[lastNum] = turn
        lastNum = num

    return num



with open("input") as file:
    lines = file.readlines()
    starting = list(map(int, lines[0].strip().split(',')))

    print("1/2:", lastNumber(starting, 2020))
    print("2/2:", lastNumber(starting, 30000000))
