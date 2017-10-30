#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")

firstDnaString = file.readline().strip()
secondDnaString = file.readline().strip()

hammingDistance = 0

for i in range(len(firstDnaString)):
    if firstDnaString[i] != secondDnaString[i]:
        hammingDistance += 1

print(hammingDistance)
