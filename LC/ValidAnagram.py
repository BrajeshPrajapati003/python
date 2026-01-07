# 242 Valid Anagram

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#              return False

#         freq = {}
#         for ch in s:
#             freq[ch] = freq.get(ch, 0) + 1

#         for ch in t:
#             if ch not in freq:
#                 return False
#             freq[ch] -= 1
#             if freq[ch] == 0:
#                 del freq[ch]
        
#         return len(freq) == 0
    


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
    

# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         freq = [0]*26

#         for ch in s:
#             freq[ord(ch) - ord('a')] += 1

#         for ch in t:
#             idx = ord(ch) - ord('a')
#             freq[idx] -= 1
#             if freq[idx] < 0:
#                 return False
            
#         return True
    


class Solution:
    def sortString(self, s):
        return "".join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for s in strs:
            key = self.sortString(s)
            # if key in map:
            #     map[key].append(s)
            # else:
            #     map[key] = [s] # IMP: str : list pairs
            map.setdefault(key, []).append(s)

        return list(map.values())

