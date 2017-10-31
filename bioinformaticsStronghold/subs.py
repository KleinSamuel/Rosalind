#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")

text = file.readline().strip()
pattern =file.readline().strip()

startIndex = 0

while True:
    index = text.find(pattern, startIndex)
    if index == -1:
        break
    else:
        print(index+1, "", end="")
        startIndex = index+1
print()
