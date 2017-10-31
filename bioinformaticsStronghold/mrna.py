#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")

codons = {
    "I": 3, "L": 6, "V": 4, "F": 2, "M": 1, "C": 2, "A": 4,
    "G": 4, "P": 4, "T": 4, "S": 6, "Y": 2, "W": 1, "Q": 2,
    "N": 2, "H": 2, "E": 2, "D": 2, "K": 2, "R": 6, "STOP": 3
}

proteinString = file.readline().strip()

possibleSource = 1

for letter in proteinString:
    possibleSource *= codons[letter]
possibleSource *= codons["STOP"]

print(possibleSource%1000000)
