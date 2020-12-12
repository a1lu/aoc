#!/bin/env python3

def move(dir, pos, value):
    if dir == "N":
        return (pos[0] - value, pos[1])
    if dir == "S":
        return (pos[0] + value, pos[1])
    if dir == "E":
        return (pos[0], pos[1] + value)
    if dir == "W":
        return (pos[0], pos[1] - value)

def forward(pos, dir, value):
    return (pos[0] + dir[0] * value, pos[1] + dir[1] * value)

def _rotate(d, p):
    if d == "R":
        return (p[1], -p[0])
    if d == "L":
        return (-p[1], p[0])

def rotate(pos, dir, value):
    value = int(value / 90)
    if value == 2:
        return (-pos[0], -pos[1])

    tmp = _rotate(dir, pos)
    if value == 3:
        tmp = (-tmp[0], -tmp[1])
    return tmp

def solve1(lines):
    dir = (0,1)
    pos = (0,0)

    for line in lines:
        action = line[0]
        value = int(line[1:])
        if action == "F":
            pos = forward(pos, dir, value)
        if action in "NSEW":
            pos = move(action, pos, value)
        if action in ["R", "L"]:
            dir = rotate(dir, action, value)

    print("1/2:", abs(pos[0]) + abs(pos[1]))

def solve2(lines):
    pos = (0,0)
    wp_pos = (-1, 10)

    for line in lines:
        action = line[0]
        value = int(line[1:])

        if action == "F":
            pos = forward(pos, wp_pos, value)
        if action in "NSEW":
            wp_pos = move(action, wp_pos, value)
        if action in ["R", "L"]:
            wp_pos = rotate(wp_pos, action, value)

    print("2/2:", abs(pos[0]) + abs(pos[1]))

with open("input") as file:
    lines = file.readlines()
    solve1(lines)
    solve2(lines)
