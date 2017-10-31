#!/usr/bin/python3

import sys
import re

# read input file
filepath = sys.argv[1]
file = open(filepath, "r")

# read monoisotopic mass table
filepath = sys.argv[2]
table = open(filepath, "r")

mass = {}

for line in table:
    tmp = re.split("\t", line.strip())
    mass[tmp[0]] = float(tmp[1])

proteinmass = 0

for letter in file.readline().strip():
    proteinmass += mass[letter]

print(proteinmass)
