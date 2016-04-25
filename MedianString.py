
# coding: utf-8

# In[ ]:

###############################################STDIN###########################################################################
import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k = int(lines[0])
Dna = []
for i in range(1, len(lines)):
    Dna.append(lines[i])
###############################################STDIN############################################################################

###############################################MAINCODE#########################################################################
def MedianString(Dna, k): #MEDIANSTRING(Dna, k)
    Distance = float("inf") #distance ← ∞
    for i in range(0, 4**k): #for i ←0 to 4k −1
        Pattern = NumberToPattern(i, k) #Pattern ← NumberToPattern(i, k)
        if Distance > distanceBetweenPatternAndStrings(Pattern, Dna): #if distance > DistanceBetweenPatternAndStrings(Pattern, Dna)
            Distance = distanceBetweenPatternAndStrings(Pattern, Dna) #distance ← DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern #Median ← Pattern
    return Median
###############################################MAINCODE#########################################################################

###################################################SubCodes#####################################################################
################################HammingDistance#########################################
def distanceBetweenPatternAndStrings(Pattern, Dna): #distanceBetweenPatternAndStrings(Pattern, Dna)
    k = len(Pattern) #k ← |Pattern|
    Distance = 0 #distance ← 0
    for string in  Dna: #for each string Text in Dna
        hammingDistance = float("inf") #HammingDistance ← ∞
        for i in range(0, len(string)-k+1): #for each k-mer Pattern’ in Text
            if hammingDistance > HammingDistance(Pattern, string[i:i+k]): #if HammingDistance > HammingDistance(Pattern, Pattern’)
                hammingDistance = HammingDistance(Pattern, string[i:i+k]) #HammingDistance ← HammingDistance(Pattern, Pattern’)
        Distance = Distance + hammingDistance#distance ← distance + HammingDistance
    return Distance
################################distanceBetweenPatternAndStrings#########################################

################################HammingDistance#########################################
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
################################HammingDistance#########################################

################################NumberToPattern#########################################
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
################################NumberToPattern#########################################
###################################################SubCodes#####################################################################

###############################################STDOUT###########################################################################
print (MedianString(Dna, k))
###############################################STDOUT###########################################################################
