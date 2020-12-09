#!/bin/env python3

PREAMBLE = 25

def validate(numbers, num):
    mem = set()
    for i in numbers:
        search = num - i
        if search in mem:
            return True
        mem.add(i)
    return False

def first(lines):
    numbers = []
    for line in lines:
        num = int(line.strip())
        if len(numbers) == PREAMBLE:
            if not validate(numbers, num):
                return num
            numbers.pop(0)
        numbers += [num]

def second(lines, search):
    numbers = []
    for line in lines:
        num = int(line.strip())
        if sum(numbers) < search:
            numbers += [num]
            continue
        while sum(numbers) > search:
            numbers.pop(0)
        if sum(numbers) == search:
            return min(numbers) + max(numbers)

        numbers += [num]


with open("input") as file:
    lines = file.readlines()
    result = first(lines)
    print("1/2:", result)

    print("2/2:", second(lines, result))

