#!/bin/env python3

def calculate_score(cards):
    score = 0
    for i in range(0,len(cards)):
        score += cards[::-1][i] * (i+1)

    return score

def recursive_combat(cards1, cards2):
    played_games = set()

    while True:
        setting = (tuple(cards1), tuple(cards2))

        if setting in played_games:
            return 1, cards1
        else:
            played_games.add(setting)
        a = cards1.pop(0)
        b = cards2.pop(0)

        if len(cards1) >= a and len(cards2) >= b:
            winner, _ = recursive_combat(cards1[0:a].copy(),
                                         cards2[0:b].copy())
        else:
            if a > b:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            cards1 += [a,b]
        else:
            cards2 += [b,a]

        if len(cards1) == 0:
            return 2, cards2
        elif len(cards2) == 0:
            return 1, cards1

def combat(cards1, cards2):
    while len(cards1) > 0 and len(cards2) > 0 :
        a = cards1.pop(0)
        b = cards2.pop(0)
        if a > b:
            cards1 += [a,b]
        else:
            cards2 += [b,a]

    score = 0
    if len(cards1):
        cards = cards1
    else:
        cards = cards2

    return calculate_score(cards)

with open("input") as file:
    player1, player2 = file.read().split("\n\n")

    player1 = player1.split("\n")[1:]
    player2 = player2.split("\n")[1:-1]
    cards1 = []
    cards2 = []
    for a,b in zip(player1, player2):
        cards1 += [int(a)]
        cards2 += [int(b)]

    print("1/2:", combat(cards1.copy(), cards2.copy()))
    _, cards = recursive_combat(cards1.copy(), cards2.copy())
    print("2/2:", calculate_score(cards))
