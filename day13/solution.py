#!/bin/env python3

import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def p1(busses, earliest):
    nearest = earliest
    res = 0
    for b in bus:
        if b != 'x':
            x = math.ceil(earliest / b) * b
            diff = x - earliest
            if diff < nearest:
                res = diff * b
                nearest = diff

    return res

def p2(bus):
    l = [(b,o) for o,b in enumerate(bus) if b != 'x'  ]
    l.sort()
    l = l[::-1]

    n = 1
    step = 1
    for (b,o) in l:
        while (n + o) % b != 0:
            n += step

        step *= b

    return n

with open("input") as file:
    lines = file.readlines()
    earliest = int(lines[0].strip())

    line = lines[1].strip()
    bus = [int(x) if x != 'x' else x for x in line.split(',')]
    print("1/2:", p1(bus, earliest))
    print("2/2:", p2(bus))
