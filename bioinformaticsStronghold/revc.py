#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")
dnaString = file.readline().strip()

complements = {"A":"T", "T":"A", "G":"C", "C":"G"}
complement = ""

for letter in dnaString:
    complement += complements[letter]

print(complement[::-1])
