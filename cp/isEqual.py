def isEqual(s: str, t: str) -> bool:
    i = len(s)-1
    j = len(t)-1
    skipS = skipT = 0

    while i >= 0 or j >= 0:
        # shrink in s
        while i >= 0:
            if s[i] == "#":
                skipS += 1
                i -= 1
            elif skipS:
                skipS -= 1
                i -= 1
            else:
                break

        # shrink in t
        while j >= 0:
            if t[j] == "#":
                skipT += 1
                j -= 1
            elif skipT:
                skipT -= 1
                j -= 1
            else:
                break


        if i>=0 and j>=0:
            if s[i] != t[j]:
                return False
        elif i>=0 or j>=0:
                return False

        # decrease the index
        i -= 1
        j -= 1

    return True
        
s = input()
t = input()
ans = isEqual(s, t)
print(ans)


# from itertools import zip_longest

# def next_char(s):
#     skip = 0
#     for ch in reversed(s):
#         if ch == '#':
#             skip += 1
#         elif skip:
#             skip -= 1
#         else:
#             yield ch

# def isEqual(s, t):
#     for a, b in zip_longest(next_char(s), next_char(t)):
#         if a != b:
#             return False
#     return True

# ! STACK can also be used but it will consume extra memory

