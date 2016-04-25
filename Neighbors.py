
# coding: utf-8

# In[22]:

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Pattern = lines[0]
d = int(lines[1]) 

def Neighbors(Pattern, d):
    if d == 0:
        return ([Pattern])
    if len(Pattern) == 1:
        return (['A', 'C', 'G', 'T'])
    Neighborhood = []
    SuffixNeighbors = Neighbors(suffix(Pattern), d)

    for Text in (SuffixNeighbors):
        if HammingDistance(suffix(Pattern), Text) <d:
            for base in "ACGT":
                Neighborhood.append(base + Text)
        else:
            Neighborhood.append(FirstSymbol(Pattern) + Text)
    return (Neighborhood)


def FirstSymbol(Pattern):
    return Pattern[0]

def suffix(Pattern):
    suffix = Pattern[1:len(Pattern)]
    return (suffix)

##HammingDistance code START
def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
##HammingDistance code END

print ('\n'.join(map(str, (Neighbors(Pattern, d)))))


# In[ ]:
