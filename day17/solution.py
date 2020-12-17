#!/bin/env python3

from collections import defaultdict
from itertools import product

def do_step(cubes, dim):
    nb = defaultdict(int)
    new_cubes = set()
    for vec in cubes:
        n = product([-1,0,1], repeat=dim)
        for v in n:
            if any(v):
                nb[tuple(x+dx for x, dx in zip(vec,v))] += 1

    for loc in cubes:
        n = nb[loc]
        if 2 <= n <= 3:
            new_cubes.add(loc)
    for loc, n in nb.items():
        if n == 3:
            new_cubes.add(loc)

    return new_cubes




with open("input") as file:
    lines = file.readlines()
    m = [x.rstrip().split("\n") for x in lines]

    cubes = {(i,j,0) for i in range(len(m)) for j in range(len(m[i][0])) if m[i][0][j] == '#'}

    dim = len(next(iter(cubes)))
    for i in range(0,6):
        cubes = do_step(cubes, dim)
    print("1/2:", len(cubes))

    cubes = {(i,j,0, 0) for i in range(len(m)) for j in range(len(m[i][0])) if m[i][0][j] == '#'}
    dim = len(next(iter(cubes)))
    for i in range(0,6):
        cubes = do_step(cubes, dim)
    print("2/2:", len(cubes))
