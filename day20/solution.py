#!/bin/env python3.9

import numpy as np
import math

grid = {}
grid_len = 0

def get_tile(i, arr):
    if i < 4:
        l = np.rot90(arr, i)
    else:
        l = np.rot90(np.flip(arr, 0), i - 4)
    return l


def get_slices(arr):
    return [[arr[0,:]], # top
            [arr[:,-1]], # right
            [arr[-1,:]], # bot
            [arr[:,0]], # left
            ]

def check_left(arr, pos):
    x,y = pos
    prev = grid[(x, y-1)]
    s1 = get_slices(arr)
    s2 = get_slices(prev)
    return all(s1[3][0] == s2[1][0])

def check_top(arr, pos):
    x,y = pos
    prev = grid[(x-1, y)]
    s1 = get_slices(arr)
    s2 = get_slices(prev)
    return all(s1[0][0] == s2[2][0])

def fit(pos, arr):
    if len(grid) == 0:
        return True
    x,y = pos
    if (x, y-1) in grid:
        fit_left = check_left(arr, pos)
    else:
        fit_left = y == 0

    if (x-1, y) in grid:
        fit_top = check_top(arr, pos)
    else:
        fit_top = True

    return fit_left and fit_top


def solve(tiles, used, pos):
    if len(used) == len(tiles):
        return (True, used)
    for k1 in tiles:
        if k1 in used:
            continue
        current_used = used.copy()
        current_used += [k1]
        arr = tiles[k1]
        for i in range(0,8):
            tile = get_tile(i, arr)
            fitts = fit(pos, tile)
            if fitts:
                grid[pos] = tile
                pos_new = (pos[0], pos[1]+1)
                if pos_new[1] >= grid_len:
                    pos_new = (pos_new[0] + 1, 0)
                success, indices = solve(tiles, current_used, pos_new)
                if not success:
                    del grid[pos]
                else:
                    return (success, indices)

    return (False, used)

with open("input") as file:
    lines = file.read()

    input = lines.split("\n\n")
    tiles = {}

    for tile in input:
        tile = tile.split("\n")
        tid = int(tile[0][5:-1])
        values = []
        for i,l in enumerate(tile[1:]):
            if len(l.strip()):
                values += [[ x for x in l.strip()]]
        tiles[tid] = np.array(values)



    grid_len = int(math.sqrt(len(tiles)))
    r, used = solve(tiles, [], (0,0))

    used = np.reshape(used, (-1,grid_len))
    print("1/2:", used[0,0] * used[0,-1] * used[-1,0] * used[-1,-1])

    pic_rows = []
    for i in range(0, grid_len):
        keys = [(i,y) for y in range(0, grid_len)]
        pic_rows.append(np.concatenate([grid[k][1:-1, 1:-1] for k in keys], axis = 1))

    pic = np.empty(shape=(grid_len,0))

    monster =["                  # ",
              "#    ##    ##    ###",
              " #  #  #  #  #  #   "]

    seamonster = [(y,x) for y,l in enumerate(monster) for x,c in enumerate(l) if
                 c == '#']

    monster_len = len(monster[0])
    monster_height = 3

    image = np.concatenate(pic_rows, axis = 0)
    image_len = len(image)

    for i in range(0,8):
        found = False
        img = np.copy(get_tile(i, image))
        for x in range(0, image_len-(monster_height)):
            for y in range(0, image_len-(monster_len-1)):
                monster_found = True
                monster = [(k[0]+x,k[1]+y) for k in seamonster]
                for m in monster:
                    if img[m] != '#':
                        monster_found = False
                        break
                if monster_found:
                    found = True
                    for m in monster:
                        img[m] = 'O'
        if found:
            print("2/2:", (img == '#').sum())
            exit(0)
