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


def process(s: str) -> str:
    stack = []
    history = [] # store deleted chunks for undo
    i = 0

    while i<len(s):
        if s[i].isdigit():
            num = 0
            while i<len(s) and s[i].isdigit():
                num = num*10 + int(s[i])
                i += 1
            
            deleted = []
            for _ in range(num):
                if stack:
                    deleted.append(stack.pop())

            history.append(deleted)

        elif s[i] == '#':
            deleted = []
            if stack:
                deleted.append(stack.pop())
            history.append(deleted)
            i += 1
        
        elif s[i] == '@':
            if history:
                last_deleted = history.pop()
                stack.extend(reversed(last_deleted))
            i += 1
        
        else:
            stack.append(s[i])
            i += 1
        
    return "".join(stack)

def isEqualComplex(s: str, t: str) -> bool:
    return process(s) == process(t)

s = input()
t = input()
print(isEqualComplex(s, t))


# extend(iterable) -> adds each element of the iterable to the list. It doesn't add the iterable as a single element.
# append(x) -> adds as one item
