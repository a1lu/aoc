#!/bin/env python3

def calculate(numbers, operators, plus=False):
    while len(operators) > 0 and operators[-1] != '(':
        if plus and operators[-1] != '+':
            break
        op = operators.pop()
        if op == '+':
            res = numbers.pop() + numbers.pop()
        elif op == '*':
            res = numbers.pop() * numbers.pop()
        numbers.append(res)


def evaluate(lines, part2=False):
    result = 0
    for line in lines:
        operators = []
        numbers = []
        for c in line:
            if c.isnumeric():
                numbers.append(int(c))
                calculate(numbers, operators, part2)
            else:
                if c in ['(', ')','+','*']:
                    if c == ')':
                        calculate(numbers, operators)
                        if operators[-1] == '(':
                            operators.pop()
                            calculate(numbers, operators, part2)
                    else:
                        operators.append(c)

        calculate(numbers, operators)
        result += numbers[0]
    return result

with open("input") as file:
    lines = file.readlines()

    print("1/2:", evaluate(lines,False))
    print("2/2:", evaluate(lines,True))


