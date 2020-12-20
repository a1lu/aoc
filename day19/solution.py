#!/bin/env python3

import re

def build_regex(rules, index, max_len, depth):
    if index == '8' or index == '11':
        depth += 1
        if depth >= max_len:
            return ""
    regex = ""
    if '|' in rules[index]:
        regex += '('
    for k in rules[index]:
        if k.isnumeric():
            regex += build_regex(rules, k, max_len, depth)
        else:
            if k in ['a', 'b']:
                depth += 1
            regex += k

    if '|' in rules[index]:
        regex += ')'
    return regex


with open("input") as file:
    lines = file.read()

    rules, messages = lines.split("\n\n")
    rules = rules.split("\n")
    messages = messages.split("\n")

    max_len = max(messages, key=len)
    print(len(max_len))

    rules_dict = {}
    for r in rules:
        i,v = r.split(":")
        v = v.replace('"', '')
        rules_dict[i] = v.strip().split()
    print(rules_dict)

    regex = "^" + build_regex(rules_dict, '0', 6, 0) + "$"

    print(len(regex))
    valid = 0
    for m in messages:
        if re.match(regex,m):
            valid += 1

    print(valid)


