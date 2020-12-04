#!/bin/env python3
import re

def parse(line):
    return dict(s.split(':', 1) for s in line.split())

def validatePassport(pp):
    if not all (k in pp for k in ("byr","iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        return False
    return True


def validatePassport2(pp):
    if not all (k in pp for k in ("byr","iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        return False

    if not (1920 <= int(pp["byr"]) <= 2002):
        return False

    if not (2010 <= int(pp["iyr"]) <= 2020):
        return False

    if not (2020 <= int(pp["eyr"]) <= 2030):
        return False

    if not ( pp["hgt"].endswith("cm") or pp["hgt"].endswith("in")):
        return False

    if (m := re.match(r'^(\d+)(in|cm)$', pp["hgt"])) is None:
        return False

    if (m[2] == "cm") and not (150 <= int(m[1]) <= 193):
        return False
    if (m[2] == "in") and not (59 <= int(m[1]) <= 76):
        return False

    if not re.match(r'^#[0-9a-f]{6}$', pp["hcl"]):
        return False

    if not re.match(r'^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$', pp["ecl"]):
        return False

    if not re.match(r'^\d{9}$', pp["pid"]):
        return False

    return True

def validate(lines, validator):
    passport = {}
    validPassports = 0
    for line in lines:
        if line.isspace():
            if validator(passport):
                validPassports += 1
            passport =  {}
            continue
        passport.update(parse(line))

    if validator(passport):
        validPassports += 1

    return validPassports

with open("input") as file:
    lines = file.readlines()

    valid = validate(lines, validatePassport)
    print("1/2:", valid)


    valid = validate(lines, validatePassport2)
    print("2/2:", valid)

