'''
📌 Problem Statement

You are given two strings s and t.

Each string may contain:
    Lowercase letters a-z
    The special character #
    Digits 0-9 (possibly multi-digit numbers)

The rules for processing a string are:
    A lowercase letter is added to the resulting string.
    The character # deletes one previous character, if any.
    A number (one or more consecutive digits) represents an integer K and deletes K previous characters, if possible.
    If there are fewer than K characters available, delete all of them.
    Delete operators (# and numbers) do not appear in the final string.

After processing both strings according to the rules above, determine whether the final resulting strings are equal.
'''



def isEqual4(s: str, t: str) -> bool:
    i = len(s) - 1
    j = len(t) - 1
    skipS = skipT = 0

    # while at least one string still has chars
    while i >= 0 or j >= 0:
        #process s
        while i >= 0:
            # If digit found, build full multi-digit number
            if s[i].isdigit():
                num, base = 0, 1
                while i >= 0 and s[i].isdigit():
                    num += int(s[i]) * base
                    base *= 10
                    i -= 1
                skipS += num

            # If '#' found, delete one previous character
            elif s[i] == '#':
                skipS += 1
                i -= 1

            # If there are pending deletions, skip character
            elif skipS > 0:
                skipS -= 1
                i -= 1

            # Valid character found
            else:
                break

        # process t
        while j >= 0:
            if t[j].isdigit():
                num, base = 0, 1
                while j >= 0 and t[j].isdigit():
                    num += int(t[j]) * base
                    base *= 10
                    j -= 1
                skipT += num

            elif t[j] == '#':
                skipT += 1
                j -= 1

            elif skipT > 0:
                skipT -= 1
                j -= 1

            else:
                break

        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            return False

        i -= 1
        j -= 1

    return True

s = input()
t = input()
print(isEqual4(s, t))

