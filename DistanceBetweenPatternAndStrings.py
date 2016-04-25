
###############################################STDIN###########################################################################
import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Pattern = lines[0]
Dna = lines[1].split(" ")
###############################################STDIN############################################################################

###############################################MAINCODE#########################################################################
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
###############################################MAINCODE#########################################################################

###################################################SubCodes#####################################################################
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
###################################################SubCodes#####################################################################

###############################################STDOUT############################################################################
print (distanceBetweenPatternAndStrings(Pattern, Dna))
###############################################STDOUT############################################################################
