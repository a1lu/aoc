#!/bin/env python3

lenmap = {}
def findArrangements(adapters):
    count = 0
    use = 1
    pos = len(adapters)
    if pos in lenmap:
        return lenmap[pos]
    while pos > use and adapters[use]-adapters[0] <= 3:
        if adapters[use] == adapters[-1]:
            count += 1
        count += findArrangements(adapters[use:])
        use += 1

    lenmap[pos] = count

    return count



with open("input") as file:
    lines = file.readlines()
    adapters = [ int(line.strip()) for line in lines ]
    adapters.sort()
    adapters += [adapters[-1]+3]
    adapters.insert(0, 0)
    dist = {1:0, 2:0, 3:0}
    last = 0
    for adapter in adapters[1:]:
        difference = adapter-last
        dist[difference] += 1
        last = adapter

    print("1/2:", dist[1] * dist[3])

    print("2/2:", findArrangements(adapters))
