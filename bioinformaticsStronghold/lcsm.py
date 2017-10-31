#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")

fastaDict = {}
currentHeader = ""
currentSequence = ""

# store shortest sequence
shortestSequence = ""

for line in file:
    if line.strip().startswith(">"):
        if currentHeader != "":
            fastaDict[currentHeader] = currentSequence
            if (shortestSequence == "") or (len(currentSequence) < len(shortestSequence)):
                shortestSequence = currentSequence
        currentHeader = line.strip()
        currentSequence = ""
    else:
        currentSequence += line.strip()
fastaDict[currentHeader] = currentSequence
if (shortestSequence == "") or (len(currentSequence) < len(shortestSequence)):
    shortestSequence = currentSequence

def findSubstring(substring):
    flag = True
    for k, v in fastaDict.items():
        if v != shortestSequence:
            index = v.find(substring)
            if index == -1:
                flag = False
                break
    if flag:
        return substring
    return ""

for i in range(len(shortestSequence)+1, 0, -1):
    for j in range(len(shortestSequence)+1-i):
        subs = shortestSequence[j:j+i]
        result = findSubstring(subs)
        if result != "":
            print(result)
            exit()
