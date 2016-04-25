
# coding: utf-8

# In[5]:

####################################STDIN####################################################
import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Genome = lines[0]
k, L, t = map(int, lines[1].split(" "))

#######################################TESTINPUT##############################################

#Genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
#k= 5
#L = 50
#t = 4

########################################BetterClumpFindingMainCODE##############################
def BetterClumpFinding(Genome, k, L, t):
    FrequentPatterns = []
    CLump = {}
    for i in range(0, 4**k):
        CLump[i] = 0
    Text = Genome[0:L+1]
    FrequencyArray = ComputingFrequencies(Text, k)
    for index in range(4**k):
        if FrequencyArray[index] >= t:
            CLump[index] = 1
    for i in range(1, len(Genome)-L+1):
        FirstPattern = Genome[i-1:(i-1)+k]
        index = PatternToNumber(FirstPattern)
        FrequencyArray[index] -= 1
        LastPattern = (Genome[i + L - k:(i + L - k)+k])
        index = PatternToNumber(LastPattern)
        FrequencyArray[index] += 1
        if FrequencyArray[index] >= t:
            CLump[index] = 1

    for i in range(4**k):
        if CLump[i]==1:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

########################################################SubCodes#############################################

###NumberToPatter code START############################################
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
###NumberToPatter code END############################################

#########################ComputingFrequencies code START#####################
def ComputingFrequencies(Text, k):
    FrequencyArray ={}
    for i in range(0, 4**k):
        FrequencyArray[i] = 0
    for i in range(0, len(Text)-k+1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] += 1
    return FrequencyArray

#PatternToNumber code START
def PatternToNumber(Pattern):
    prefix = ''
    if Pattern == '':
        return 0
    symbol = Lastsymbol(Pattern)
    prefix = (Prefix(Pattern))
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def Lastsymbol(Pattern):
    return Pattern[-1]

def Prefix(Pattern):
    return Pattern[:len(Pattern)-1]

def SymbolToNumber(symbol):
    if symbol == "A":
        return 0
    elif symbol == "C":
        return 1
    elif symbol == "G":
        return 2
    else:
        return 3
#PatternToNumber code End

def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
#########################ComputingFrequencies code END#####################

print (' '.join(map(str, BetterClumpFinding(Genome, k, L, t))))


# In[ ]:
