#!/usr/bin/python3

import sys

filepath = sys.argv[1]

file = open(filepath, "r")

lineCounter = 1

for line in file:
    if lineCounter % 2 == 0:
        print(line.strip())
    lineCounter += 1
