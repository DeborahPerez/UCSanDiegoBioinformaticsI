
# coding: utf-8

# In[7]:

#We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern' 
#of Text having d or fewer mismatches with Pattern; that is, HammingDistance(Pattern, Pattern') ≤ d. Our observation that a DnaA 
#box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.

#Find all approximate occurrences of a pattern in a string. 
#d number of mismatches
#def ApproximatePatternMatching(Pattern, Text):
#    positions = [] # initializing list of positions
#    HD = HammingDistance(Pattern, Text)
#    k = len(Pattern)
#    for i in range(k):
#        if HammingDistance(Pattern, kmer) <= d:
    # your code here

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Pattern = lines[0]
Text = lines[1]
d = int(lines[2])
    
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # output variable
    # your code here
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:len(Pattern)+1] != Pattern:
            if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
                positions.append(i)
    return (' '.join(map(str, positions)))

def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count


print (ApproximatePatternMatching(Pattern, Text, d))


# In[ ]:



