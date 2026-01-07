# 3. Longest Substring Without Repeating Characters

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         if n == 0:
#             return 0
        
#         hs = set({})
#         hs.add(s[0])
#         ans = 1        
#         i,j = 0,1

#         while j<n:
#             while s[j] in hs:
#                 hs.discard(s[i])
#                 i+=1
#             hs.add(s[j])
#             j+=1
#             ans = max(ans, j-i)

#         return ans



class Solution:
    # “Instead of shrinking the window character by character, 
    # we track the last index of each character and jump the left pointer directly.”

    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1]*128 # ASCII size -> constant space

        i=0 # left pointer
        ans=0

        for j, ch in enumerate(s):
            idx = ord(ch)

            # if character was seen inside the current window
            if last[idx] >= i:
                i = last[idx] + 1

            last[idx] = j
            ans = max(ans, j-i+1)

        return ans
