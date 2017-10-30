#!/usr/bin/python3

import sys

filepath = sys.argv[1]

file = open(filepath, "r")

header = file.readline().strip().split()

degree = {}
neighbors = {}

for i in range(1,int(header[0])+1):
    degree[i] = 0
    neighbors[i] = []

for line in file:
    tmp = line.strip().split()

    for i in range(2):
        degree[int(tmp[i])] = degree[int(tmp[i])] + 1
        neighbors[int(tmp[i])].append(int(tmp[1-i]))

for k, v in sorted(degree.items()):
    sum = 0
    for neighbor in neighbors[k]:
        sum += degree[neighbor]
    print(sum, "", end="")
print()
