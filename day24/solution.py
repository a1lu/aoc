#!/bin/env python3

from collections import defaultdict

with open("input") as file:
    lines = file.readlines()
    directions = {"e" : (1,-1,0), "se": (0, -1,1), "sw" : (-1,0,1), "w":
                  (-1,1,0),"nw" : (0,1,-1), "ne" : (1,0,-1)}
    start = (0,0,0)
    tiles = defaultdict(int)
    for line in lines:
        line = line.strip()
        buf = None
        pos = start
        for c in line:
            op = None
            if c in  ['s', 'n']:
                buf = c
            elif buf:
                op = buf + c
                buf = None
            elif c in ['e', 'w']:
                op = c
            if op:
                di = directions[op]
                pos = (pos[0] + di[0], pos[1] + di[1], pos[2] + di[2])

        tiles[pos] ^= 1

    tiles = { k:v for k, v in tiles.items() if v }
    print("1/2:", len(tiles))

    for i in range(0,100):
        nbs = defaultdict(int)
        for pos, c in tiles.items():
            for n in directions.values():
                nbs[tuple(map(sum, zip(pos, n)))] += 1

        new_tiles = { k:v for k, v in tiles.items() if k in nbs and nbs[k] <= 2 }
        new_tiles |= {pos: 1 for pos in nbs if pos not in tiles and nbs[pos] == 2}
        tiles = new_tiles

    print("2/2:", len(tiles))
