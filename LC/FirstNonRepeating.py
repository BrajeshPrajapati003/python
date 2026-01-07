# 387 -> First Unique Character in a String

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         dict1 = {}

#         # frequency count
#         for ch in s:
#             dict1[ch] = dict1.get(ch, 0) + 1

#         # find first unique character INDEX
#         for i in range(len(s)):
#             if dict1[s[i]] == 1:
#                 return i

#         return -1



class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        # count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0)+1

        # find first unique character
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        
        return -1
