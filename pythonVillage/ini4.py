#!/usr/bin/python3

inputString = "4124 8337"
inputArray = inputString.split()

firstInteger = int(inputArray[0])
secondInteger = int(inputArray[1])

sumOfOdds = 0

for i in range(firstInteger, secondInteger+1):
    if(i % 2 != 0):
        sumOfOdds += i

print(sumOfOdds)
