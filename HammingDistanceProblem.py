
# coding: utf-8

# In[1]:

# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.

import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

p = lines[0]
q = lines[1]
def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

print (HammingDistance(p, q))


# In[ ]:



