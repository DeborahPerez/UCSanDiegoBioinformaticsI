
# coding: utf-8

# In[ ]:

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Genome = lines[0]

def Skew(Genome):
    skew = {}
    n = len(Genome)
    for i in range(1, n+1):
        skew[0] = 0
        if Genome[i-1] == "G":
            skew[i] = skew[i-1] + 1
        elif Genome[i-1] == "C":
            skew[i] = skew[i-1] - 1
        else:
            skew[i] = skew[i-1]
    skewlist = []
    for i in range(len(Genome)+1):
        skewlist.append(skew[i])
    return (' '.join(map(str, skewlist)))

print (Skew(Genome))
