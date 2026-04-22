'''
Given 2 anagrams s1 & s2.
Allowed moves: swap any 2 characters in s1
Goal: Min. swaps needed to make s1 == s2

Input: s1 = "abac", s2 = "baca"
Output: 2
'''

# idea:
# 1. Find 1st idx i where s != target
# 2. Only swap with j where: s[j] == target[i]

from collections import deque

def kSimilarity(s1, s2):

    q = deque([(s1, 0)])
    vis = set([s1])

    while q:
        s, steps = q.popleft()

        if s == s2:
            return steps
        
        # find first mismatch
        i = 0
        while s[i] == s2[i]:
            i += 1

        for j in range(i+1, len(s)):

            # only swap useful chars
            if s[j] == s2[i] and s[j] != s2[j]:

                new_s = list(s)
                new_s[i], new_s[j] = new_s[j], new_s[i]
                new_s = "".join(new_s)

                if new_s not in vis:
                    vis.add(new_s)
                    q.append((new_s, steps+1))
