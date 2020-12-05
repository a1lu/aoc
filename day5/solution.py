#!/bin/env python3
import math
import functools

def getSeatId(string):
    l = list(map( lambda b: 0 if b in ['F', 'L'] else 1, string))
    return functools.reduce(lambda a,b : (a << 1) + b, l)

def first(lines):
    maxId = 0
    for line in lines:
        id = getSeatId(line.strip())
        maxId = max(maxId, id)
    return maxId

def second(lines):
    maxId = 0
    minId = 1024
    sum = 0
    for line in lines:
        id = getSeatId(line.strip())
        maxId = max(maxId, id)
        minId = min(minId, id)
        sum += id

    allSeats = ((maxId - minId + 1) * (maxId + minId)) / 2
    return allSeats - sum


with open("input") as file:
    lines = file.readlines()

    result = first(lines)
    print("1/2:", result)


    result = second(lines)
    print("2/2:", result)

