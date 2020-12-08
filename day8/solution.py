#!/bin/env python3

import copy

def runProgram(prog):
    acc = 0
    pc = 0
    executed = []
    finished = False
    while True:
        if pc == len(prog):
            finished = True
            break
        if pc in executed:
            break
        executed += [pc]
        line = prog[pc]
        op, arg = line
        if op == "nop":
            pc += 1
            continue
        if op == "acc":
            acc += int(arg)
            pc += 1
            continue
        if op == "jmp":
            pc += int(arg)
            continue
    return (acc, finished)

def solution1(lines):
    prog = list(map(str.split, lines))
    acc, finished = runProgram(prog)
    return acc


def solution2(lines):
    prog = list(map(str.split, lines))
    nops = []
    jmps = []
    for i, x in enumerate(prog):
        if x[0] == "nop":
            nops += [i]
        elif x[0] == "jmp":
            jmps += [i]

    for l in nops:
        tmp = copy.deepcopy(prog)
        tmp[l][0] = "jmp"
        (acc, finished) = runProgram(tmp)
        if finished:
            return acc

    for l in jmps:
        tmp = copy.deepcopy(prog)
        tmp[l][0] = "nop"
        (acc, finished) = runProgram(tmp)
        if finished:
            return acc

with open("input") as file:
    lines = file.readlines()

    print("1/2:", solution1(lines))
    print("2/2:", solution2(lines))
