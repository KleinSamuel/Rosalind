#!/usr/bin/python3

import sys

filepath = sys.argv[1]

file = open(filepath, "r")

stringArray = file.readline().strip().split()

dict = {}

for word in stringArray:
    if word in dict:
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1

for key, value in dict.items():
    print(key," ",value)
