#!/bin/env python3

with open("input") as file:
    lines = file.readlines()
    report = {}
    for line in lines:
        number = int(line.strip())
        if not number in report:
            report[number] = number

        search = 2020 - number
        if search in report:
            print("result: ",search," * ", number, " = ", search*number)
            break



    report = {}
    for line in lines:
        number = int(line.strip())
        if not number in report:
            report[number] = number

        for line2 in lines:
            number2=int(line2.strip())
            search = 2020 - number - number2
            if search in report:
                print("result: ",search," * ", number, " * ", number2," = ",
                      search * number * number2)
                exit()
