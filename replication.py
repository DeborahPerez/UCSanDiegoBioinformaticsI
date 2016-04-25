def FrequentWords(Text, k):
    FrequentPatterns = [] # output variable
    # your code here
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# Input:  A list Items
# Output: A list containing all objects from Items without duplicates
def remove_duplicates(Text):
    ItemsNoDuplicates = [] # output variable
    # your code here
    for item in Text:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
# HINT:   This code should be identical to when you last implemented CountDict
def CountDict(Text, k):
    Count = {} # output variable
    # your code here
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count


# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Now set Text equal to the Vibrio cholerae oriC and k equal to 10
Text = 'ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC'

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array
k = 10
# Finally, print the result of calling FrequentWords on Text and k.

print (FrequentWords(Text, k))

def Skew(Genome):
    skew = {}
    n = len(Genome)
    for i in range(1, n+1):
        skew[0] = 0
        if Genome[i-1] == "G":
            skew[i] = skew[i-1] + 1
        elif Genome[i-1] == "C":
            skew[i] = skew[i-1] - 1
        else:
            skew[i] = skew[i-1]
    return skew

def MinimumSkew(Genome):
    positions = []
    SkewGenome = Skew(Genome)
    m = min(SkewGenome.values())
    n = len(Genome)
    for i in range(1, n+1):
        if SkewGenome[i] == m:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    count = 0
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            count = count+1
            positions.append(i)
    return positions
