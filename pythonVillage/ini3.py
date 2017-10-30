#!/usr/bin/python3

longString = "zLGCKxdhJzEF2SiVchGxxHpLptvBKpW5WCLh5lyWqqU8d07rcOT4LftkprFa3AntaresiawQrunRqtZXY4lDTbKysCykP3APlosQKTt8Uk6kZ9LrapaxDF4ZAaKnzXl2MbSZPo3R3FdRWxg38wcGwItXzaO0P1HwgaiWtWAGEGxxrjaUk"
numberString = "61 69 111 115"

numberArray = numberString.split()

firstSubstring = longString[int(numberArray[0]):int(numberArray[1])+1]
secondSubstring = longString[int(numberArray[2]):int(numberArray[3])+1]

print(firstSubstring+" "+secondSubstring)
