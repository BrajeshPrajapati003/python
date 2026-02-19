def isEqual3(s: str, t: str) -> bool:
    # start iterating from end
    i = len(s)-1
    j = len(t)-1
    skipS = skipT = 0
    
    # while at least one string still has chars
    while i>=0 or j>=0:
        
        # process s
        while i>=0:
            if s[i].isdigit():
                num = 0
                base = 1

                # build num in reverse (right -> left)
                while i>=0 and s[i].isdigit():
                    num += int(s[i]) * base
                    base *= 10
                    i-=1

                skipS += num
            elif skipS:
                skipS -= 1
                i-=1

            # found a valid char to compare
            else:
                break

        # process t
        while j>=0:
            if t[j].isdigit():
                num = 0
                base = 1
                while j>=0 and t[j].isdigit():
                    num += int(t[j]) * base
                    base *= 10
                    j-=1
                skipT += num
            elif skipT:
                    skipT -= 1
                    j-=1
            else:
                break
            
        
        if i>=0 and j>=0:
            if s[i] != t[j]:
                return False
        
        # if only one string has chars -> not equal
        elif i>=0 or j>=0:
            return False
        
        i-=1
        j-=1
    return True

s = input()
t = input()
print(isEqual3(s, t))
