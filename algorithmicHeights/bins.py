#!/usr/bin/python3

import sys

filepath = sys.argv[1]

file = open(filepath, "r")

n = file.readline().strip()
m = file.readline().strip()
sortedArray = file.readline().strip().split()
unSortedArray = file.readline().strip().split()

def binarySearch(toSearch, array):
    leftIndex = 0
    rightIndex = len(array) - 1
    index = -1

    while leftIndex <= rightIndex:
        tmp = leftIndex + int((rightIndex - leftIndex) / 2)

        if int(array[tmp]) == toSearch:
            index = tmp + 1
            break
        elif int(array[tmp]) < toSearch:
            leftIndex = tmp+1
        else:
            rightIndex = tmp-1

    return index

for toSearch in unSortedArray:
    print(binarySearch(int(toSearch), sortedArray), "", end="")
print()
