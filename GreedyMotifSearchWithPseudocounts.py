
# coding: utf-8

# In[12]:

###############################################STDIN###########################################################################
import sys        # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines()        # read in the input from STDIN

k, t = map(int, lines[0].split(" "))
Dna = []
for i in range(1, len(lines)):
    Dna.append(lines[i])
###############################################STDIN############################################################################

###############################################TESTINPUT########################################################################
#Dna = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
#k = 3
#t = 5
###############################################TESTINPUT########################################################################

###############################################MAINCODE#########################################################################
def greedy_motif_search_with_pseudocounts(Dna, k, t):
    bestMotifs = []
    for i in range(0, t):
        bestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        motifs = []
        motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = profile_with_pseudocounts(motifs[0:j])
            motifs.append(profile_most_probable_kmer(Dna[j], k, P))
        if _score(motifs) < _score(bestMotifs):
            bestMotifs = motifs
    return (bestMotifs)
###############################################MAINCODE#########################################################################

###################################################SubCodes#####################################################################
def profile_with_pseudocounts(motifs):
    profile = {}
    t = len(motifs)
    k = len(motifs[0])
    countMotifs = count_with_pseudocounts(motifs)

    for symbol in "ACGT":
        profile[symbol] = []

    for x in countMotifs:
        for y in countMotifs[x]:
            z = y/float(t+4)
            profile[x].append(z)

    return profile

def count_with_pseudocounts(motifs):
    count = {}
    pseudocounts = {}
    t = len(motifs)
    k = len(motifs[0])

    for symbol in "GACT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            count[symbol][j] += 1

    for symbol in "GACT":
        pseudocounts[symbol] = []

    for x in count:
        for y in count[x]:
            z = y + 1
            pseudocounts[x].append(z)

    return pseudocounts

def _score(motifs):
    count = 0
    k = len(motifs[0])
    t = len(motifs)
    consensusMotif = _consensus(motifs)
    for i in range(t):
        for j in range(k):
            if motifs[i][j] != consensusMotif[j]:
                count += 1
    return count

def _consensus(motifs):
    k = len(motifs[0])
    count = count_with_pseudocounts(motifs)

    consensus = ""
    for j in range(k):
        M = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > M:
                M = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def profile_most_probable_kmer(text, k, profile):
    mostProbVal = -1
    mostProbKmer = ''
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        probKmerVal = _pr(kmer, profile)
        if probKmerVal > mostProbVal:
            mostProbVal = probKmerVal
            mostProbKmer = kmer
    return mostProbKmer

def _pr(text, profile):
    P = 1
    for i in range(len(text)):
        P = P * profile[text[i]][i]
    return P
###################################################SubCodes#####################################################################

###############################################STDOUT############################################################################
print ('\n'.join(greedy_motif_search_with_pseudocounts(Dna, k, t)))
###############################################STDOUT############################################################################


# In[ ]:
