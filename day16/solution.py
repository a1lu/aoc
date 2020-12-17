#!/bin/env python3
import re
from collections import defaultdict

def parse(lines):
    section = 0
    fields = {}
    rules = {}
    nearby = []
    for line in lines:
        if line.isspace():
            section += 1
            continue
        line = line.rstrip()
        if section == 0:
            sp = line.split(": ")
            rules[sp[0]] = [ list(map(int, r.split("-"))) for r in sp[1].split(" or ")]
        elif section == 1:
            if line.startswith("your"):
                continue
            my = list(map(int, line.split(",")))
        elif section == 2:
            if line.startswith("nearby"):
                continue
            values = list(map(int, line.split(",")))
            nearby += [values]

    return rules, my, nearby

def valid(v, rules):
    validRules = []
    for r in rules:
        for i in rules[r]:
            if i[0] <= v <= i[1]:
                validRules += [r]
                break
    return validRules

def p1(fields):
    rules, my, nearby = fields[0], fields[1], fields[2]
    sum = 0
    for n in nearby:
        for v in n:
            if not len(valid(v, rules)):
                sum += v

    print(sum)

def p2(fields):
    rules, my, nearby = fields[0], fields[1], fields[2]
    assigned = set()
    mult = 1
    rd = dict()
    for n in nearby:
        for i, v in enumerate(n):
            rules1 = valid(v, rules)
            if l := len(rules1):
                if i in rd:
                    rd[i] = rd[i].intersection(set(rules1))
                else:
                    rd[i] = set(rules1)

    loop = True
    while loop:
        loop = False
        for a in rd:
            rd[a] -= assigned
            if len(rd[a]) == 1:
                for x in rd[a]:
                    if x.startswith("de"):
                        mult *= my[a]
                assigned.update(rd[a])
            elif len(rd[a]) > 1:
                loop = True

    print(mult)


with open("input") as file:
    lines = file.readlines()
    p1(parse(lines))
    p2(parse(lines))
