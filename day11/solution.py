#!/bin/env python3

import copy

FREE = 'L'
FLOOR = '.'
OCCUPIED = '#'
WILL_OCC = 'O'
WILL_FREE = 'E'

def isFree(row, col, seats):
    return seats[row][col] == FREE

def isOcc(row, col, seats):
    return seats[row][col] == OCCUPIED

def wasOcc(row, col, seats):
    return seats[row][col] in [OCCUPIED, WILL_FREE]

def step(seats, s_map, offset=0):
    ret = False
    for seat in seats:
        occupied = 0
        for n in seat["nb"]:
            if wasOcc(n[0], n[1], s_map):
                occupied += 1
        (i,j) = seat["pos"]
        if isFree(i, j, s_map) and occupied == 0:
            s_map[i][j] = 'O'
            ret = True
        elif isOcc(i, j, s_map) and occupied >= (4 + offset):
            s_map[i][j] = 'E'
            ret = True

    for seat in seats:
        (i,j) = seat["pos"]
        if s_map[i][j] == WILL_OCC:
            s_map[i][j] = OCCUPIED
        elif s_map[i][j] == WILL_FREE:
            s_map[i][j] = FREE

    return ret


def findNeighbours(seats, part):
    positions = []
    directions = [(-1, 0), (-1, 1), (0, 1), (1,1), (1,0), (1, -1), (0,-1),
                  (-1,-1)]
    (rows, columns) = (len(seats), len(seats[0]))
    for i,row in enumerate(seats[1:-1], 1):
        for j,p  in enumerate(row[1:-1],1):
            if p == FLOOR:
                continue
            if isFree(i,j, seats):
                tmp= {"pos":(i,j), "nb": []}
                for dir in directions:
                    (k,l) = (i,j)
                    while 0 <= k < rows-1 and 0 <= l < columns-1:
                        k += dir[0]
                        l += dir[1]
                        if isFree(k,l,seats):
                            tmp["nb"] += [(k, l)]
                            break
                        if part == 1:
                            break
                positions += [tmp]

    return positions


def solve(seats, nb, offset = 0):
    while step(nb, seats, offset):
        continue

    occ = 0
    for seat in nb:
        (i,j) = seat["pos"]
        if isOcc(i,j, seats):
            occ += 1
    return occ

with open("input") as file:
    seats = []
    lines = file.readlines()
    row_len = len(lines[0].strip())
    seats += [[ '.' for i in range(0,row_len+2)]]
    for line in lines:
        seats += [list('.') + list(line.strip()) + list('.')]

    seats += [[ '.' for i in range(0,row_len+2)]]

    nb1 = findNeighbours(seats, 1)
    seats1 = copy.deepcopy(seats)
    print("1/2:", solve(seats1, nb1))

    nb2 = findNeighbours(seats, 2)
    seats2 = copy.deepcopy(seats)
    print("2/2:", solve(seats2, nb2, 1))
