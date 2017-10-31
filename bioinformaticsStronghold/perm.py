#!/usr/bin/python3

input = 6

list = []

for i in range(input):
    list.append(i+1)

def permutate(list):

    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]

    out = []

    for i in range(len(list)):
        extracted = list[i]
        new = list[:i] + list[i+1:]

        for j in permutate(new):
            out.append([extracted] + j)

    return out

result = permutate(list)

print(len(result))
for tmp in result:
    for i in tmp:
        print(i, "", end="")
    print()
