
# coding: utf-8

# In[78]:

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Text = lines[0]
k = int(lines[1])

def allkmers(Text, k):
    Array ={}
    for word in ["k-mer", "index", "frequency"]:
        Array[word] = []
    for i in range(0, 4**k):     
        Array['k-mer'].append(NumberToPattern(i, k))
    for i in range(0, 4**k):
        Array['index'].append(i)
    for i in range(0, 4**k):
        for item in Array['k-mer']:
            Array["frequency"].append(PatternCount(item, Text))
        return (' '.join(map(str, Array['frequency'])))

#NumberToPattern code START
def NumberToPattern(index, k):
    PrefixPattern = ''
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = Quotient(index, 4)
    r = Remainder(index, 4)
    symbol = NumberToSymbol(r)
    PrefixPattern += symbol
    for i in range(k-1):
            r = Remainder(int(prefixIndex), 4)
            symbol = NumberToSymbol(r)
            PrefixPattern += symbol
            prefixIndex = Quotient(int(prefixIndex), 4)
    return reverse(PrefixPattern)

def reverse(text):
    result = ''
    count = len(text) -1
    for x in text:
        result += text[count]
        count -=1
    return result

def NumberToSymbol(r):
    if r == 0:
        return "A"
    elif r == 1:
        return "C"
    elif r == 2:
        return "G"
    else:
        return "T"

def Remainder(num, n):
    return int(num)%n
    
def Quotient(num, n):
    return int(num)/n
#NumberToPattern code End

def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

print (allkmers(Text, k))


# In[ ]:



