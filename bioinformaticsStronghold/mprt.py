#!/usr/bin/python3

import sys
import re
import urllib.request

filepath = sys.argv[1]
file = open(filepath, "r")

def getFastaFromUniprot(id):
    response = urllib.request.urlopen("http://www.uniprot.org/uniprot/"+id+".fasta")
    content = response.read()
    contentString = content.decode("utf8")
    response.close()
    return contentString

def getSequenceFromFasta(fastaString):
    sequence = ""
    for line in re.split("\n", fastaString):
        if not line.startswith(">"):
            sequence += line.strip()
    return sequence

def findMotifInSequence(sequence):
    motif = "N[^P][ST][^P]"
    indices = []

    for i in range(0, len(sequence)-4):
        if re.compile(motif).match(sequence[i:i+4]):
            indices.append(i+1)
    return indices

for line in file:
    url = line.strip()
    content = getFastaFromUniprot(url)
    fastaString = getSequenceFromFasta(content)
    indices = findMotifInSequence(fastaString)

    if len(indices) > 0:
        print(url)
        for index in indices:
            print(index, "", end="")
        print()
