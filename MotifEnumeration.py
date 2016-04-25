
####################################STDIN#####################################################################
import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k, d = map(int, lines[0].split(" "))
Dna = []
Dna.append(lines[1])
Dna.append(lines[2])
Dna.append(lines[3])
Dna.append(lines[4])
Dna.append(lines[5])
Dna.append(lines[6])

####################################STDIN######################################################################

#######################################TESTINPUT###############################################################
#k = 3
#d = 1
#Dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
#######################################TESTINPUT##############################################################


#CHECK FOR MOST COMMON KMERS IN DNA STRINGS THEN PROCEED


#########################################MotifEnumerationMAINCODE#############################################
def MotifEnumeration(Dna, k, d):
    Patterns = set() #Patterns ← an empty set
    for strand in Dna:
        Length = len(strand)
        for i in range(0, Length-k+1):
            Pattern = strand[i:i+k]
            neighbors = Neighbors(Pattern, d)
            for candidate in neighbors:
                if patternIsMotif(Dna, candidate, d) == True:
                    Patterns.add(candidate)
    Patterns = remove_duplicates(Patterns)
    return Patterns
#########################################MotifEnumerationMAINCODE#############################################



#########################################SubCodes##############################################################
def patternIsMotif(Dna, pattern, d):
    for strand in Dna:
        if PatternIsApproxContained(strand, pattern, d) == False:
            return False
    return True

def PatternIsApproxContained(strand, pattern, d):
    Length = len(strand)
    for i in range(0, Length-k+1):
        if HammingDistance(pattern, strand[i:i+k]) <=d:
            return True
    return False




##############NeighborsSTART#####################
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
##############NeighborsEND#####################

###############RemoveDuplicatesSTART###########
def remove_duplicates(Text):
    ItemsNoDuplicates = []
    for item in Text:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates
###############RemoveDuplicatesEND###########

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:len(Pattern)+1] == Pattern:
            count += 1
        elif Text[i:len(Pattern)+1] != Pattern:
            if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
                count += 1
    return count

###############RemoveDuplicatesSTART###########
def remove_duplicates(Text):
    ItemsNoDuplicates = []
    for item in Text:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates
###############RemoveDuplicatesEND###########

####################################STDOUT#####################################################################
print (' '.join(map(str, (MotifEnumeration(Dna, k, d)))))
#print ((MotifEnumeration(Dna, k, d)))
####################################STDOUT#####################################################################


# In[ ]:
