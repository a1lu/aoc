#!/bin/env python3
import re


def getRules(lines):
    bags = {}
    for line in lines:
        line=line.strip()
        if line.endswith("no other bags."):
            continue
        line = re.sub(r' bags?', '', line)
        line = re.sub(r' contain', ',', line)
        line = list(map(str.strip, line[:-1].split(',')))
        bag = line[0]
        contains = line[1:]

        m= list(map(lambda x: re.match(r'(\d+) (\w+ \w+)', x), contains))

        container = {}
        for e in m:
            container[e[2]] = int(e[1])

        bags[bag] = container
    return bags

def contains(rules, color, search):
    count = 0
    for c in rules[color]:
        if c == search:
            return True
        elif c in rules:
            if contains(rules, c, search):
                return True
    return False

def solution1(lines, search):
    rules = getRules(lines)
    count = 0
    for bag in rules:
        if contains(rules, bag, search):
            count += 1

    return count

def countBags(rules, search):
    count = 0
    x = rules[search]
    for bag in x:
        num = x[bag]
        count += num
        if bag in rules:
            count += num * countBags(rules, bag)

    return count

def solution2(lines, search):
    rules = getRules(lines)
    count = countBags(rules, search)
    return count

with open("input") as file:
    lines = file.readlines()

    print("1/2:", solution1(lines, "shiny gold"))
    print("2/2:", solution2(lines, "shiny gold"))
