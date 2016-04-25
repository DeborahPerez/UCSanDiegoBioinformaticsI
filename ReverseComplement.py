
# coding: utf-8

# In[3]:

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Pattern = lines[0]

def ReverseComplement(Pattern):
    revComp = '' 
    revPat = reverse(Pattern)
    for Nucleotide in revPat:
        revComp += complement(Nucleotide)
    return revComp

def reverse(text):
    result = ''
    count = len(text) -1
    for x in text:
        result += text[count]
        count -=1
    return result

def complement(Nucleotide):
    comp = '' 
#    for base in Nucleotide:
    if Nucleotide is 'A':
        comp += 'T'
    elif Nucleotide is 'T':
        comp += 'A'
    elif Nucleotide is 'C':
        comp += 'G'
    elif Nucleotide is 'G':
        comp += 'C'
    else:
        stop
    return comp

print (ReverseComplement(Pattern))


# In[ ]:



