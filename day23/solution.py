#!/bin/env python3

pick = [None] * 3
pick_nums = [None] * 3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    indices = [None] * 1_000_001
    nodes = None
    def __init__(self, items):
        self.start_node = None
        self.generate(items)

    def print(self):
        c = self.start_node
        while True:
            print(c.value,"", end= '')
            c = c.next
            if c == self.start_node:
                break
        print("")
    def to_str(self):
        ret = ""
        c = self.start_node
        while True:
            ret += str(c.value)
            c = c.next
            if c == self.start_node:
                break

        return ret

    def generate(self, cups):
        p = None
        self.nodes = [Node(i) for i in cups]
        for n in self.nodes:
            if not self.start_node:
                self.start_node = n
            else:
                p.next = n
            self.indices[n.value] = n

            p = n

        n.next=self.start_node



def simulate(cups, turns, max_label):
    for loops in range(0, turns):

        current = cups.start_node

        pf = current.next
        pl = current.next.next.next

        pick_nums[0] = pf.value
        pick_nums[1] = pf.next.value
        pick_nums[2] = pf.next.next.value

        current.next = pl.next

        destination = current.value - 1
        if destination == 0:
            destination = max_label
        while destination in pick_nums:
            destination -= 1
            if destination == 0:
                destination = max_label

        dest = cups.indices[destination]
        pl.next = dest.next
        dest.next=pf
        cups.start_node = cups.start_node.next

    return cups


def p1(cups):
    max_label = max(cups)
    l = simulate(List(cups), 100, max_label)
    return l.to_str()[1:]

def p2(cups):
    max_label = max(cups) + 1
    while max_label != 1_000_001:
        cups.append(max_label)
        max_label += 1

    l = simulate(List(cups), 10_000_000, 1_000_000)

    return l.indices[1].next.value * l.indices[1].next.next.value


with open("input") as file:
    lines = file.readlines()
    cups = [int(x) for line in lines for x in line.strip() ]

    print("1/2:", p1(cups.copy()))
    print("2/2:", p2(cups.copy()))
