#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")
dnaString = file.readline().strip()

nucleotides = {}

for letter in dnaString:
    if letter in nucleotides:
        nucleotides[letter] = nucleotides[letter] + 1
    else:
        nucleotides[letter] = 1

for k, v in sorted(nucleotides.items()):
    print(v, "", end="")
print()
