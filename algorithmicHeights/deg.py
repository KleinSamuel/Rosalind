#!/usr/bin/python3

import sys

filepath = sys.argv[1]

file = open(filepath, "r")

file.readline()

dict = {}

for line in file:
    tmp = line.strip().split()

    for i in range(2):
        if int(tmp[i]) in dict:
            dict[int(tmp[i])] = dict[int(tmp[i])] + 1
        else:
            dict[int(tmp[i])] = 1

for k, v in sorted(dict.items()):
    print(v, "", end="")
print()
