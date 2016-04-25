###############################################STDIN###########################################################################
import sys        # you must import "sys" to read from STDIN
stdin = sys.stdin
text = stdin.readline().strip()
k = int(stdin.readline().strip())
profile = {}
for i in range(4):
    profile['ACGT'[i]] = [float(item) for item in stdin.readline().strip().split()]
###############################################STDIN############################################################################

###############################################MAINCODE#########################################################################
def profile_most_probable_kmer(text, k, profile):
    mostProbVal = -1
    mostProbKmer = ''
    for i in range(0, 1 + len(text) - k):
        kmer = text[i:i+k]
        probKmerVal = _pr(kmer, profile)
        if probKmerVal > mostProbVal:
            mostProbVal = probKmerVal
            mostProbKmer = kmer
    return mostProbKmer
###############################################MAINCODE#########################################################################

###################################################SubCodes#####################################################################
def _pr(text, profile):
    P = 1
    for i in range(len(text)):
        P = P * profile[text[i]][i]
    return P
###################################################SubCodes#####################################################################

###############################################STDOUT############################################################################
print (profile_most_probable_kmer(text, k, profile))
###############################################STDOUT############################################################################
