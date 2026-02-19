# smallest substring of s containing all chars of t (with freq)
from collections import Counter, defaultdict

def minimum_window(s: str, t: str) -> str:
    # if t is longer, impossible to form window
    if len(t) > len(s):
        return ""

    # freq map of required chars
    need = Counter(t)
    # freq map of current window
    window = defaultdict(int)

    # no. of unique chars required
    required = len(need)
    # how many chars currently meet required freq
    formed = 0
    # left ptr
    l = 0

    # track min window length & starting idx
    minLen, start = float("inf"), 0

    # expand window using right ptr
    for r in range(len(s)):
        c = s[r]

        # add curr char to window
        window[c] += 1

        # if this char is needed & its freq matches requirement
        if c in need and window[c] == need[c]:
            formed += 1
        
        # shrink window while it's valid
        while l<=r and formed == required:

            # update min window
            if r-l+1 < minLen:
                minLen = r-l+1
                start = l
            
            # remove left char from window
            left = s[l]
            window[left] -= 1

            # if removing makes it invalid, decrease formed
            if left in need and window[left] < need[left]:
                formed -= 1
            
            # move left ptr
            l += 1

    return "" if minLen == float("inf") else s[start:start+minLen]

s = input()
t = input()
print(minimum_window(s, t))




# from collections import Counter, defaultdict

# def min_window(s: str, t: str) -> str:

#     if len(t) > len(s):
#         return ""
    
#     need = Counter(t)
#     window = defaultdict(int)

#     l = start = 0
#     minLen = float("inf")

#     required = len(need)
#     formed = 0

#     for r in range(len(s)):
#         c = s[r]
#         window[c] += 1

#         if c in need and window[c] == need[c]:
#             formed += 1

#         while l <= r and formed == required:
#             if r-l+1 < minLen:
#                 minLen = r-l+1
#                 start = l
            
#             left = s[l]
#             window[left] -= 1

#             if left in need and window[left] < need[left]:
#                 formed -= 1

#             l += 1
        
#     return "" if minLen == float("inf") else s[start: start+minLen]


# print(min_window(s, t))

