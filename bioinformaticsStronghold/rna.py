#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")
dnaString = file.readline().strip()

rnaString = ""

for letter in dnaString:
    if letter == "T":
        rnaString += "U"
    else:
        rnaString += letter

print(rnaString)
