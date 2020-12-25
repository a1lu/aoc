#!/bin/env python3

def calc(num, sub):
    return num * sub % 20201227

def transform(subject_number, loops):
    num = 1
    for i in range(0, loops):
        num = calc(num, subject_number)

    return num

with open("input") as file:
    lines = file.readlines()
    pk_card, pk_door = int(lines[0].strip()), int(lines[1].strip())

    num = 1
    i  = 1
    while True:
        num = calc(num, 7)
        if num == pk_card:
            key = transform(pk_door, i)
            break
        if num == pk_door:
            key = transform(pk_card, i)
            break

        i += 1

    print("1/2:", key)
