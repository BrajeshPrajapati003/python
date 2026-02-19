def isEqualAfterOpr(s: str, t: str) -> bool:
    i = len(s)-1
    j = len(t)-1
    skipS = skipT = 0

    while i>=0 or j>=0:
        # skip in s
        while i>=0:
            if '0' <= s[i] <= '9':
                skipS += int (s[i])
                i-=1
            elif skipS:
                i -= 1
                skipS -= 1
            else:
                break
        
        # skip in t
        while j>=0:
            if '0' <= t[j] <= '9':
                skipT += int (t[j])
                j-=1
            elif skipT:
                j -= 1
                skipT -= 1
            else:
                break
        
        if i>=0 and j>=0:
            if s[i] != t[j]:
                return False
        elif i>=0 or j>=0:
            return False

        i-=1
        j-=1
        
    return True
        

s = input()
t = input()
ans = isEqualAfterOpr(s, t)
print(ans)
