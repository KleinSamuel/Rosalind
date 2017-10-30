#!/usr/bin/python3

import sys

filepath = sys.argv[1]
file = open(filepath, "r")

fastaHeader = []
currentDnaString = ""
index = -1

outputGCPercentage = 0.0
outputIndex = -1

def processDnaString(dnaString):
    global index
    global outputGCPercentage
    global outputIndex
    if len(dnaString) > 0:
        gcCount = 0
        totalCount = 0
        for letter in dnaString:
            if (letter == "G") or (letter == "C"):
                gcCount += 1
            totalCount += 1
        tmpContent = float("{0:.6f}".format((gcCount / totalCount)*100))
        if tmpContent > outputGCPercentage:
            outputGCPercentage = tmpContent
            outputIndex = index
    index += 1
    return

for line in file:
    if line.startswith(">"):
        processDnaString(currentDnaString)
        currentDnaString = ""
        fastaHeader.append(line.strip())
    else:
        currentDnaString += line.strip()
processDnaString(currentDnaString)

print(fastaHeader[outputIndex][1:])
print(outputGCPercentage)
