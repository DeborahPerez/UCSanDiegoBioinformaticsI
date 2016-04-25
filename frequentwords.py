import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Text = lines[0]
k = int(lines[1])

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

def remove_duplicates(Text):
    ItemsNoDuplicates = []
    for item in Text:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates

def CountDict(Text, k):
    Count = {} # output variable
    # your code here
    for i in range((len(Text))-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

print (FrequentWords(Text, k))
