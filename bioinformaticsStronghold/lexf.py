#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")

symbols = file.readline().strip().split()
n = int(file.readline().strip())

result = symbols

for i in range(n-1):
    new = []
    for elem in result:
        for symbol in symbols:
            new.append(elem+symbol)
    result = new

for elem in result:
    print(elem)
