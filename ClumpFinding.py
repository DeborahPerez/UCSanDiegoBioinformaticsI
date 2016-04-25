
# coding: utf-8

# In[36]:

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Genome = lines[0]
k, L, t = map(int, lines[1].split(" "))  

def ClumpFinding(Genome, k, L, t):
    FrequentPatterns = []
    CLump = {}
    for i in range(0, 4**k):
        CLump[i] = 0
    for i in range(len(Genome)-L + 1):
        Text = Genome[i:i+L]
        FrequencyArray = ComputingFrequencies(Text, k)
        for index in range(4**k):
            Value = int(FrequencyArray[index])
            if Value > t: 
                CLump[index] = 1
            elif Value == t:
                CLump[index] = 1
    for i in range(4**k):
        if CLump[i]==1:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return (' '.join(map(str, FrequentPatterns)))
        
        
        
##ComputingFrequencies code START
def ComputingFrequencies(Text, k):
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
        return (''.join(map(str, Array['frequency'])))
    
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
##ComputingFrequencies code END

print (ClumpFinding(Genome, k, L, t))


# In[ ]:



