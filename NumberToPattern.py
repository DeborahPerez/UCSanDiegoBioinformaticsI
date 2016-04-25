
# coding: utf-8

# In[8]:

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

#index = 45

#k = 4

def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = Quotient(index, 4)
    r = Remainder(index, 4)
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    return PrefixPattern + symbol

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
    return int(num)//n

print (NumberToPattern(index, k))


# In[ ]:



