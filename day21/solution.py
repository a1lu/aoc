#!/bin/env python3
import re
from collections import defaultdict

with open("input") as file:
    lines = file.readlines()
    foods = []
    all_ingredients = set()
    allergen_to_food = {}
    for line in lines:
        ingredients, allergens = line.split("(contains ")
        ingredients = ingredients.split()
        allergens = allergens[:-2].split(", ")
        foods += [(ingredients, allergens)]
        all_ingredients.update(ingredients)

        for a in allergens:
            if a not in allergen_to_food:
                allergen_to_food[a] = set(ingredients)
            else:
                allergen_to_food[a] = allergen_to_food[a].intersection(ingredients)

    cant_contain = set(all_ingredients)
    for v in allergen_to_food.values():
        cant_contain -= v

    count = 0
    for line in foods:
        for f in cant_contain:
            if f in line[0]:
                count += 1

    print("1/2:", count)


    assigned = set()
    assignment = {}

    loop = True
    while loop:
        loop = False
        for k,v in allergen_to_food.items():
            remain = v - assigned
            if len(remain) == 1:
                assignment[k] = remain
                assigned.update(remain)
            elif len(remain) > 1:
                loop = True

    arrange = list(assignment.keys())
    arrange.sort()
    ret = ""
    for a in arrange:
        ret += ''.join(assignment[a])+','

    print("2/2:", ret[:-1])
