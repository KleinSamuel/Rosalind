#!/usr/bin/python3

givenInteger = 24

new = 1
old = 0

for i in range(givenInteger-1):
    tmp = old
    old = new
    new += tmp

print(new)
