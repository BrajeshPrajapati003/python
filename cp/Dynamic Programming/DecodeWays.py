'''
LC 91. Decode Ways
A string containing digits from 0-9 can be decoded into letters using the mapping:
    1 → A
    2 → B
    ...
    26 → Z
Given a string s containing digits, return the number of ways to decode it.
'''
def numDecodings(s):
    # return decodeRecursion1(s, len(s)-1)
    # return decodeRecursion2(s, len(s)-1)

    # dp = [-1]*len(s)
    # return self.decodeMemo(s, dp, len(s)-1)

    # return self.decodeTabulation(s)
    return decodeConstantSpace(s)

def decodeRecursion1(s, idx):
    if idx < 0:
        return 1
    if s[idx] == '0':
        if idx >= 1 and s[idx-1] in "12":
            return decodeRecursion1(s, idx-2)
        return 0
    
    one = decodeRecursion1(s, idx-1)

    two = 0
    if idx >= 1:
        num = int(s[idx-1:idx+1])
        if 10 <= num <= 26:
            two = decodeRecursion1(s, idx-2)
    
    return one + two

def decodeRecursion2(s, idx):
    if idx < 0:
        return 1
    if s[0] == '0':
        return 0

    one = 0
    if s[idx] != '0':
        one = decodeRecursion2(s, idx-1)
    
    two = 0
    if idx >= 1:
        num = int(s[idx-1: idx+1])
        if 10 <= num <= 26:
            two = decodeRecursion2(s, idx-2)
    
    return one + two

def decodeMemo(s, dp, idx):
    if idx < 0:
        return 1
    
    if s[0] == '0':
        return 0
    
    if dp[idx] != -1:
        return dp[idx]

    # one digit
    one = 0
    if s[idx] != '0':
        one = decodeMemo(s, dp, idx-1)
    
    # two digits
    two = 0
    if idx >= 1:
        num = int(s[idx-1:idx+1])
        if 10 <= num <= 26:
            two = decodeMemo(s, dp, idx-2)
    
    dp[idx] = one + two
    return dp[idx]

def decodeTabulation(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0
    
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1, n+1):
    
        # take 1 digit
        if  s[i-1] != '0':
            dp[i] += dp[i-1] 

        # take 2 digits
        if i >= 2:
            num = int(s[i-2:i])
            if 10 <= num <= 26:
                dp[i] += dp[i-2]
    
    return dp[n]

def decodeConstantSpace(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0
    
    prev2, prev1 = 1, 1
    for i in range(1, n+1):
        curr = 0

        # decode 1 digit
        if s[i-1] != '0':
            curr += prev1
        
        # decode 2 digits
        if i>1:
            num = int(s[i-2:i])
            if 10 <= num <= 26:
                curr += prev2
        
        prev2 = prev1
        prev1 = curr
    
    return prev1

str = input().strip()
print(numDecodings(str))

# NOTE:
# Never update your previous DP states while calculating the current state. 
# Calculate curr first, then shift the previous states forward.
