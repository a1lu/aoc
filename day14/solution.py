#!/bin/env python3
import re
from collections import defaultdict
import functools

def setBit(value, bit):
    return value | (1 << bit)
def clrBit(value, bit):
    return value & ~(1 << bit)

def applyMaskValue(value, mask):
    for (i,b) in mask:
        if b == 1:
            value = setBit(value, i)
        else:
            value = clrBit(value, i)

    return value

def p1(lines):
    memory = defaultdict(int)
    for line in lines:
        if line.startswith("mask"):
            mask = [(i,int(v)) for i,v in enumerate(line[:-39:-1].strip()) if v!= 'X']
            continue
        m = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
        memory[m[1]] = applyMaskValue(int(m[2]), mask)
    result = functools.reduce(lambda a, v: a + v, memory.values())
    print("1/2:", result)


def applyMaskMemory(value, mask):
    values = []
    x_bits= []
    for (i,b) in mask:
        if b == 1:
            value |= 1 << i
        if b == 'X':
            x_bits+=[i]

    num_permutations = 2**len(x_bits)
    for i in range(0, num_permutations):
        v = value
        for j,x in enumerate(x_bits):
            if i & (1<<j) == 0:
                v = clrBit(v, x)
            else:
                v = setBit(v, x)
        values += [v]

    return values

def p2(lines):
    memory = defaultdict(int)
    for line in lines:
        if line.startswith("mask"):
            mask = [(i,int(v)) if v != 'X' else (i,v) for i,v in enumerate(line[:-39:-1].strip())]
            continue
        m = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
        memories = applyMaskMemory(int(m[1]), mask)
        for mem in memories:
            memory[mem] = (int(m[2]))

    result = functools.reduce(lambda a, v: a + v, memory.values())
    print("2/2:", result)

with open("input") as file:
    lines = file.readlines()

    p1(lines)
    p2(lines)
