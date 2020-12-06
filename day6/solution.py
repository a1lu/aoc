#!/bin/env python3

def count(lines, operation):
    questions = None
    sum = 0
    for line in lines:
        if line.isspace():
            sum += len(questions)
            questions = None
            continue
        line = line.strip()
        if questions == None:
            questions = set(line)
        else:
            questions = operation(questions, set(line))

    sum += len(questions)
    return sum

with open("input") as file:
    lines = file.readlines()

    print("1/2:", count(lines, set.union))
    print("2/2:", count(lines, set.intersection))
